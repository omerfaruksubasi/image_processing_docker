import cv2

# Load the image
# Replace 'input.jpg' with the path to your image
image = cv2.imread('lenna.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the original image
    cv2.imshow("Original Image", image)

    # Display the grayscale image
    cv2.imshow("Grayscale Image", gray_image)

    # Save the grayscale image
    # Replace 'output.jpg' with the desired output file path
    cv2.imwrite('output.jpg', gray_image)
    print("Grayscale image saved as 'output.jpg'")

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

