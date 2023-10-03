import threading
import cv2
import time
import speech_recognition as sr

# Initialize recognizer class (for recognizing speech)
rec = sr.Recognizer()

# Function to capture video from the camera
def camera_task():
    # Open the default camera (camera index 0)
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Error reading frame from the camera.")
            break

        # Display the frame (you can replace this with your actual processing logic)
        cv2.imshow('Camera Task', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera when the loop is exited
    cap.release()
    cv2.destroyAllWindows()

# Function to simulate microphone task
def microphone_task():
    while True:
        with sr.Microphone() as mic:
            try:
                print("Microphone task: Listening to audio")
                audio = rec.listen(mic, phrase_time_limit=3, timeout=5)
                text = rec.recognize_google(audio).lower()
                print('Converting audio transcripts into text...')
                print('Text:', text)
                time.sleep(1)
            except sr.UnknownValueError:
                # Handle unknown value error
                print("Speech Recognition could not understand audio.")
            except sr.WaitTimeoutError:
                # Handle timeout error
                print("Listening timed out. Please speak again.")
            except sr.RequestError as e:
                # Handle request error
                print(f"Could not request results from Google Speech Recognition service; {e}")

# Create threads
camera_thread = threading.Thread(target=camera_task)
microphone_thread = threading.Thread(target=microphone_task)

# Start threads
camera_thread.start()
microphone_thread.start()

# Wait for threads to finish (optional)
camera_thread.join()
microphone_thread.join()

print("Both tasks are completed.")
