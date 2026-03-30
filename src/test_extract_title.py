import unittest
from extract_title import extract_title  # adjust import

class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")

    def test_title_with_whitespace(self):
        md = "   #   Hello World   "
        self.assertEqual(extract_title(md), "Hello World")

    def test_multiple_lines(self):
        md = """
Some text
# My Title
More text
"""
        self.assertEqual(extract_title(md), "My Title")

    def test_no_title(self):
        md = "No header here"
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()
