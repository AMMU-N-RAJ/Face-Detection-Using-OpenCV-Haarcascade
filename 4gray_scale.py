import cv2

# Read image
image = cv2.imread('Sample.jpg')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(gray_image, (15,15), 0)

# Display results
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Blurred Image', blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
