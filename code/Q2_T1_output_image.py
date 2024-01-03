import time 
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
  generated_number += 10
print(generated_number)
import cv2
import numpy as np

# Load the image
image_path = 'output\peakpx.jpg'
original_image = cv2.imread(image_path)

# Generated number
n = generated_number

# Add the generated number to each pixel (r, g, b)
modified_image = original_image + n

# Save the modified image
cv2.imwrite('chapter1out.png', modified_image)

# Sum of all red (r) pixel values in the modified image
red_sum = np.sum(modified_image[:, :, 0])

# Output the sum
print(f"Sum of red pixel values: {red_sum}")