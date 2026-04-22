import unittest
from src.main import run_app

class TestMain(unittest.TestCase):
    
    def test_run_app(self):
        # Test if the application runs without errors
        try:
            run_app()
            self.assertTrue(True)  # If no exception is raised, the test passes
        except Exception as e:
            self.fail(f"Application raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()