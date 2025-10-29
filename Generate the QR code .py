import qrcode
from PIL import Image

# Step 1: Take input from user
data = input("Enter text or link to generate QR code: ")

# Step 2: Create a QRCode object with custom settings
qr = qrcode.QRCode(
    version=1,  # QR size (1-40); higher means bigger and more data capacity
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction (for logo support)
    box_size=10,  # size of each box in the QR grid
    border=4,     # white border size
)

qr.add_data(data)
qr.make(fit=True)

# Step 3: Generate the QR code image with color customization
qr_img = qr.make_image(fill_color="blue", back_color="white").convert('RGB')

# Step 4 (Optional): Add a logo in the center
try:
    logo = Image.open("logo.png")  # put your logo file in same folder
    box_size = qr_img.size[0] // 4  # logo size = 1/4th of QR
    logo = logo.resize((box_size, box_size))

    # Calculate position for the logo to be centered
    pos = ((qr_img.size[0] - box_size) // 2, (qr_img.size[1] - box_size) // 2)
    qr_img.paste(logo, pos)
except FileNotFoundError:
    print("⚠️ Logo file not found! Skipping logo...")

# Step 5: Save final QR image
qr_img.save("custom_qrcode.png")
print("✅ Custom QR Code generated successfully and saved as 'custom_qrcode.png'")
