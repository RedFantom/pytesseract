"""
Python Wrapper around Tesseract-OCR

Author: RedFantom
License: GNU GPLv3
"""
# Standard Library
from os.path import join, abspath, realpath, dirname
from unittest import TestCase
# Packages
from PIL import Image
# Package to test
from src import image_to_string


def printf(*args):
    print(*args, flush=True)


class TestImageToString(TestCase):
    IMAGES = {
        "test.png":
            "This is a lot of 12 point text to test the\n"
            "ocr code and see if it works on all types\n"
            "of file format.\n\n"
            "The quick brown dog jumped over the\n"
            "lazy fox. The quick brown dog jumped\n"
            "over the lazy fox. The quick brown dog\n"
            "jumped over the lazy fox. The quick\n"
            "brown dog jumped over the lazy fox.",
        "test-european.jpg":
            "The (quick) [brown] {fox} jumps!\n"
            "Over the $43,456.78 <laxy> #90 dog\n"
            "& duck/goose, as 12.5% of E-mail\n"
            "from aspammer@website.com is spam.\n"
            "Der \u201Eschelle\u201C braune Fuchs springt\n"
            "über den faulen Hund. Le renard brun\n"
            "\u00BBrapide\u00AB saute par-dessus le chien\n"
            "paressaux. La volpe marrone rapida\n"
            "salta sopra il cane pigro. El zorro\n"
            "marrón rápido salta sobre el perro\n"
            "perezoso. A raposa marrom rápida\n"
            "salta sobre o cão pregui\u00E7oso."
    }

    def test_image_to_string(self):
        directory = realpath(join(dirname(abspath(__file__)), "..", "src"))
        results = dict()
        for file_name, expected in self.IMAGES.items():
            path = join(directory, file_name)
            image = Image.open(path)
            results[file_name] = image_to_string(image)
        for (file_name, expected), (_, result) in zip(self.IMAGES.items(), results.items()):
            if result == expected:
                printf("File passed: {}".format(file_name))
            self.assertEqual(result, expected)
