
# Whisper and Expert Coding Comparison

## Project Overview

This project explores the use of OpenAI’s **Whisper** automatic speech recognition (ASR) system to transcribe naturalistic, daylong audio recordings collected in infant home environments. Transcription of children's language is a widely used method in developmental and cognitive psychology, but manual transcription is time consuming and effortful, especially for long and noisy recordings.

By comparing Whisper’s transcriptions to expert human transcriptions, this project aims to evaluate the accuracy and efficiency of automated transcription methods for use in developmental research.


---
## Installation
```bash
# Install the required dependencies 
pip install -r requirements.txt

# Run the test file
pytest tests/
```
---
## Code Structure
- `test/` - contains three unit tests.
    - `test.py` – Simple test file for testing Whisper accuracy.
- `requirements.txt` – Python dependencies needed to run the project.
- `analysis.py` – Main script for comparing Whisper and expert transcriptions.
- `clean_files.py` - script that will clean csv files with blanks or non-utterance conts.
- `whisper_transcription.py` - script that will process audio files through Whisper to output a transcribed csv file.
---
## Folder Structure Requirements
To run the scripts, you will need to make sure your directory is organized like this:
whisper-project/
├── audio/                           
├── transcripts/
│   ├── whisper_transcripts/        
│   └── expert_transcripts/ 
│       └── cleaned/        
├── cleaned_individual/                           
├── scripts/
│   ├── analysis.py
│   ├── clean_files.py
│   └── whisper_transcription_process.py
├── tests/
│   └── test.py   
Subfolders like cleaned_individual/ and cleaned/ will be automatically created by the scripts.        

---
## References 
Sun, A., Londono, J. J., Elbaum, B., Estrada, L., Lazo, R. J., Vitale, L., ... & Messinger, D. S. (2024, May). Who said what? an automated approach to analyzing speech in preschool classrooms. In 2024 IEEE International Conference on Development and Learning (ICDL) (pp. 1-8). IEEE.


 
