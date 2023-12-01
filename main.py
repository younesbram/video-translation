import subprocess
import logging
import os
from argparse import ArgumentParser

logging.basicConfig(level=logging.INFO)

def download_video(url):
    # Define the directory to save downloaded videos
    download_directory = os.path.join('videos', 'downloaded')
    # Create the directory if it does not exist
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
    
    logging.info(f"Downloading video from {url}")
    # Update the path where the video will be saved
    video_file = os.path.join(download_directory, 'downloaded_video.mp4')

    # Construct yt-dlp command to download the video
    command = ['yt-dlp', url, '-o', video_file]

    try:
        subprocess.run(command, check=True)
        logging.info(f"Video downloaded successfully: {video_file}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error downloading video: {e}")
        raise
    return video_file

def trim_video(video_file, start_time, end_time):
    if start_time is None or end_time is None:
        logging.error("Start time or end time not provided for trimming.")
        return video_file

    trimmed_video_file = video_file.replace('.mp4', '_trimmed.mp4')
    # Construct FFmpeg command for trimming
    command = ['ffmpeg', '-i', video_file, '-ss', start_time, '-to', end_time, '-c', 'copy', trimmed_video_file]
    
    try:
        subprocess.run(command, check=True)
        logging.info(f"Video trimmed successfully: {trimmed_video_file}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error trimming video: {e}")
        raise
    return trimmed_video_file


def process_local_videos():
    # Get the directory of the script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Define the relative path to the videos/source directory
    video_directory = os.path.join(base_dir, 'videos', 'source')
    logging.info(f"Translating video(s) in {video_directory}")

    if not os.path.exists(video_directory):
        logging.error(f"Directory not found: {video_directory}")
        return

    video_files = [f for f in os.listdir(video_directory) if f.endswith(('.mp4', '.avi', '.mov'))]
    
    if not video_files:
        logging.info("No video files found in the directory.")
        return

    for video_file in video_files:
        video_path = os.path.join(video_directory, video_file)
        logging.info(f"Processing video: {video_path}")
        # Placeholder for video processing code
        # You can add your specific video processing logic here

if __name__ == "__main__":
    parser = ArgumentParser(description="Download or process a video.")
    parser.add_argument('--url', type=str, help="URL of the video to be downloaded.", default=None)
    parser.add_argument('--start_time', type=str, help="Start time for trimming the video (in format hh:mm:ss).", default=None)
    parser.add_argument('--end_time', type=str, help="End time for trimming the video (in format hh:mm:ss).", default=None)
    args = parser.parse_args()

    if args.url:
        # Download the video
        video_file = download_video(args.url)
        # If start and end times are provided, trim the video
        if args.start_time and args.end_time:
            trim_video(video_file, args.start_time, args.end_time)
    else:
        # Process local videos if no URL is provided
        process_local_videos()