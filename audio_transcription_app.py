import os
import sys
import time
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, 
                            QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, 
                            QComboBox, QTextEdit, QProgressBar, QMessageBox,
                            QGroupBox, QRadioButton, QButtonGroup)
from PyQt5.QtGui import QClipboard
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from faster_whisper import WhisperModel

class TranscriptionThread(QThread):
    progress_update = pyqtSignal(str)
    transcription_complete = pyqtSignal(str, float)
    
    def __init__(self, audio_path, model_size, language, device, compute_type):
        super().__init__()
        self.audio_path = audio_path
        self.model_size = model_size
        self.language = language if language != "auto" else None
        self.device = device
        self.compute_type = compute_type
        
    def run(self):
        try:
            self.progress_update.emit("Loading model...")
            model = WhisperModel(self.model_size, device=self.device, compute_type=self.compute_type)
            
            self.progress_update.emit("Transcribing audio...")
            segments, info = model.transcribe(
                self.audio_path, 
                beam_size=5,
                language=self.language
            )
            
            self.progress_update.emit(f"Detected language: {info.language} (confidence: {info.language_probability:.2f})")
            
            # Collect all segments
            full_text = ""
            segments_list = list(segments)  # Convert generator to list
            
            for i, segment in enumerate(segments_list):
                full_text += segment.text + " "
                progress = (i + 1) / len(segments_list) * 100
                self.progress_update.emit(f"Processing segment {i+1}/{len(segments_list)}")
            
            self.transcription_complete.emit(full_text, info.language_probability)
            
        except Exception as e:
            self.progress_update.emit(f"Error: {str(e)}")

class AudioTranscriptionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Audio Transcription App")
        self.setGeometry(100, 100, 800, 600)
        
        # Main layout
        main_layout = QVBoxLayout()
        
        # File selection section
        file_group = QGroupBox("Audio File")
        file_layout = QHBoxLayout()
        
        self.file_path_label = QLabel("No file selected")
        self.file_path_label.setWordWrap(True)
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_file)
        
        file_layout.addWidget(self.file_path_label)
        file_layout.addWidget(self.browse_button)
        file_group.setLayout(file_layout)
        
        # Model settings section
        model_group = QGroupBox("Model Settings")
        model_layout = QVBoxLayout()
        
        # Model size selection
        model_size_layout = QHBoxLayout()
        model_size_layout.addWidget(QLabel("Model Size:"))
        self.model_size_combo = QComboBox()
        self.model_size_combo.addItems(["tiny", "base", "small", "medium", "large-v2", "large-v3"])
        self.model_size_combo.setCurrentText("small")
        model_size_layout.addWidget(self.model_size_combo)
        
        # Language selection
        language_layout = QHBoxLayout()
        language_layout.addWidget(QLabel("Language:"))
        self.language_combo = QComboBox()
        self.language_combo.addItems(["auto", "en", "ja", "zh", "de", "es", "ru", "ko", "fr", "it", "pt", "tr", "pl", "ca", "nl", "ar", "sv", "cs", "fi", "uk"])
        language_layout.addWidget(self.language_combo)
        
        # Device selection
        device_layout = QHBoxLayout()
        device_layout.addWidget(QLabel("Device:"))
        self.device_group = QButtonGroup()
        self.cpu_radio = QRadioButton("CPU")
        self.gpu_radio = QRadioButton("GPU (CUDA)")
        self.device_group.addButton(self.cpu_radio)
        self.device_group.addButton(self.gpu_radio)
        self.cpu_radio.setChecked(True)
        device_layout.addWidget(self.cpu_radio)
        device_layout.addWidget(self.gpu_radio)
        
        model_layout.addLayout(model_size_layout)
        model_layout.addLayout(language_layout)
        model_layout.addLayout(device_layout)
        model_group.setLayout(model_layout)
        
        # Transcription button
        self.transcribe_button = QPushButton("Transcribe Audio")
        self.transcribe_button.clicked.connect(self.transcribe_audio)
        self.transcribe_button.setEnabled(False)
        
        # Progress section
        progress_group = QGroupBox("Progress")
        progress_layout = QVBoxLayout()
        self.status_label = QLabel("Ready")
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.setVisible(False)
        
        progress_layout.addWidget(self.status_label)
        progress_layout.addWidget(self.progress_bar)
        progress_group.setLayout(progress_layout)
        
        # Results section
        results_group = QGroupBox("Transcription Results")
        results_layout = QVBoxLayout()
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        
        # Add Copy button
        self.copy_button = QPushButton("Copy Transcription")
        self.copy_button.clicked.connect(self.copy_transcription)
        self.copy_button.setEnabled(False)  # Initially disabled until transcription is complete
        
        results_layout.addWidget(self.results_text)
        results_layout.addWidget(self.copy_button)
        results_group.setLayout(results_layout)
        
        # Add all sections to main layout
        main_layout.addWidget(file_group)
        main_layout.addWidget(model_group)
        main_layout.addWidget(self.transcribe_button)
        main_layout.addWidget(progress_group)
        main_layout.addWidget(results_group)
        
        # Set central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Audio File", "", "Audio Files (*.mp3 *.wav *.m4a *.flac);;All Files (*)"
        )
        
        if file_path:
            self.file_path_label.setText(file_path)
            self.transcribe_button.setEnabled(True)
    
    def transcribe_audio(self):
        if not os.path.exists(self.file_path_label.text()):
            QMessageBox.warning(self, "Error", "Please select a valid audio file.")
            return
        
        # Get settings
        model_size = self.model_size_combo.currentText()
        language = self.language_combo.currentText()
        device = "cuda" if self.gpu_radio.isChecked() else "cpu"
        compute_type = "float16" if device == "cuda" else "float32"
        
        # Update UI
        self.transcribe_button.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.results_text.clear()
        self.status_label.setText("Starting transcription...")
        
        # Start transcription in a separate thread
        self.transcription_thread = TranscriptionThread(
            self.file_path_label.text(),
            model_size,
            language,
            device,
            compute_type
        )
        
        self.transcription_thread.progress_update.connect(self.update_progress)
        self.transcription_thread.transcription_complete.connect(self.display_results)
        self.transcription_thread.start()
    
    def update_progress(self, message):
        self.status_label.setText(message)
    
    def display_results(self, text, confidence):
        self.progress_bar.setVisible(False)
        self.transcribe_button.setEnabled(True)
        self.results_text.setText(text)
        self.status_label.setText("Transcription complete!")
        
        # Enable save option
        save_button = QPushButton("Save Transcription")
        save_button.clicked.connect(lambda: self.save_transcription(text))
        
        # Enable Copy button
        self.copy_button.setEnabled(True)

        # Find the results layout and add the save button
        results_group = self.findChild(QGroupBox, "")
        if results_group and results_group.title() == "Transcription Results":
            results_group.layout().addWidget(save_button)
    
    def save_transcription(self, text):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Transcription", "", "Text Files (*.txt);;All Files (*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                QMessageBox.information(self, "Success", "Transcription saved successfully!")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to save file: {str(e)}")

    def copy_transcription(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.results_text.toPlainText())
        QMessageBox.information(self, "Copied", "Transcription copied to clipboard!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioTranscriptionApp()
    window.show()
    sys.exit(app.exec_()) 