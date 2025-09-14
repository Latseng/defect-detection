# AOI Defect Detection Demo

## 目的
運用 Python (OpenCV + pandas) 進行簡易 AOI 影像檢測，模擬檢測表面瑕疵並輸出統計報表。

## 執行步驟
1. 讀取影像檔案（灰階）
2. 二值化處理，檢測黑點/瑕疵
3. 標記瑕疵區域，輸出結果影像與 CSV 報表

## 輸出範例
- output_marked.jpg: 帶紅框的瑕疵影像
- defects.csv: 瑕疵清單與座標