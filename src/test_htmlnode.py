import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        props_to_pass = {"href": "https://www.google.com","target": "_blank",}
        node = HTMLNode(props=props_to_pass)
        expected_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(),expected_result)

    def test_eq(self):
        props_to_pass = {"href": "https://www.google.com","target": "_blank",}
        node = HTMLNode(props=props_to_pass)
        node2 = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node,node2)

    def test_eq_different(self):
        props_to_pass = {"href": "https://www.google.com","target": "_blank",}
        node = HTMLNode(props=props_to_pass)
        node2 = HTMLNode()
        self.assertNotEqual(node,node2)

if __name__ == "__main__":
    unittest.main()
