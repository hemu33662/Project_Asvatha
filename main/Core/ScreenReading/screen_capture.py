import threading
import mss
import numpy as np
import cv2
import time
from ocr_processor import OCRProcessor  # Assuming OCRProcessor is in a separate file named ocr_processor.py

class ScreenCapture:
    def __init__(self):
        self.running = threading.Event()
        self.ocr_processor = OCRProcessor()  # Initialize OCRProcessor instance
    
    def start_capture(self):
        self.running.set()  # Signal to start capture
        thread = threading.Thread(target=self._capture_loop, daemon=True)
        thread.start()
    
    def stop_capture(self):
        self.running.clear()  # Signal to stop capture
    
    def _capture_loop(self):
        with mss.mss() as sct:  # Initialize mss inside the thread
            monitor = sct.monitors[1]  # Capture primary screen
            print("Monitor dimensions:", monitor)  # Debugging: Print monitor dimensions
            while self.running.is_set():
                screenshot = sct.grab(monitor)
                frame = np.array(screenshot)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)  # Convert BGRA to BGR for OpenCV
                
                # Debugging: Check if frame is being captured
                print(f"Captured frame with shape: {frame.shape}")

                # Extract text from the captured frame using OCRProcessor
                extracted_text = self.ocr_processor.extract_text_from_screenshot(frame)
                
                # Debug print for OCR text
                print("Extracted Text:", extracted_text)  # Print the extracted text from the frame
                
                # Optionally, you can display the live screen capture
                cv2.imshow('Live Screen Capture', frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cv2.destroyAllWindows()


# Example test case
if __name__ == '__main__':
    # Initialize ScreenCapture instance
    screen_capture = ScreenCapture()

    # Start screen capture
    print("Starting screen capture with OCR...")
    screen_capture.start_capture()

    # Run capture for 10 seconds and then stop (for debugging purposes)
    time.sleep(10)
    screen_capture.stop_capture()
    print("Screen capture stopped.")
