import qrcode
name = input("enter time=")
img=qrcode.make(name)
img.save('myqr.jpg')


# importing Image class from PIL package
from PIL import Image

# creating a object
im = Image.open("myqr.jpg")

im.show()
