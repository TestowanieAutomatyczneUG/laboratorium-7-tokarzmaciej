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


if __name__ == '__main__':
    unittest.main()