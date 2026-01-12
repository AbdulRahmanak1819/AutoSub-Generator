import ffmpeg
import os

def extract_audio(video_path, audio_output_path):
    """
    Extracts audio from a video file and optimizes it for AI processing.
    Specs: 16kHz sampling rate, Mono audio channel.
    """
    try:
        if not os.path.exists(video_path):
            print(f"Error: Video file not found at {video_path}")
            return

        print(f"Processing: {video_path}...")

        stream = ffmpeg.input(video_path)
        stream = ffmpeg.output(stream, audio_output_path, ar='16000', ac='1')
        
        ffmpeg.run(stream, overwrite_output=True)

        print(f"Success! Audio saved to: {audio_output_path}")

    except ffmpeg.Error as e:
        print("FFmpeg Error occurred:")
        print(e.stderr.decode('utf8')) #stderr -> standard error

# --- TEST AREA ---
if __name__ == "__main__":

    input_video = "input_video.mp4" 
    
    output_audio = "extracted_audio.wav"

    extract_audio(input_video, output_audio)
