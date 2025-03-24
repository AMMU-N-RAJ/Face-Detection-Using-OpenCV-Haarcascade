import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")  # Create a black canvas

cv2.line(img, (50, 50), (450, 50), (0, 255, 0), 3)  # Green line
cv2.rectangle(img, (50, 100), (200, 300), (255, 0, 0), 3)  # Blue rectangle
cv2.circle(img, (300, 250), 50, (0, 0, 255), -1)  # Red circle

cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()