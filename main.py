import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")


def create_pdf(file_path):
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    filename = Path(file_path).stem
    invoice_number = filename.split("-")[0]
    invoice_date = filename.split("-")[1]

    pdf.add_page()
    pdf.set_font("Courier", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_number}")
    pdf.output(f"PDFs/{filename}.pdf")

for filepath in filepaths:
    data_frame = pd.read_excel(filepath, sheet_name="Sheet 1")
    create_pdf(filepath)



