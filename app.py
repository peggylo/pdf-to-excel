import pdfplumber
import pandas as pd

pdf_path = r"填入pdf路徑"
tables = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        for table in page.extract_tables():
            # 第一列當作表頭，剩下視為資料
            df = pd.DataFrame(table[1:], columns=table[0])
            tables.append(df)

if not tables:
    print("❌ 沒有偵測到任何表格，請確認 PDF 為可選取文字格式。")
    exit(1)

df_all = pd.concat(tables, ignore_index=True)
output_path = r"填入產出路徑"
df_all.to_excel(output_path, index=False)
print(f"✅ 已成功轉檔至：{output_path}")
