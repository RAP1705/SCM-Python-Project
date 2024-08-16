from fpdf import FPDF
import pandas as pd


def generate_pdf(item_df: pd.DataFrame, total_amount: float, output_filename: str = 'delivery_note.pdf'):
    pdf = FPDF()
    pdf.add_page()

    pdf.image('logo.png', x=10, y=8, w=40)  # Adjust x, y, w (width), h (height) as needed
    pdf.set_xy(0, 30)  # Reset position after logo; adjust y coordinate based on logo size    

    # Set title
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Delivery Note", ln=True, align='C')

    # Calculate effective page width (EPW)
    epw = pdf.w - 2 * pdf.l_margin

    # Add table
    pdf.set_font("Arial", size=10)
    line_height = pdf.font_size * 2.5
    col_width = epw / 5  # distribute content evenly across 5 columns

    # Headers
    headers = ["Product ID", "Product Name", "Price", "Stock", "Subtotal"]
    for header in headers:
        pdf.cell(col_width, line_height, header, border=1)

    pdf.ln(line_height)

    # Data rows
    for row in item_df.itertuples():
        for item in row[1:]:
            pdf.cell(col_width, line_height, str(item), border=1)
        pdf.ln(line_height)

    # Add the subtotal at the end of the PDF
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Total Amount: ${total_amount:.2f}", ln=True, align='R')

    # Save PDF
    pdf.output(output_filename)
