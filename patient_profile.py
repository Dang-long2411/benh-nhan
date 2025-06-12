import pandas as pd
import json

df = pd.read_excel(r"C:\Users\DELL\Desktop\benh_nhan.xlsx")
df = df.astype(str)
patients = df.to_dict(orient="records")

html_template = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Hồ sơ bệnh nhân</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'Roboto', sans-serif;
            background: linear-gradient(to right, #e0f7fa, #e0f2f1);
            margin: 0;
            padding: 40px 0;
        }}
        .card {{
            background: white;
            max-width: 600px;
            margin: auto;
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }}
        .card:hover {{
            transform: scale(1.01);
        }}
        h2 {{
            color: #00796b;
            border-bottom: 1px solid #ddd;
            padding-bottom: 10px;
        }}
        p {{
            margin: 12px 0;
            font-size: 16px;
            line-height: 1.5;
        }}
        strong {{
            color: #333;
        }}
        .nav {{
            text-align: center;
            margin-top: 30px;
        }}
        button {{
            background-color: #009688;
            color: white;
            border: none;
            padding: 10px 18px;
            margin: 0 12px;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s;
        }}
        button:hover {{
            background-color: #00796b;
        }}
    </style>
</head>
<body>
    <div class="card" id="profileCard">
        <h2 id="hoTen">Họ tên bệnh nhân</h2>
        <p><strong>Ngày sinh:</strong> <span id="ngaySinh"></span></p>
        <p><strong>CCCD:</strong> <span id="Cccd"></span></p>
        <p><strong>Tiền sử:</strong> <span id="tienSu"></span></p>
        <p><strong>Thuốc:</strong> <span id="Thuoc"></span></p>
    </div>
    <div class="nav">
        <button onclick="prevPatient()">← Trước</button>
        <button onclick="nextPatient()">Sau →</button>
    </div>

    <script>
        const patients = {json.dumps(patients, ensure_ascii=False)};
        let index = 0;

        function showPatient(i) {{
            const p = patients[i];
            document.getElementById('hoTen').textContent = p.ho_ten || 'Không có';
            document.getElementById('ngaySinh').textContent = p.ngay_sinh || '';
            document.getElementById('Cccd').textContent = p.cccd || '';
            document.getElementById('tienSu').textContent = p.tien_su || '';
            document.getElementById('Thuoc').textContent = p.thuoc || '';
        }}

        function prevPatient() {{
            index = (index - 1 + patients.length) % patients.length;
            showPatient(index);
        }}

        function nextPatient() {{
            index = (index + 1) % patients.length;
            showPatient(index);
        }}

        showPatient(index);
    </script>
</body>
</html>
"""

OUTPUT_FILE = "C:/Users/DELL/Desktop/patient_profile.html"
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_template)

print("✅ Đã tạo file HTML đẹp:", OUTPUT_FILE)

