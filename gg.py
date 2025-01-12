import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sample tour packages
packages = [
    {"name": "Juhu Beach", "price": "1500", "description": "Enjoy the sun and sand."},
    {"name": "Lonavala", "price": "1000", "description": "Hike and explore the peaks."},
    {"name": "Pick-up & Drop", "price": "1000", "description": "Get the car at airpot and from hotel to airpot"},
    {"name": "Side seen", "price": "5000", "description": "Enjoy full side seen of mumbai suburban area"},
]

# Home Page
st.title("Welcome to Dubey tours and travels")
st.image("i.jpg", use_container_width=True)
st.markdown("Discover amazing tours and travels with us!")

# Tour Packages Section
st.header("Our Tour Packages")
for package in packages:
    st.subheader(package["name"])
    st.write(f"Price: {package['price']}")
    st.write(package["description"])

# Booking Form
st.header("Book a Tour")
name = st.text_input("Name")
email = st.text_input("Email")  # Customer's email address
tour = st.selectbox("Select Tour", [pkg["name"] for pkg in packages])

# Send email function
def send_email_to_company(name, email, tour):
    sender_email = "dvinit061@gmail.com"  # Your Gmail address
    sender_password = "vozx lmym ojni jcdn"  # Your Gmail App Password
    receiver_email = "dubeyashok9167@gmail.com"  # Your father's email address

    # Email Content to send to your father (the travel company)
    subject = "New Booking Received"
    body = f"""
    A new booking has been received!

    Booking Details:
    - Name: {name}
    - Email: {email}
    - Tour: {tour}
    """

    # Create Email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email  # Send to your father's email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(message)  # Send email to your father
            return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Submit the booking
if st.button("Submit Booking"):
    if name and email:  # Check if name and email are provided
        if send_email_to_company(name, email, tour):
            st.success(f"Booking confirmed for {name} on the {tour}.")
            st.success(f"Booking details have been sent to the travel company (your father).")
        else:
            st.error("Failed to send booking details via email.")
    else:
        st.warning("Please fill in all fields (Name and Email are required).")


# Contact Section
st.header("Contact Us")
st.write("📍 Address: Hotel Diploment,Next to Taj Mahal Hotel, opposite Starbucks ,Mumbai-40001")
st.write("📞 Phone: +91-9167125621")
st.write("📧 Email: info@travel.com")

