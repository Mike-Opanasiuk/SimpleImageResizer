
from PIL import Image

# Open the image
image = Image.open("your_image.png")

# Resize with a 640x328 aspect ratio
resized_image = image.resize((640, 328))
resized_image.save("resized_image.png")