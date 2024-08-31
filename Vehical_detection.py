import cv2
import os

def detect_vehicles_in_image(image_path, cascade_path):
    """Detect vehicles in an image and display the result."""
    # Load the Haar Cascade classifier
    car_cascade = cv2.CascadeClassifier(cascade_path)
    
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect vehicles
    vehicles = car_cascade.detectMultiScale(gray, 1.1, 1)
    
    # Draw rectangular frames around detected vehicles
    for (x, y, w, h) in vehicles:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display the output
    cv2.imshow('Vehicle Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_vehicles_in_video(video_path, cascade_path, output_path=None):
    """Detect vehicles in a video and optionally save the result."""
    # Load the Haar Cascade classifier
    car_cascade = cv2.CascadeClassifier(cascade_path)
    
    # Capture video from file
    video_capture = cv2.VideoCapture(video_path)
    
    # Define the codec and create VideoWriter object if output_path is provided
    if output_path:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(video_capture.get(3)), int(video_capture.get(4))))
    
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        vehicles = car_cascade.detectMultiScale(gray, 1.1, 1)
        
        # Draw rectangular frames around detected vehicles
        for (x, y, w, h) in vehicles:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Display the frame
        cv2.imshow('Vehicle Detection', frame)
        
        # Write the frame to the output video if output_path is provided
        if output_path:
            out.write(frame)
        
        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release everything if the job is finished
    video_capture.release()
    if output_path:
        out.release()
    cv2.destroyAllWindows()

def main():
    # Path to the Haar Cascade XML file
    cascade_path = 'haarcascade_car.xml'
    
    # Detect vehicles in an image
    image_path = 'path_to_your_image.jpg'
    detect_vehicles_in_image(image_path, cascade_path)
    
    # Detect vehicles in a video
    video_path = 'path_to_your_video.mp4'
    output_path = 'output_video.avi'  # Optional: Save the output video
    detect_vehicles_in_video(video_path, cascade_path, output_path)

if __name__ == "__main__":
    main()
