from moviepy import VideoFileClip
import argparse,os

def time_str_to_seconds(time_str):
    if isinstance(time_str, (int, float)) or time_str is None:
        return time_str
    h, m, s = map(int, time_str.split(":"))
    return h * 3600 + m * 60 + s


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract mp3 from mp4 with optional trimming")
    parser.add_argument("input", help="Input MP4 file path")
    parser.add_argument("--output", default="",help="Output MP3 file path")
    parser.add_argument("--start", default="", help="Start time in hh:mm:ss (optional)")
    parser.add_argument("--end", default="", help="End time in hh:mm:ss (optional)")
    args = parser.parse_args()

    input_video_path = os.path.join("data",args.input) 
    output_audio_path = os.path.join("data",args.output) if args.output!= "" else os.path.join("data",args.input.split(".")[0]+".mp3")
    start_time = args.start
    end_time = args.end

    video_clip = VideoFileClip(input_video_path)

    start_sec = 0 if start_time == "" else time_str_to_seconds(start_time)
    end_sec = video_clip.duration if end_time == "" else time_str_to_seconds(end_time)

    if start_sec is not None or end_sec is not None:
        video_clip = video_clip.subclipped(start_sec, end_sec)

    video_clip.audio.write_audiofile(output_audio_path)
    video_clip.close()