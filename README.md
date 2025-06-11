# Cathay Cube Selenium 自動化腳本

## 簡介
本專案使用 Python Selenium 實現自動化流程，包含：
- 自動下載並啟動 ChromeDriver
- 進入國泰 Cube 網站
- 等待指定元素顯性載入後截圖
- 點擊選單、展開「停發卡」區塊並逐一點擊分頁截圖
- 跳轉申辦頁面並切換分頁
- 擷取卡片列表並截圖保存

此流程可用於自動化測試、資料擷取與頁面快照。

## 環境需求

- Python 3.9+
- Google Chrome 瀏覽器（建議最新版）
- ChromeDriver（由 `webdriver_manager` 自動管理）
- Python 套件：
  - selenium
  - webdriver_manager

## 安裝 & 執行

1. 建議使用虛擬環境：
   ```bash
   python3 -m venv env
   source env/bin/activate   


2. 下載需要套件：
   ```bash
   pip3 install -r requirements.txt

3. 執行：
   ```bash
   python3 main.py


## 輸出說明

1. home.png：首頁截圖
2. stopcard_screenshots/：停發卡每一頁的截圖
3. card_screenshots/：分類卡片每張的截圖

logic.py 為程式邏輯作業答案