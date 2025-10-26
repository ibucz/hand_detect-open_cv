import cv2
import mediapipe as mp
#import serial
import time

# Initialize serial connection (replace 'COM3' with your Arduino port)

#arduino = serial.Serial('/dev/ttyUSB0', 9600)
#time.sleep(2)  # Wait for Arduino to initialize


# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize OpenCV video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image and detect hands
    results = hands.process(rgb_frame)

    # Initialize hand labels
    left_hand = False
    right_hand = False

    # Draw hand landmarks
    if results.multi_hand_landmarks:
        for hand_info in results.multi_handedness:
            handedness = hand_info.classification[0].label
            if handedness == 'Left':
                left_hand = True
            elif handedness == 'Right':
                right_hand = True

    # Determine what to display
    if left_hand and right_hand:
        message = "Both Hands Raised"
    elif left_hand:
        message = "Left Hand Raised"
    elif right_hand:
        message = "Right Hand Raised"
    else:
        message = ""

    # Send message to Arduino if not empty
    if message:
    #    print(f"Sending message: {message}") 
    #    arduino.write(f"{message}\n".encode())
       cv2.putText(frame, message, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    #else:
        # Clear the LCD message if no hands are raised
    #    arduino.write(f"                \n".encode())  # Send empty spaces to clear

    # Display the frame
    cv2.imshow('Hand Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
#arduino.close()