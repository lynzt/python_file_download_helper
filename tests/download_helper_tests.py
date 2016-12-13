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

    def test_get_extension_from_uri(self):
        uri = "https://yt3.ggpht.com/-p-K2HbhiCfE/AAAAAAAAAAI/AAAAAAAAAAA/k4V1tvBNygo/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"
        ext = download_helper.get_extension_from_uri(uri)
        self.assertEqual(ext, '.jpg')

# python -m unittest discover -s tests -p "*_tests.py"
