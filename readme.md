# MP4 to MP3 Audio Extractor 🎞️

這個簡單的 Python 腳本可將指定的 `.mp4` 影片檔案轉換為 `.mp3` 音訊檔案。非常適合從會議記錄、演講、線上教學影片中提取純音訊內容。

## 功能說明 🧾

- 讀取本地的 MP4 檔案
- 使用 `moviepy` 套件提取音訊
- 將音訊儲存為 MP3 格式
- 自動關閉影片資源以節省記憶體

## 環境需求 📦

請先安裝以下 Python 套件：

```bash
pip install moviepy
```

※ 若是初次使用 `moviepy`，它可能還會安裝 `ffmpeg`，並自動下載必要的執行檔。

## 檔案結構 📂

```
project-folder/
│
├── data/
│   ├── Filename.mp4  ← 輸入檔案
│   └── Filename.mp3  ← 輸出檔案
│
├── mp4_to_mp3.py  ← 主程式
└── readme.md
```

## 使用方法 🧑‍💻

在 `mp4_to_mp3.py` 中指定要轉換的 MP4 檔案：

```python
input_video_path = "data//Filename.mp4"
output_audio_path = "data//Filename.mp3"
```

然後執行：

```bash
python mp4_to_mp3.py
```

轉換完成後，MP3 音訊檔案將會輸出到你指定的路徑。

## 注意事項 🛑

- 檔案路徑需使用英文，避免因中文造成編碼錯誤。
- 若遇到 `ffmpeg` 無法找到的錯誤，可參考 moviepy 文件手動安裝。
- 建議使用 Python 3.7 以上版本以確保相容性。

## 參考資源 📘

- [moviepy 官方文件](https://zulko.github.io/moviepy/)
- [FFmpeg 官方網站](https://ffmpeg.org/)
