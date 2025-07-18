import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

def create_pdf(file_path):
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    filename = Path(file_path).stem
    invoice_number,date = filename.split("-")

    pdf.add_page()
    pdf.set_font("Courier", size=14, style="B")

    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_number}", ln=True)
    pdf.cell(w=50, h=8, txt=f"Invoice date: {date}")

    pdf.output(f"PDFs/{filename}.pdf")

for filepath in filepaths:
    data_frame = pd.read_excel(filepath, sheet_name="Sheet 1")
    create_pdf(filepath)



