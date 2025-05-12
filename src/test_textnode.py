import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq_none_url(self):
        node = TextNode("Text node",TextType.BOLD,None)
        node2 = TextNode("Text node",TextType.BOLD,None)
        self.assertEqual(node,node2)
    def test_eq_different(self):
        node = TextNode("Text node",TextType.BOLD)
        node2 = TextNode("Text mode",TextType.BOLD)
        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()

