import qrcode
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.youtube.com/c/SeaOfCPrograms')
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="black")
img.save("Image1.png")

import cv2

d = cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("Channel.jpg"))
""" print(val)
print(points)
print(straight_qrcode) """