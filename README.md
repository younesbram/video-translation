# Video-Translation

A tool for translating video audio, including audio transcription, translation, natural voice cloning, and lip-syncing!

Please bewary of ethical boundaries and it is up to the end user to be adamant and dilligent to use this only with permission of video owners

This is a paid feauture in many websites such as HeyGen. I wanted my video of L'inspecteur Taher et L'apprenti to be translated to English but they queued me up behind 5000 users, so I reverse engineered the product/feauture.

Hooray to open source.

## Features
- Extract and download video locally with yt-dlp
- Extract audio from video using `ffmpeg`.
- Transcribe audio to text with `whisper` . *Currently on V3, up to 53 languages transcribable!
- Translate text to target language using GPT-4. *Currently on GPT4, up to 95+ natural languages with complex semantic understanding. Might move to a fine-tuned LLM or NLLB/SeamlessM4T from Meta AI for 200+ languages.
- Use ElevenLabs API for voice synthesis.
- Lip-sync the voice-cloned translated audio using Wav2Lip.
- Dubbed video achieved!

## Prerequisites
- ffmpeg
- whisper
- GPT-4 API access
- ElevenLabs API access
- Wav2Lip

## Usage

1. Clone the repository.
2. Install required dependencies.
3. Run `video_processor.py` with the video file as input.

## Batch Processing

Use `batch_process.sh` for processing multiple languages.

## Contribution

Feel free to contribute to the project by submitting pull requests or issues.

## License

Standard Ethics.
