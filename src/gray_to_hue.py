import cv2
import numpy as np
from tkinter.filedialog import askopenfilename
import tkinter as tk
import os




#Getting the heightmap
root = tk.Tk()
print("Please select Gray-scale Heightmap")
grayscale_image = cv2.imread(askopenfilename(initialdir=os.getcwd(), title="Please select Gray-scale Map"), cv2.IMREAD_GRAYSCALE)
root.destroy()


def grayscale_to_hsv(grayscale_image):
    # Create a blank HSV image of the same size
    height, width = grayscale_image.shape
    hsv_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Set saturation and value to maximum
    hsv_image[:, :, 1] = 255
    hsv_image[:, :, 2] = 255

    # Set hue based on grayscale intensity
    hsv_image[:, :, 0] = grayscale_image

    # Convert HSV image to BGR (for display purposes)
    bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    return bgr_image

# Convert grayscale to HSV
hsv_image = grayscale_to_hsv(grayscale_image)

# Display the original grayscale and the resulting HSV image
cv2.imwrite('HSV Image.png', hsv_image)
