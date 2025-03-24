import cv2

image = cv2.imread("Sample.jpg") #load an image
cv2.imshow('Sample Image', image) #show image
cv2.waitKey(0) #wait for key presses
cv2.destroyAllWindows() #closes allwindows