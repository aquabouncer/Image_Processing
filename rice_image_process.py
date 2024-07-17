import os
import cv2
import numpy as np

input_directory = "C:\\Users\\Zebus\\Desktop\\rice\\Rice_Image_Dataset\\Jasmine"
output_directory = "C:\\Users\\Zebus\\Desktop\\rice\\Processed_Rice_Images4"

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Process each image in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        file_path = os.path.join(input_directory, filename)
        image = cv2.imread(file_path)

        if image is None:
            print(f"Error: Could not read the image {filename}.")
            continue

        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_blur = cv2.GaussianBlur(image_gray, (5, 5), 0)
        image_edge = cv2.Canny(image_blur, 50, 150)
        processed_contours, _ = cv2.findContours(image_edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in processed_contours:
            if len(contour) >= 5:  # fitEllipse requires at least 5 points
                ellipse = cv2.fitEllipse(contour)
                image = cv2.ellipse(image, ellipse, (0, 255, 0), 2)
                
                # Extract center, axes, and angle
                center, axes, angle = ellipse
                center = tuple(map(int, center))
                axes = tuple(map(int, axes))

                # Calculate the end point of the line indicating orientation
                length = max(axes) // 2
                angle_rad = np.deg2rad(angle)
                end_point = (
                    int(center[0] + length * np.cos(angle_rad)),
                    int(center[1] + length * np.sin(angle_rad))
                )
                
                # Draw the orientation line
                image = cv2.line(image, center, end_point, (255, 0, 0), 2)
                
                # Optionally draw an arrow to indicate direction
                #image = cv2.arrowedLine(image, center, end_point, (255, 0, 0), 2, tipLength=0.2)

        # Save the processed image
        output_file_path = os.path.join(output_directory, filename)
        cv2.imwrite(output_file_path, image)

print("Processing complete. Processed images are saved in the output directory.")
