import cv2

cap = cv2.VideoCapture(0)  # Open webcam

while True:
    ret, frame = cap.read()
    edges = cv2.Canny(frame, 100, 500)  # Apply edge detection

    cv2.imshow('Edge Detection', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
