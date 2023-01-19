import qrcode
import os

def generate_qr(url):
    # create qr object
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    # add url to qr object
    qr.add_data(url)
    qr.make(fit=True)
    # create image from qr object
    img = qr.make_image(fill_color="black", back_color="white")
    # create a file name from the url
    file_name = url.replace("/", "-") + ".png"
    # save the image to the desktop
    img.save(os.path.expanduser("~/Desktop/") + file_name)
    # display the image
    img.show()

# get user input for url
url = input("Enter the URL: ")
# generate and save QR code image
generate_qr(url)
