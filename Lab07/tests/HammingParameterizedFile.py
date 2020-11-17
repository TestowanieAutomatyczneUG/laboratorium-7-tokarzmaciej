import unittest
from sample.Hamming import *

class HammingParameterizedFile(unittest.TestCase):

    def test_from_file(self):
      fileTest = open("data/hamming_data_test")
      tmpHamming = Hamming()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            inp1, inp2, result = (data[0], data[1], int(data[2]))
            self.assertEqual(tmpHamming.distance(inp1, inp2), result)
      fileTest.close()

    def test_exceptions_from_file(self):
      fileTest = open("data/hamming_exception_data_test")
      tmpHamming = Hamming()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            inp1, inp2, message = (data[0], data[1], data[2].strip("\n"))
            self.assertRaisesRegex(Exception, message, tmpHamming.distance, inp1, inp2)
      fileTest.close()


if __name__ == '__main__':
    unittest.main()
