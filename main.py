import subprocess
import logging
import os
from argparse import ArgumentParser
import torch
from transformers import SeamlessM4Tv2Model, AutoProcessor
import scipy.io.wavfile
import torchaudio

# Setup logging
logging.basicConfig(level=logging.INFO)

# Initialize the processor and model
processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large")
model = SeamlessM4Tv2Model.from_pretrained("facebook/seamless-m4t-v2-large")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def download_video(url):
    download_directory = os.path.join('videos', 'source')
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
    video_file = os.path.join(download_directory, 'downloaded_video.mp4')
    command = ['yt-dlp', url, '-o', video_file]
    subprocess.run(command, check=True)
    return video_file

def trim_video(video_file, start_time, end_time):
    if not start_time or not end_time:
        return video_file
    trimmed_video_file = video_file.replace('.mp4', '_trimmed.mp4')
    command = ['ffmpeg', '-i', video_file, '-ss', start_time, '-to', end_time, '-c', 'copy', trimmed_video_file]
    subprocess.run(command, check=True)
    return trimmed_video_file

def extract_and_translate_audio(trimmed_video_file, target_language):
    audio_file_name = os.path.basename(trimmed_video_file).replace('.mp4', '_audio.wav')
    audio_file = os.path.join(os.path.dirname(trimmed_video_file), audio_file_name)

    if os.path.exists(audio_file):
        os.remove(audio_file)

    command = ['ffmpeg', '-i', trimmed_video_file, '-ar', '16000', '-ac', '1', audio_file]
    subprocess.run(command, check=True)

    waveform, orig_freq = torchaudio.load(audio_file)
    waveform_resampled = torchaudio.functional.resample(waveform, orig_freq, 16000)
    waveform_resampled = waveform_resampled.to(device)

    # Make sure to use 'audios' instead of 'audio'
    audio_inputs = processor(audios=waveform_resampled.squeeze().numpy(), sampling_rate=16000, return_tensors="pt").to(device)

    with torch.no_grad():
        translated_audio = model.generate(**audio_inputs, tgt_lang=target_language)
        # If the output is a tuple, we take the first element which is usually the desired tensor.
        translated_audio_tensor = translated_audio[0] if isinstance(translated_audio, tuple) else translated_audio
    translated_audio_array = translated_audio_tensor.cpu().numpy().squeeze()


    translated_audio_file = audio_file.replace('_audio.wav', '_translated.wav')
    scipy.io.wavfile.write(translated_audio_file, 16000, translated_audio_array)

    return translated_audio_file

def synthesize_voice_and_video(video_file, new_audio):
    # Placeholder for synthesizing voice and video (lip-syncing/mixing)
    # Add your code here for the actual processing
    pass

def process_local_video(video_directory):
    if not os.path.exists(video_directory):
        logging.error(f"Directory not found: {video_directory}")
        return None
    video_files = [f for f in os.listdir(video_directory) if f.endswith(('.mp4', '.avi', '.mov'))]
    return os.path.join(video_directory, video_files[0]) if video_files else None

if __name__ == "__main__":
    parser = ArgumentParser(description="Download, trim, translate and lip-sync a video.")
    parser.add_argument('--url', type=str, help="URL of the video to be downloaded.", required=False)
    parser.add_argument('--start_time', type=str, help="Start time for trimming the video (in format hh:mm:ss).", required=False)
    parser.add_argument('--end_time', type=str, help="End time for trimming the video (in format hh:mm:ss).", required=False)
    parser.add_argument('--target_language', type=str, help="Target language for translation.", required=True)

    args = parser.parse_args()

    if args.url:
        video_file = download_video(args.url)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        video_directory = os.path.join(base_dir, 'videos', 'source')
        video_file = process_local_video(video_directory)
        if not video_file:
            logging.error("No local video files found for processing.")
            exit(1)

    trimmed_video_file = trim_video(video_file, args.start_time, args.end_time)
    translated_audio_array = extract_and_translate_audio(trimmed_video_file, args.target_language)
    #synthesize_voice_and_video(trimmed_video_file, translated_audio_array)