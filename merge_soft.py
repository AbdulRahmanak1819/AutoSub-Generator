import ffmpeg
import os

def add_soft_subtitles(video_path, srt_path, output_path):
    if not os.path.exists(video_path):
        print("Video file not found.")
        return
    if not os.path.exists(srt_path):
        print("SRT file not found.")
        return

    input_video = ffmpeg.input(video_path)
    input_srt = ffmpeg.input(srt_path)

    print(f"Packaging video + subtitles into '{output_path}'...")

    stream = ffmpeg.output(
        input_video, 
        input_srt, 
        output_path, 
        **{'c': 'copy', 'c:s': 'srt', 'metadata:s:s:0': 'language=eng'}
    )

    ffmpeg.run(stream, overwrite_output=True)
    print(f"Output saved to: {output_path}")

if __name__ == "__main__":

    video_file = "test_video.mp4" 
    srt_file = "subtitles.srt"
    output_file = "final_output.mkv"

    add_soft_subtitles(video_file, srt_file, output_file)
