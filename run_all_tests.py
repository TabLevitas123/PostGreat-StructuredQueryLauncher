
import os
import unittest
import sys
import time

def list_test_files(test_dir="tests"):
    return [f for f in os.listdir(test_dir) if f.startswith("test_") and f.endswith(".py")]

def run_all_tests():
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    
    # Display available tests
    print("Detected Test Files:")
    for test_file in list_test_files():
        print(f" - {test_file}")
    
    # Load all test cases from the tests directory
    test_suite = test_loader.discover(start_dir="tests", pattern="test_*.py")
    
    # Run tests and display results with a simple UI
    print("\nRunning Tests...")
    result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    
    # Display summary
    print("\nTest Summary:")
    print(f"Total Tests Run: {result.testsRun}")
    print(f"Errors: {len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    
    if result.wasSuccessful():
        print("All tests passed successfully!")
    else:
        print("Some tests failed. Please check errors and failures above.")

if __name__ == "__main__":
    print("===== Database Creation Wizard Test Runner =====")
    time.sleep(1)
    run_all_tests()
