import unittest
from download_helper import download_helper

class UtilsTests(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(download_helper.file_exists("tests/files/keepfile.txt"))
        self.assertFalse(download_helper.file_exists("tests/files/doesntexist.txt"))


    def test_download_helper_from_uri(self):
        # TODO: fix this - this is a horrible way to test...
        uri = "https://yt3.ggpht.com/-p-K2HbhiCfE/AAAAAAAAAAI/AAAAAAAAAAA/k4V1tvBNygo/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"
        filename = "tests/files/test_pic.jpg"
        download_helper.download_file_from_uri(uri, filename)
        self.assertTrue(download_helper.file_exists(filename))
        download_helper.delete_file(filename)
        self.assertFalse(download_helper.file_exists(filename))

        uri = "http://cdn.exxonmobil.com/~/media/global/images/supporting-images/portraits/boskin-2016_supporting-portrait.jpg?as=1&h=NaN&w=NaN"
        filename = "tests/files/test_pic1.jpg"
        download_helper.download_file_from_uri(uri, filename)
        self.assertTrue(download_helper.file_exists(filename))
        download_helper.delete_file(filename)
        self.assertFalse(download_helper.file_exists(filename))

    def test_get_file_details(self):
        uri = "https://yt3.ggpht.com/-p-K2HbhiCfE/AAAAAAAAAAI/AAAAAAAAAAA/k4V1tvBNygo/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"
        file = download_helper.get_file_details(uri)
        self.assertEqual(file['extension'], '.jpg')

        filename = "a_file.csv"
        file = download_helper.get_file_details(filename)
        self.assertEqual(file['extension'], '.csv')

# python -m unittest discover -s tests -p "*_tests.py"
