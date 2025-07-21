# MP4 轉 MP3 擷取器

此 Python 腳本允許您從 MP4 視頻檔案中擷取音訊（MP3 格式），並可選擇透過指定開始與結束時間進行裁剪。

## 需求

- Python 3.x
- `moviepy` 函式庫

安裝所需的依賴套件：
```
pip install moviepy
```

## 使用方法

從命令列執行腳本：

```
python mp4_to_mp3.py <input_file> [--output <output_file>] [--start hh:mm:ss] [--end hh:mm:ss]
```

- `input`（必填）：輸入的 MP4 檔名，位於 `/data/` 目錄中。
- `--output`（選填）：輸出的 MP3 檔名。若未提供，預設為 `<input_file>.mp3`。
- `--start`（選填）：音訊剪輯的起始時間，格式為 `hh:mm:ss`。
- `--end`（選填）：音訊剪輯的結束時間，格式為 `hh:mm:ss`。

## 範例

擷取完整音訊：
```
python mp4_to_mp3.py example.mp4
```

擷取裁剪後的音訊：
```
python mp4_to_mp3.py example.mp4 --output output.mp3 --start 00:01:00 --end 00:02:30
```

## 注意事項

- 所有檔案應放置於 `/data/` 目錄中。
- 時間參數為選填，若未填寫，將擷取整段音訊。
- 輸出檔案將儲存在 `/data/` 目錄內。