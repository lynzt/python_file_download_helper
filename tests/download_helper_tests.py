import unittest
from download_helper import download_helper

class UtilsTests(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(download_helper.file_exists("tests/files/keepfile.txt"))
        self.assertFalse(download_helper.file_exists("tests/files/doesntexist.txt"))


    def test_download_helper_from_uri(self):
        # TODO: fix this - this is a horrible way to test...
        uri = "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download"
        filename = "tests/files/nyse_companies.csv"
        download_helper.download_file_from_uri(uri, filename)

        self.assertTrue(download_helper.file_exists(filename))
        download_helper.delete_file(filename)
        self.assertFalse(download_helper.file_exists(filename))



# python -m unittest discover -s tests -p "*_tests.py"
