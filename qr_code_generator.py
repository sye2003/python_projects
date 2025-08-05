import qrcode

data= input("Enter a text or URL to generate QR code: ").strip()
filename = input("Enter the filename to save the QR code: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image= qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR code generated and saved as {filename}")
print("You can scan the QR code with your mobile device to access the data.")
