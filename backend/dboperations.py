   
# import psycopg2
# import os
# from dotenv import load_dotenv
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart


# # Load .env file
# load_dotenv('./.env')

# # Print all environment variables (for debugging)
# print("Environment Variables:", os.environ)


# dbname = os.environ.get("dbname", "SCMBATCH3")
# user = os.environ.get("user", "postgres")
# password = os.environ.get("password", "Just4fun_135")
# host = os.environ.get("host", "localhost")
# port = os.environ.get("port", "5434")

# # Email credentials and settings
# email_user = os.environ.get("email_user", "planas.raul@gmail.com")
# email_password = os.environ.get("email_password", "Just4go_135")
# email_recipient = os.environ.get("email_recipient", "planas.raul@gmail.com")
# email_subject = "Your Delivery Note - Raul Planas"


# try:
#     port = int(port)
# except ValueError:
#     print(f"Invalid port value: {port}. Please check your environment variable.")
#     port = 5432  # Fallback to a default p



# # Test the connection (for debugging)
# try:
#     conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
#     print("Connected successfully")
#     conn.close()
# except Exception as e:
#     print("Connection failed: {}".format(e))

# def get_item_details(barcode):
#     item = None
#     conn_str = f"dbname='{dbname}' user='{user}' password='{password}' host='{host}' port='{port}'"
#     try:
#         with psycopg2.connect(conn_str) as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute("SELECT product_id, product_name, product_price, product_stock FROM products WHERE barcode = %s", (barcode,))
#                 item = cursor.fetchone()
#         return item
#     except Exception as e:
#         print("Database connection failed due to {}".format(e))
        
        
#----------------------------------------      
import psycopg2
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load .env file
load_dotenv('./.env')

# Fetch environment variables with default values
dbname = os.environ.get("dbname", "SCMBATCH3")
user = os.environ.get("user", "postgres")
password = os.environ.get("password", "Just4fun_135")
host = os.environ.get("host", "localhost")
port = os.environ.get("port", "5434")

# Email credentials and settings
email_user = os.environ.get("email_user", "your_email@example.com")
email_password = os.environ.get("email_password", "your_email_password")
email_recipient = os.environ.get("email_recipient", "recipient@example.com")
email_subject = "Your Delivery Note"

try:
    port = int(port)
except ValueError:
    print(f"Invalid port value: {port}. Please check your environment variable.")
    port = 5432  # Fallback to a default port

# Test the connection (for debugging)
try:
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    print("Connected successfully")
    conn.close()
except Exception as e:
    print("Connection failed: {}".format(e))

def get_item_details(barcode):
    item = None
    conn_str = f"dbname='{dbname}' user='{user}' password='{password}' host='{host}' port='{port}'"
    try:
        with psycopg2.connect(conn_str) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT product_id, product_name, product_price, product_stock FROM products WHERE barcode = %s", (barcode,))
                item = cursor.fetchone()
        return item
    except Exception as e:
        print("Database connection failed due to {}".format(e))

def send_delivery_note_by_email(barcode):
    # Get item details
    item_details = get_item_details(barcode)
    if not item_details:
        print(f"No item found with barcode: {barcode}")
        return

    # Create the delivery note content
    product_id, product_name, product_price, product_stock = item_details
    message_body = f"""
    Delivery Note:
    
    Product ID: {product_id}
    Product Name: {product_name}
    Product Price: ${product_price}
    Product Stock: {product_stock} units
    
    Thank you for your purchase!
    """

    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = email_user
    message['To'] = email_recipient
    message['Subject'] = email_subject

    # Attach the body with the msg instance
    message.attach(MIMEText(message_body, 'plain'))

    # Create the server object
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)
        text = message.as_string()
        server.sendmail(email_user, email_recipient, text)
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
barcode = '1234567890123'
send_delivery_note_by_email(barcode)
        
    