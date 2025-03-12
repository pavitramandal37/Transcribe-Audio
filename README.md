# Audio Transcription App

A PyQt5-based GUI application for transcribing audio files using the Faster Whisper model.

## Features

- Transcribe audio files in multiple languages
- Support for various model sizes (tiny, base, small, medium, large-v2, large-v3)
- Option to use CPU or GPU (CUDA) for processing
- Save transcription results to text files
- Real-time progress updates

## Requirements

This application requires the following Python packages:
- PyQt5
- faster-whisper

## Installation

This application is designed to run in an Anaconda environment with the required packages installed.

1. Make sure you have Anaconda installed
2. Open Anaconda Prompt
3. Create a new environment (optional):
   ```
   conda create -n fasterWhisper python=3.9
   conda activate fasterWhisper
   ```
4. Install the required packages:
   ```
   pip install PyQt5
   pip install faster-whisper
   ```

## Usage

1. Run the application:
   ```
   python audio_transcription_app.py
   ```

2. Click the "Browse" button to select an audio file (supported formats: mp3, wav, m4a, flac)

3. Configure the transcription settings:
   - Model Size: Select the model size based on your needs (larger models are more accurate but slower)
   - Language: Choose the language of the audio or select "auto" for automatic detection
   - Device: Select CPU or GPU (CUDA) for processing

4. Click the "Transcribe Audio" button to start the transcription process

5. Once the transcription is complete, you can save the results by clicking the "Save Transcription" button

## Model Size Recommendations

- **tiny**: Fastest, lowest accuracy, minimal resource usage
- **base**: Fast with reasonable accuracy for simple audio
- **small**: Good balance between speed and accuracy for general use
- **medium**: Higher accuracy, moderate resource usage
- **large-v2/v3**: Highest accuracy, significant resource usage, recommended for complex audio or challenging accents

## Language Support

The application supports multiple languages including English, Japanese, Chinese, German, Spanish, Russian, Korean, French, Italian, Portuguese, Turkish, Polish, Catalan, Dutch, Arabic, Swedish, Czech, Finnish, and Ukrainian.

## Notes

- GPU acceleration requires CUDA to be properly installed on your system
- For large audio files, using a larger model size may require significant processing time and memory
- The application will display the detected language and confidence level during transcription 