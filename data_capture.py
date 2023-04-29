import cv2
import os

# Create a VideoCapture object to capture video from webcam
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video capture")
else:
    # Create a directory to store captured images
    if not os.path.exists('captured_images'):
        os.makedirs('captured_images')

    # Counter for image filenames
    count = 0

    # Loop to capture frames from webcam
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly, save it
        if ret:
            # Save the captured frame as a PNG image
            img_filename = f'captured_images/captured_{count}.png'
            cv2.imwrite(img_filename, frame)
            print(f'Image saved: {img_filename}')
            count += 1

            # Display the resulting frame
            cv2.imshow('Webcam', frame)

        # Wait for key press (1 millisecond)
        key = cv2.waitKey(1)

        # Exit loop if 'q' key is pressed
        if key == ord('q'):
            break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()