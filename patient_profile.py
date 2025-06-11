import pandas as pd
import os
import re
from jinja2 import Template

# === File Excel đầu vào ===
INPUT_FILE = r'C:\Users\DELL\Desktop\benh_nhan.xlsx' 
OUTPUT_FOLDER = 'output_html'

# === Mẫu HTML đơn giản ===
html_template = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Lý lịch bệnh nhân</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f1f5f9; padding: 30px; }
        .card { background: #fff; padding: 25px; border-radius: 12px; max-width: 600px; margin: auto; box-shadow: 0 4px 8px rgba(0,0,0,0.1);}
        h1 { text-align: center; color: #1e293b; }
        .field { margin: 12px 0; }
        .label { font-weight: bold; color: #334155; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Lý Lịch Bệnh Nhân</h1>
        <div class="field"><span class="label">Họ tên:</span> {{ ho_ten }}</div>
        <div class="field"><span class="label">Ngày sinh:</span> {{ ngay_sinh }}</div>
        <div class="field"><span class="label">CCCD:</span> {{ cccd }}</div>
        <div class="field"><span class="label">Tiền sử bệnh:</span> {{ tien_su }}</div>
        <div class="field"><span class="label">Thuốc:</span> {{ thuoc }}</div>
    </div>
</body>
</html>
"""

# === Hàm tạo tên file từ họ tên ===
def to_filename(name):
    name = name.lower()
    name = re.sub(r'[^\w\s-]', '', name)
    return '-'.join(name.strip().split())

# === Đọc file Excel ===
df = pd.read_excel(INPUT_FILE)

# === Tạo thư mục chứa HTML ===
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# === Biên dịch mẫu HTML ===
template = Template(html_template)

# === Tạo HTML cho từng bệnh nhân ===
for _, row in df.iterrows():
    file_name = to_filename(row["ho_ten"]) + ".html"
    html_content = template.render(
        ho_ten=row["ho_ten"],
        ngay_sinh=row["ngay_sinh"],
        cccd=row["cccd"],
        tien_su=row["tien_su"],
        thuoc=row["thuoc"]
    )
    with open(os.path.join(OUTPUT_FOLDER, file_name), "w", encoding="utf-8") as f:
        f.write(html_content)

print(f"✅ Đã tạo {len(df)} trang HTML trong thư mục '{OUTPUT_FOLDER}'")
