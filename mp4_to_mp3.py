from moviepy import VideoFileClip

# 指定你的 mp4 檔案路徑
input_video_path = "data//大數據專案小組第三十三次會議-20250717 0713-1.mp4"

# 產生 mp3 檔案的輸出路徑
output_audio_path = "data//大數據專案小組第三十三次會議-20250717 0713-1.mp3"

# 載入影片
video_clip = VideoFileClip(input_video_path)

# 提取音訊並寫入 mp3
video_clip.audio.write_audiofile(output_audio_path)

# 關閉資源
video_clip.close()