import cv2
import numpy as np
import pyautogui
import time

# Definining screen resolution and frame rate
screen_width, screen_height = pyautogui.size()
frame_rate = 30
output_file = "screen_recording.avi"

# Initialize video writer object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
video_writer = cv2.VideoWriter(output_file, fourcc, frame_rate, (screen_width, screen_height))

# Function to capture screen
def capture_screen():
    print("Recording started. Press 'q' to stop.")
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
          
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        video_writer.write(frame)
        
        
        cv2.imshow('Screen Recorder', frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
capture_screen()

# Release the video writer object and close any OpenCV windows
video_writer.release()
cv2.destroyAllWindows()
print("Recording stopped. Video saved as", output_file)
