import PIL
from PIL import Image
img = PIL.Image.open("C:\\Users\\Abu Bakar\\Downloads\\Untitled design")
width, height = img.size
print(width, "X", height)