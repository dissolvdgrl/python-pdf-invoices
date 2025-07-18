import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

def create_pdf(file_path, data_frame):
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    filename = Path(file_path).stem
    invoice_number,date = filename.split("-")
    header_cells = list(data_frame.columns)
    header_cells = [item.replace("_", " ").title() for item in header_cells]

    pdf.add_page()
    pdf.set_font("Courier", size=14, style="B")

    pdf.cell(w = 50, h = 8, txt = f"Invoice nr. {invoice_number}", ln=1)
    pdf.cell(w = 50, h = 8, txt = f"Invoice date: {date}", ln=1)

    # Table Header
    pdf.set_font("Courier", size=9, style="B")
    pdf.cell(w = 25, h = 8, txt = str(header_cells[0]), border=1)
    pdf.cell(w = 70, h = 8, txt = str(header_cells[1]), border=1)
    pdf.cell(w = 30, h = 8, txt = str(header_cells[2]), border=1)
    pdf.cell(w = 30, h = 8, txt = str(header_cells[3]), border=1)
    pdf.cell(w = 30, h = 8, txt = str(header_cells[4]), border=1, ln=1)

    for index, row in data_frame.iterrows():
        pdf.set_font("Courier", size=9, )
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w = 25, h = 8, txt = str(row["product_id"]), border=1)
        pdf.cell(w = 70, h = 8, txt = str(row["product_name"]), border=1)
        pdf.cell(w = 30, h = 8, txt = str(row["amount_purchased"]), border=1)
        pdf.cell(w = 30, h = 8, txt = str(row["price_per_unit"]), border=1)
        pdf.cell(w = 30, h = 8, txt = str(row["total_price"]), border=1, ln=1)

    pdf.output(f"PDFs/{filename}.pdf")

for filepath in filepaths:
    dataframe = pd.read_excel(filepath, sheet_name="Sheet 1")
    create_pdf(filepath, dataframe)



