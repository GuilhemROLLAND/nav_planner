from PIL import ImageEnhance
from PIL import Image

def increase_brightness(image_path, factor=1.5):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to RGB mode
    image = image.convert("RGB")

    # Create a brightness enhancement object
    enhancer = ImageEnhance.Brightness(image)

    # Increase the brightness of the image
    enhanced_image = enhancer.enhance(factor)

    # Save the enhanced image
    enhanced_image.save("bright_images/" + image_path.split("/")[-1])


if __name__ == "__main__":
    increase_brightness("image_satellite.png")
