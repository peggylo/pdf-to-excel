# PDF to Excel 轉換工具

## 中文說明

這是一個簡單的 PDF 表格轉 Excel 工具，可以從 PDF 文件中提取表格數據並保存為 Excel 格式。

### 功能特點

- 自動識別 PDF 中的表格
- 提取表格數據並保存為 Excel 文件
- 簡單易用，只需修改輸入輸出路徑

### 使用方法

1. 安裝所需依賴包：
   ```
   pip install pdfplumber pandas openpyxl
   ```

2. 在 `app.py` 中修改以下內容：
   - `pdf_path`：要處理的 PDF 文件路徑
   - `output_path`：輸出的 Excel 文件路徑

3. 執行腳本：
   ```
   python app.py
   ```

### 注意事項

**重要提醒**：此工具僅適用於包含可選取文字的 PDF 文件，不支援掃描的圖片型 PDF 文件。如果是掃描文檔，需要先進行 OCR 處理轉換為文本型 PDF。

## English Description

# PDF to Excel Converter

A simple tool to extract tables from PDF files and save them as Excel format.

### Features

- Automatically detects tables in PDF files
- Extracts table data and saves to Excel format
- Easy to use, just modify input and output paths

### How to Use

1. Install required packages:
   ```
   pip install pdfplumber pandas openpyxl
   ```

2. Modify the following in `app.py`:
   - `pdf_path`: Path to the PDF file you want to process
   - `output_path`: Path where the Excel file will be saved

3. Run the script:
   ```
   python app.py
   ```

### Important Note

**Warning**: This tool only works with PDF files containing selectable text. It does not support scanned image-based PDF files. For scanned documents, OCR processing is required first to convert them to text-based PDFs. 
