import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. 讀取圖片
image = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)

# 2. 二值化（簡單 threshold）
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

# 3. 找輪廓（瑕疵區域）
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 建立瑕疵清單
defects = []
for i, cnt in enumerate(contours):
    x, y, w, h = cv2.boundingRect(cnt)
    defects.append({"id": i+1, "x": x, "y": y, "width": w, "height": h})

# 4. 在原圖上標記瑕疵
output = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
for d in defects:
    cv2.rectangle(output, (d["x"], d["y"]), (d["x"]+d["width"], d["y"]+d["height"]), (0,0,255), 2)

# 5. 儲存結果
cv2.imwrite("output_marked.jpg", output)
pd.DataFrame(defects).to_csv("defects.csv", index=False)

# 6. 顯示結果
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title(f"Detected Defects: {len(defects)}")
plt.show()