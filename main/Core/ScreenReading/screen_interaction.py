import pyautogui
import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

class ScreenInteraction:
    def __init__(self, typing_speed=0.1):
        self.typing_speed = typing_speed  # Allows configurable typing speed

    def click_on(self, x, y):
        pyautogui.click(x, y)
        time.sleep(0.1)  # Small delay to ensure UI responsiveness

    def type_text(self, text):
        pyautogui.write(text, interval=self.typing_speed)

    def locate_and_click(self, image_path):
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
            if location:
                pyautogui.click(location)
                return True
            print(f"Image not found: {image_path}")
            return False
        except Exception as e:
            print(f"Error during image recognition: {e}")
            return False

    def scroll(self, amount):
        pyautogui.scroll(amount)

    def move_mouse(self, x, y):
        pyautogui.moveTo(x, y, duration=0.2)

if __name__ == "__main__":
    screen_interaction = ScreenInteraction(typing_speed=0.05)

    try:
        print("Starting interaction tests...")
        time.sleep(2)  # Give user time to switch to an application

        # Example test actions:
        screen_interaction.click_on(500, 500)  # Click on a coordinate
        screen_interaction.type_text("Hello, this is a test!")  # Type text
        screen_interaction.scroll(-500)  # Scroll down
        screen_interaction.move_mouse(1000, 500)  # Move mouse

        print("Test complete.")
    except KeyboardInterrupt:
        print("Program terminated by user.")
