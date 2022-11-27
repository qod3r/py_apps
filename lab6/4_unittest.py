import unittest
from reverse import reverse


class ReverseTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(""), "")

    def test_single(self):
        self.assertEqual(reverse("a"), "a")

    def test_palindrome(self):
        self.assertEqual(reverse("aboba"), "aboba")

    def test_string(self):
        self.assertEqual(reverse("asd"), "dsa")

    def test_noniter_nonstr(self):
        with self.assertRaises(TypeError):
            reverse(11)

    def test_iter_nonstr(self):
        with self.assertRaises(TypeError):
            reverse(["a", "b", "c"])


if __name__ == "__main__":
    unittest.main()
