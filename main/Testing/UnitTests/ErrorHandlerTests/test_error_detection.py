# test_error_detection.py
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from Core.ErrorHandling.error_detection import ErrorDetection

# Instantiate ErrorDetection
error_detector = ErrorDetection()

# Test cases
print("Testing Error Detection...")
task1 = None
task2 = {"action": "open"}
task3 = {"target": "chrome"}
task4 = {"action": "open", "target": "chrome"}

print("Task 1 Error:", error_detector.detect_error(task1))  # Should log error for no task
print("Task 2 Error:", error_detector.detect_error(task2))  # Should log error for missing 'target'
print("Task 3 Error:", error_detector.detect_error(task3))  # Should log error for missing 'action'
print("Task 4 Error:", error_detector.detect_error(task4))  # Should return False (no error)
