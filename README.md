# Audio Transcription Application - Powered by Faster Whisper

This application provides a user-friendly, PyQt5-based Graphical User Interface (GUI) for transcribing audio files with high accuracy and efficiency, leveraging the Faster Whisper model.

## Overview

The Audio Transcription Application simplifies the process of converting speech to text, offering robust features and flexible configuration options suitable for a wide range of audio transcription needs.

## Key Features

* **Multi-Language Transcription:** Transcribe audio in numerous languages, with automatic language detection available.
* **Flexible Model Selection:** Choose from various Faster Whisper model sizes (tiny, base, small, medium, large-v2, large-v3) to balance accuracy and processing speed.
* **Hardware Acceleration:** Utilize CPU or GPU (CUDA) for accelerated transcription, significantly reducing processing time.
* **Result Persistence:** Save transcription results to easily accessible text files.
* **Real-time Progress Monitoring:** Track the transcription progress with live updates within the GUI.
* **User-Friendly Interface:** Intuitive design for seamless navigation and operation.

## System Requirements

To ensure optimal performance, the following system requirements must be met:

* **Operating System:** Windows, macOS, or Linux (tested primarily on Windows).
* **Python:** Python 3.10 is required within your virtual environment.
* **CUDA (for GPU Acceleration):** CUDA version 9.0 is required for GPU acceleration.
* **cuDNN (for GPU Acceleration):** cuDNN version 11.8 is required for GPU acceleration.
* **Anaconda:** Recommended for environment management.
* **Temporary Directory:** A temporary directory such as "C:\temp" is required for the installation process.

## Installation Guide

This application is designed to be installed and run within an Anaconda environment. Follow these steps for a successful setup:
You can directly run the ```Transcribe MyApp.bat``` file or go with the manual step:
1.  **Install Anaconda:** Ensure Anaconda is installed on your system.
2.  **Open Anaconda Prompt:** Launch the Anaconda Prompt.
3.  **Create a Virtual Environment:** (Recommended) Create a dedicated virtual environment to avoid dependency conflicts:

    ```bash
    conda create -n fasterWhisper python=3.10 -y
    conda activate fasterWhisper
    ```

4.  **Create Temporary Directory:** Create a temporary directory at `C:\temp`
5.  **Clone Faster Whisper Repository:** Clone the Faster Whisper repository into the `C:\temp` directory.

    ```bash
    git clone https://github.com/SYSTRAN/faster-whisper.git
    ```

6.  **Install Dependencies:** Navigate to the cloned repository and install the required packages:

    ```bash
    cd C:\temp\faster-whisper
    conda install --file requirements.txt
    ```

7.  **Install Faster Whisper:** Install the Faster Whisper package.

    ```bash
    conda install faster-whisper
    ```
8.  **Install PyQt5:** Install the PyQt5 library for the GUI.

    ```bash
    pip install PyQt5
    ```

## Usage Instructions

1.  **Run the Application:** Execute the application script:

    ```bash
    python audio_transcription_app.py
    ```

2.  **Select Audio File:** Click the "Browse" button to choose an audio file (supported formats: mp3, wav, m4a, flac).
3.  **Configure Transcription Settings:**
    * **Model Size:** Select the desired Faster Whisper model size.
    * **Language:** Choose the audio language or "auto" for automatic detection.
    * **Device:** Select "CPU" or "GPU (CUDA)" for processing.
4.  **Start Transcription:** Click "Transcribe Audio" to initiate the transcription process.
5.  **Save Results:** Once completed, click "Save Transcription" to save the results to a text file.

## Model Size Recommendations

* **tiny:** Fastest, minimal resource usage, lowest accuracy.
* **base:** Fast, reasonable accuracy for simpler audio.
* **small:** Good balance of speed and accuracy for general use.
* **medium:** Higher accuracy, moderate resource usage.
* **large-v2/v3:** Highest accuracy, significant resource usage, recommended for complex audio.

## Language Support

The application supports a wide range of languages, including but not limited to: English, Japanese, Chinese, German, Spanish, Russian, Korean, French, Italian, Portuguese, Turkish, Polish, Catalan, Dutch, Arabic, Swedish, Czech, Finnish, and Ukrainian.

## Important Notes

* GPU acceleration requires a properly configured CUDA and cuDNN environment.
* Large audio files and larger model sizes will require more processing time and memory.
* The application displays the detected language and confidence level during transcription.
* This application's performance is optimized for specific system specifications. Performance may vary on different systems.
* With a compatible GPU, the application can provide rapid transcription, potentially processing a 5-minute audio file within seconds.

## Further Information

If you face any trouble to install faster-wispher you can refer to the following resource:

* [YouTube Video](https://youtu.be/Kyc0AgMIBSU?si=5Di7bfHi_lHePeLy)
* ![image](https://github.com/user-attachments/assets/cb9a4192-0201-48ae-b0de-e1701efd9fc2)


## Screenshots

![image](https://github.com/user-attachments/assets/cb123d43-cc20-4914-8605-38795ae65f37)


**Disclaimer:** This application is tailored to the developer's system specifications. Performance may vary on different hardware configurations.
