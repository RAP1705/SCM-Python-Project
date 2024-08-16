import streamlit as st
import pandas as pd
from backend.dboperations import get_item_details
from helper_function.pdf_generator import generate_pdf
from helper_function.barcode_scanner import scan_barcode_opencv


# Title
st.title("SCM - Delivery Note Generation")

# Initialize session state to keep track of multiple inputs
if 'item_list' not in st.session_state:
    st.session_state['item_list'] = []

barcode = st.text_input("Input for Barcode", help="Enter the barcode for the product which will check in DB")

if st.button("Submit"):
    item_details = get_item_details(barcode)
    
    if item_details:
        st.session_state['item_list'].append(item_details)
    else:
        st.error("No product found for this barcode!")

st.write("------------------")
st.write("OR")

if st.button("Barcode Scan"):
    barcode = scan_barcode_opencv()
    item_details = get_item_details(barcode)
    
    if item_details:
        st.session_state['item_list'].append(item_details)
    else:
        st.error("No product found for this barcode!")    

st.write("------------------")            

# Convert the list of items to a DataFrame for better display
if st.session_state['item_list']:
    df = pd.DataFrame(st.session_state['item_list'], columns=["Product ID", "Product Name", "Price", "Stock"])
    
    # Calculate the subtotal
    df['Subtotal'] = df['Price'] * df['Stock']
    total_amount = df['Subtotal'].sum()
    
    # Display the table and subtotal
    st.table(df)
    st.write(f"**Total Amount: ${total_amount:.2f}**")

# Button to generate PDF
if st.button("Generate Delivery Note"):
    if st.session_state['item_list']:
        # Generate the PDF using the modularized function
        generate_pdf(df, total_amount)
        
        # Display download link
        st.success("PDF generated successfully!")
        with open('delivery_note.pdf', "rb") as f:
            st.download_button("Download Delivery Note", f, file_name='delivery_note.pdf')
    else:
        st.warning("No products added. Please add products before generating the delivery note.")
        
        

        
