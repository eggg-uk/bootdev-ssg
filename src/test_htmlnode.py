import unittest

from htmlnode import HTMLNode,LeafNode

class TestHtmlNode(unittest.TestCase):
    #html
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

    #leaf
    def test_leaf_to_html(self):
        node = LeafNode("p","diddlydoodly howdy")
        expected_result = '<p>diddlydoodly howdy</p>'
        self.assertEqual(node.to_html(),expected_result)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_invalid(self):
        node = LeafNode("h1",None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    #parent
if __name__ == "__main__":
    unittest.main()
