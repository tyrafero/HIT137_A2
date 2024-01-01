from PIL import Image
import time

# Load the original image
image_path = "output/peakpx.jpg"
image = Image.open(image_path)

# Get the size of the image
width, height = image.size

# Generate the number (n)
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

# Create a new image with the modified pixels
new_image = Image.new("RGB", (width, height))

# Iterate over each pixel in the original image
for x in range(width):
    for y in range(height):
        # Get the original pixel values
        r, g, b = image.getpixel((x, y))

        # Modify the pixel values by adding the generated number
        new_r = r + generated_number
        new_g = g + generated_number
        new_b = b + generated_number

        # Set the modified pixel values in the new image
        new_image.putpixel((x, y), (new_r, new_g, new_b))

# Save the new image
output_image_path = "chapter1out.png"
new_image.save(output_image_path)

# Calculate the sum of red (r) pixel values
red_sum = sum([new_image.getpixel((x, y))[0] for x in range(width) for y in range(height)])

# Display the sum of red (r) pixel values
print("Sum of red pixel values:", red_sum)