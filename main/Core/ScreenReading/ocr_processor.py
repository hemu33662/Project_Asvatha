import easyocr
import numpy as np
import cv2

class OCRProcessor:
    def __init__(self):
        # Initialize EasyOCR reader
        self.reader = easyocr.Reader(['en'])  # 'en' is the language code for English

    def extract_text(self, image: np.ndarray) -> str:
        """
        Extracts text from the provided image using EasyOCR.
        """
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        result = self.reader.readtext(gray_image)
        
        # Print OCR result for debugging
        print("OCR Result:", result)
        
        # Extract text from the result (list of tuples containing text)
        extracted_text = ' '.join([text[1] for text in result])
        return extracted_text
    
    def extract_text_from_screenshot(self, screenshot: np.ndarray) -> str:
        """
        Converts a screenshot (NumPy array) into text using OCR.
        """
        text = self.extract_text(screenshot)
        print(f"OCR Text Extracted: {text}")  # Debugging: Print the OCR text
        return text


    def extract_text_from_region(self, screenshot: np.ndarray, region: tuple) -> str:
        """
        Extracts text from a specific region of the screenshot.

        :param screenshot: The full screenshot.
        :param region: A tuple (x, y, width, height) representing the region to process.
        :return: Extracted text from the region.
        """
        x, y, w, h = region
        region_of_interest = screenshot[y:y+h, x:x+w]
        return self.extract_text(region_of_interest)

# Example usage of the OCRProcessor class
if __name__ == '__main__':
    # Initialize OCRProcessor instance
    ocr_processor = OCRProcessor()

    # Load a sample image (screenshot) for OCR processing
    screenshot = cv2.imread("D:\PersonalProjects\Project_Asvatha\screenshots\Screenshot 2025-01-29 135719.png")  # Replace with your image path

    # Extract text from the full screenshot
    extracted_text = ocr_processor.extract_text_from_screenshot(screenshot)
    print("Extracted Text from Screenshot:", extracted_text)

    # Extract text from a specific region (e.g., coordinates x=50, y=50, width=200, height=100)
    region = (50, 50, 200, 100)
    extracted_text_from_region = ocr_processor.extract_text_from_region(screenshot, region)
    print("Extracted Text from Region:", extracted_text_from_region)
