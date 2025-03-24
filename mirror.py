import cv2

cap = cv2.VideoCapture(0)  # Open webcam

while True:
    ret, frame = cap.read()  
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip to avoid mirror effect
    half_width = frame.shape[1] // 2  

    left_half = frame[:, :half_width]  # Get left half
    mirrored_half = cv2.flip(left_half, 1)  # Mirror it

    mirrored_frame = frame.copy()
    mirrored_frame[:, half_width:] = mirrored_half  # Replace right half

    cv2.imshow("Fun Mirror Effect", mirrored_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
