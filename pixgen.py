import numpy as np
from PIL import Image

# Load the reference image
ref_image = Image.open('home/darkstar/pixgen/input/picture.jpg')
ref_pixels = np.array(ref_image)

# Define the amount of randomness to add
random_factor = 20  # You can adjust this value

# Generate random pixel values based on the reference image
random_pixels = ref_pixels + np.random.randint(-random_factor, random_factor,
ref_pixels.shape)

# Clip the pixel values to be within valid range (0-255)
random_pixels = np.clip(random_pixels, 0, 255)

# Create a new image from the random pixel values
new_image = Image.fromarray(random_pixels.astype('uint8'))

# Save or display the new image
new_image.save('home/darkstar/pixgen/image.jpg')
new_image.show()
