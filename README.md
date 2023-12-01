# Video-Dubbing

A tool for translating video audio, including audio transcription, translation, natural voice cloning, and lip-syncing!

Please bewary of ethical boundaries and it is up to the end user to be adamant and dilligent to use this only with permission of video owners

This is a paid feauture in many websites such as HeyGen. I wanted my video to be translated to English but they queued me up behind 5000 users, so I reverse engineered the product/feauture.

Hooray to open source.

## Features
- Extract and download video locally with `yt-dlp`.
- Extract audio from video using `ffmpeg`.
- Transcribe audio to text with `whisper` . *Currently on V3, up to 53 languages transcribable!
- Translate text to target language using GPT-4. *Currently on GPT4, up to 95+ natural languages with complex semantic understanding. Might move to a fine-tuned LLM or [NLLB/SeamlessM4T](#links) from Meta AI for 200+ languages.

- Note: Currently, using seamless for the voice synthesizing + translation all in one. Nov 30, 2023.
  
- Use ElevenLabs API / TorToiSe for voice synthesis.
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
```
!pip install --quiet git+https://github.com/huggingface/transformers sentencepiece
```
3. Run `video_processor.py` with the video file and target language as input.

## Batch Processing

Use `batch_process.sh` for dubbing same video to multiple languages.

## Contribution

Feel free to contribute to the project by forking this repo and submitting pull requests.

## Diagram
![Mermaid Diagram of Program Logic](https://github.com/younesbram/video-translation/blob/main/for_valued_homie.png "Diagram")


## Links

- NLLB: <https://github.com/facebookresearch/fairseq/tree/nllb>
- Open-NLLB repository: <https://github.com/gordicaleksa/Open-NLLB>
- SeamlessM4T: <https://example-seamlessm4t-link.com>
- TorToiSe: <https://github.com/neonbjb/tortoise-tts>
- ElevenLabs: <https://elevenlabs.io/docs/api-reference/text-to-speech>
- Wav2Lip: <https://github.com/Rudrabha/Wav2Lip>
- Whisper: <https://platform.openai.com/docs/guides/speech-to-text>
- GPT4: <https://openai.com/research/gpt-4>



## Alternatives
Rask.ai
HeyGen video translate
? Feel free to add more.

## License

Standard Ethics.
