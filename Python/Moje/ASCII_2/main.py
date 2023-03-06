from PIL import Image
from numpy import asarray
user_screen_width = 100

def Image_To_Array(path, user_screen_width):
    image = Image.open(path).convert("L")
    scale = image.width//user_screen_width
    image = image.resize((round(image.width*1.75)//scale, (image.height//scale)))
    return asarray(image)

def Image_To_ASCII(path, user_screen_width):
    image_pixel_array = Image_To_Array(path, user_screen_width)
    ascii_chars = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', '.', ' ']
    ASCII_image = [[ascii_chars[(pixel//4)] for pixel in row] for row in image_pixel_array]
    return ASCII_image

def Printout_ASCII_Image(ASCII_image):
    for row in ASCII_image:
        print("".join(row))

Printout_ASCII_Image(Image_To_ASCII("koala.jpeg", user_screen_width))