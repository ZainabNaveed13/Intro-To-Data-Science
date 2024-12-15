import qrcode

# Step 1: Replace with your WhatsApp number and message
phone_number = "923004200676"  # Pakistan's country code +92 (no +, spaces, or dashes)
message = (
    "Assalamualaikum! Thank you for reaching out to us. "
    "You can place your orders here, share valuable feedback about our food, "
    "or ask any queries. We look forward to serving you!"
)

# Step 2: Encode the WhatsApp link
whatsapp_link = f"https://wa.me/{phone_number}?text={message.replace(' ', '%20')}"

# Step 3: Generate the QR Code
qr = qrcode.make(whatsapp_link)

# Step 4: Save the QR Code
qr.save("whatsapp_qr.png")
print("QR Code for WhatsApp chat saved as 'whatsapp_qr.png'")
