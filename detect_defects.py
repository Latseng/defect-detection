import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 重新建立模擬影像 (因為之前生成的檔案已清空)
image = np.full((300, 300, 3), 220, dtype=np.uint8)
for i in range(50, 300, 50):
    cv2.line(image, (i, 0), (i, 300), (180, 180, 180), 2)
    cv2.line(image, (0, i), (300, i), (180, 180, 180), 2)
np.random.seed(42)
for _ in range(8):
    x, y = np.random.randint(20, 280, 2)
    cv2.circle(image, (x, y), radius=5, color=(0, 0, 0), thickness=-1)
cv2.imwrite("sample.jpg", image)

# 灰階
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 定義 ROI 區域 (避免標題，僅檢測 y=50~300, x=0~300)
roi = gray[50:300, 0:300]

# 二值化只針對 ROI
_, binary = cv2.threshold(roi, 127, 255, cv2.THRESH_BINARY_INV)

# 找輪廓（瑕疵區域）
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 建立瑕疵清單，並把座標轉回全圖座標
defects = []
for i, cnt in enumerate(contours):
    x, y, w, h = cv2.boundingRect(cnt)
    defects.append({"id": i+1, "x": x, "y": y+50, "width": w, "height": h})

# 在原圖上標記瑕疵
output = image.copy()
for d in defects:
    cv2.rectangle(output, (d["x"], d["y"]), (d["x"]+d["width"], d["y"]+d["height"]), (0,0,255), 2)

# 儲存結果
cv2.imwrite("output_marked_roi.jpg", output)
pd.DataFrame(defects).to_csv("defects_roi.csv", index=False)

# 顯示結果
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title(f"Detected Defects in ROI: {len(defects)}")
plt.axis("off")
plt.show()
