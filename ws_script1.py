import qrcode
from PIL import Image  # Required for image handling

# Step 1: Replace with your WhatsApp number and message
phone_number = "923004200676"  # Pakistan's country code +92 (no +, spaces, or dashes)
message = (
    "Assalamualaikum! Thank you for reaching out to us. "
    "You can place your orders here, share valuable feedback about our food, "
    "or ask any queries. We look forward to serving you!"
)

# Step 2: Encode the WhatsApp link
whatsapp_link = f"https://wa.me/{phone_number}?text={message.replace(' ', '%20')}"

# Step 3: Generate the QR Code with a custom configuration
qr = qrcode.QRCode(
    version=2,  # Controls the size of the QR Code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for embedding images
    box_size=10,  # Size of each box
    border=4,     # Border size around QR code
)

qr.add_data(whatsapp_link)
qr.make(fit=True)

# Step 4: Generate the QR Code as an image
qr_img = qr.make_image(fill="black", back_color="white")

# Step 5: Embed the Image in the Center
logo_path = "bbq.png"  # Path to the logo file
try:
    logo = Image.open(logo_path)

    # Calculate dimensions for the logo
    qr_width, qr_height = qr_img.size
    logo_size = qr_width // 4  # Logo size is 1/4th of the QR code

    # Resize the logo
    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

    # Calculate position to place the logo
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

    # Paste the logo on the QR code
    qr_img.paste(logo, pos, mask=logo.convert("RGBA").split()[3])  # Preserve transparency

except FileNotFoundError:
    print("Error: Logo file not found. Ensure 'bbq.png' exists in the same directory.")

# Step 6: Save the QR Code
qr_img.save("whatsapp_qr_with_logo.png")
print("QR Code with logo saved as 'whatsapp_qr_with_logo.png'")
