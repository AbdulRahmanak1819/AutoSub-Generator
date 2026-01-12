# AutoSub Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Enabled-green)
![OpenAI Whisper](https://img.shields.io/badge/AI-OpenAI%20Whisper-orange)

**AutoSub Generator** is a Python automation tool that automatically transcribes and translates audio from any language into English subtitles using OpenAI's Whisper AI, embedding them directly into the video container.

---

## 🚀 Features

- **Audio Extraction:** Automatically strips audio from video files using FFmpeg.
- **AI Transcription:** Uses OpenAI's **Whisper** model to listen to audio in any language and generate accurate **English** subtitles.
- **Smart Formatting:** Converts raw timestamps into industry-standard SRT format.
- **Soft Subtitles:** Muxes subtitles into an MKV container instantly (no re-encoding required).

---

## 🛠️ Prerequisites

Before running the code, ensure you have the following installed:

1. **Python 3.8+**
2. **FFmpeg** (System-level installation required)
   - **Windows:** Download from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) and add to your System PATH.
   - **Mac:** `brew install ffmpeg`
   - **Linux:** `sudo apt install ffmpeg`

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/AbdulRahmanak1819/AutoSub-Generator.git](https://github.com/AbdulRahmanak1819/AutoSub-Generator.git)
   cd AutoSub-Generator
   ```

2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ How to Run

### Step 1: Prepare your Video
Place your video file in the project folder and rename it to **`input_video.mp4`**.

### Step 2: Extract Audio
Run the preprocessor to isolate the audio track for the AI.
```bash
python preprocess.py
```
*Output:* `extracted_audio.wav`

### Step 3: Transcribe & Generate Subtitles
Run the AI model. It will listen to the audio, translate it to English, and generate accurate timestamps.
```bash
python transcribe.py
```
*Output:* `subtitles.srt`

### Step 4: Merge Subtitles
Package the video and subtitles together into a final MKV file.
```bash
python merge_soft.py
```
*Output:* `final_output.mkv`

---

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `preprocess.py` | FFmpeg logic to strip audio from the video file. |
| `transcribe.py` | Whisper AI logic for transcription and SRT formatting. |
| `merge_soft.py` | FFmpeg logic to remux video and subtitles into a container. |
| `requirements.txt` | List of Python library dependencies. |
