import unittest

from py_to_md import read_py, read_markdown, write_markdown


class TestSum(unittest.TestCase):
    def test_read_py_have_file(self):
        """Test the read_py function if have file."""
        title_py, all_info_py = read_py('solution.py')
        self.assertEqual(title_py, "+ [Print Hello](#print-hello)\n", 'Should be "+ [Print Hello](#print-hello)\n"')
        self.assertEqual(all_info_py, """## Print Hello

Напечатать на экран Hello!

```python 
def print_hello():
    print('Hello!')
```""", '''Should be "## Print Hello

Напечатать на экран Hello!

```python 
def print_hello():
    print('Hello!')
```"''')

    def test_read_py_havent_file(self):
        """Test the read_py function if not have file."""
        title_py, all_info_py = read_py('solution1.py')
        self.assertEqual(title_py, None, 'Should be "None"')
        self.assertEqual(all_info_py, None, 'Should be "None"')

    def test_read_markdown_have_file(self):
        """Test the read_markdown function if have file."""
        titles, all_info = read_markdown('out.md')
        self.assertEqual(titles, "+ [Print Hello](#print-hello)", 'Should be "+ [Print Hello](#print-hello)"')
        self.assertEqual(all_info, '''## Print Hello

Напечатать на экран Hello!

```python 
def print_hello():
    print('Hello!')
```
''')

    def test_read_markdown_havent_file(self):
        """Test the read_markdown function if not have file."""
        title_py, all_info_py = read_py('out1.md')
        self.assertEqual(title_py, None, 'Should be "None"')
        self.assertEqual(all_info_py, None, 'Should be "None"')


if __name__ == '__main__':
    unittest.main()