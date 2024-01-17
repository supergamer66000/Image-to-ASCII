import PIL.Image

__version__ = 0.1

ASCII = ["@", "#", "S", "%", "?", "*", "+", ":", ",", "."]

def resize_image(image, new_width=1000):
    width, height = image.width, image.height
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def greyscale(image):
    grayscaled_image = image.convert("L")
    return grayscaled_image

def to_ASCII(image):
    pixels = image.getdata()
    characters = "".join([ASCII[pixel // 26] for pixel in pixels])
    return characters

def Main():
    # Gets the image
    image = PIL.Image.open("Image.jpg")

    new_image_data = to_ASCII(greyscale(resize_image(image)))
    pixel_count = len(new_image_data)

    ascii_image = "\\n".join(new_image_data[i:(i+200)] for i in range(0 , pixel_count, 200))

    print(ascii_image)

    with open("ascii.txt", "w") as f:
        f.write(ascii_image)

if __name__ == '__main__':
    Main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
