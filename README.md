# project_1
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
python test.py
```
---
## Code Structure

- `test/` - contains files for running a demo
    - `test_clip_tracript.txt`- sample human trascript that corresponds to the test clip audio.
    - `test_clip.wav` - sample audio clip that can be used for the test
    - `test.py` – Simple test file for testing Whisper transcription and word counts.
- `requirements.txt` – Python dependencies needed to run the project.
- `transcribe_compare.py` – Main script for comparing Whisper and expert transcriptions.

---
## References 
Sun, A., Londono, J. J., Elbaum, B., Estrada, L., Lazo, R. J., Vitale, L., ... & Messinger, D. S. (2024, May). Who said what? an automated approach to analyzing speech in preschool classrooms. In 2024 IEEE International Conference on Development and Learning (ICDL) (pp. 1-8). IEEE.


 
