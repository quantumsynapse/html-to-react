import unittest
from src.converter import html_to_react

class TestHtmlToReact(unittest.TestCase):

    def test_basic_conversion(self):
        html_code = "<div>Hello World!</div>"
        expected_react_code = "<div>Hello World!</div>"
        self.assertEqual(html_to_react(html_code), expected_react_code)

if __name__ == "__main__":
    unittest.main()

