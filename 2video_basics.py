import cv2

cap = cv2.VideoCapture(0) #open window(default)

while True:
    ret, frame = cap.read() #read frame
    cv2.imshow('Live Video', frame) #display frames

    if cv2.waitKey(1) & 0xFF == ord('q') : #press 'q' to exit
          break
    
cap.release() #release the window
cv2.destroyAllWindows() #close the whole window