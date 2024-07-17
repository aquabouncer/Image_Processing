import cv2
import os

"""I included this basic set up so that you could mess with the diffrent image processing steps to see what each one does. Just change the image you want to display
in the cv2.imshow()

 """

directory ="your image directory here dont forget to \\"
image = cv2.imread(directory)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_blur = cv2.GaussianBlur(image_gray, (5, 5), 0)

image_edge = cv2.Canny(image_blur, 50, 150)
processed_contours, _ = cv2.findContours(image_edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

final_image = cv2.drawContours(image, processed_contours, -1, (0, 255, 0), 2)

if image is None:
    print("Error: Could not read the image.")
else:
    # Display the image in a window
    cv2.imshow('Image Window', final_image)

    # Wait for a key press indefinitely or for a specified amount of time in milliseconds
    cv2.waitKey(0)

    # Destroy all windows created by OpenCV
    cv2.destroyAllWindows()