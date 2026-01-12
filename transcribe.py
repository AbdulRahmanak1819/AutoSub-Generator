import whisper
import warnings
import os
from datetime import timedelta

warnings.filterwarnings("ignore")

def format_timestamp(seconds):
    """
    Converts seconds (e.g., 3.36) to SRT format (00:00:03,360).
    """
    td = timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    microseconds = td.microseconds

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    millis = microseconds // 1000

    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

def run_ai_transcription(audio_path, model_type="base"):
    if not os.path.exists(audio_path):
        print(f"Error: Audio file not found at {audio_path}")
        return

    print(f"Loading Whisper AI model ('{model_type}')...")
    model = whisper.load_model(model_type)

    print(f"Listening to audio...")
    result = model.transcribe(audio_path, task="translate")

    # --- Saving the SRT File ---
    srt_filename = "subtitles.srt"
    print(f"Saving subtitles to '{srt_filename}'...")
    
    with open(srt_filename, "w", encoding="utf-8") as srt_file:

        for index, segment in enumerate(result["segments"], start=1):
            
            start = format_timestamp(segment["start"])
            end = format_timestamp(segment["end"])
            text = segment["text"].strip()

            srt_file.write(f"{index}\n")
            srt_file.write(f"{start} --> {end}\n")
            srt_file.write(f"{text}\n")
            srt_file.write("\n")
            
    print(f"Subtitles saved.")

if __name__ == "__main__":
    audio_file = "extracted_audio.wav" 
    run_ai_transcription(audio_file)
