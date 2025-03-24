import cv2

image = cv2.imread('sample.jpg')  # Load an image
cv2.imshow('Sample Image', image)  # Show image
cv2.waitKey(0)  # Wait for key press
cv2.destroyAllWindows()  # Close all windows