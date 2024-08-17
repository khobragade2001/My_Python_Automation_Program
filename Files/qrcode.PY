import qrcode
from PIL import Image

img = qrcode.make("9673040564@ybl")
img.save("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\Phone_Pay.png")

# colour full qrcode
# qr = qrcode.QRCode(version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_H,
#     box_size=20,border=5)
#
# qr.add_data("9673040564@ybl")
# qr.make(fit=True)
# img=qr.make_image(fill_color="black",back_color="cyan")
# img.save("c:\\color_sbi.png")