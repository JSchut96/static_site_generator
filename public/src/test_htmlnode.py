import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    # HTMLnode Tests
    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {
            "href": "https://www.google.com", 
            "target": "_blank",
        })

        expected_result = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(node.props_to_html(), expected_result)

    def test_values(self):
        node = HTMLNode("h1", "This is a test")

        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "This is a test")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("p", "This is another test", None, {"href": "https:google.com"})

        self.assertEqual(node.__repr__(), "HTMLNode(p, This is another test, children: None, {'href': 'https:google.com'})")

    # LeafNode Tests
    def test_to_html_no_props(self):
        node = LeafNode("p", "This is a paragraph of text.")

        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_with_props(self):
        node = LeafNode("div", "This is a paragraph of text.", {'class': 'test'})

        self.assertEqual(node.to_html(), '<div class="test">This is a paragraph of text.</div>')

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a paragraph of text.", None)

        self.assertEqual(node.to_html(), "This is a paragraph of text.")

    def test_to_html_no_value(self):
        node = LeafNode("div", None, {'class': 'test'})

        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertEqual(str(context.exception), "All leaf nodes must have a value")

    def test_repr(self):
        node = LeafNode("div", "This is a div.", {'class': 'test'})

        self.assertEqual(node.__repr__(), "LeafNode(div, This is a div., {'class': 'test'})")

    # ParentNode Tests
    def test_to_html(self):
        node = ParentNode("p", 
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],)

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_no_children(self):
        node = ParentNode("p", [ ],)

        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertEqual(str(context.exception), "All parent nodes must have children")

    def test_to_html_parent_as_child(self):
        node = ParentNode("p", 
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            ParentNode("p", 
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],)

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><i>italic text</i>Normal text</p>")

    def test_to_html_no_tag2(self):
        node = ParentNode(None, [ LeafNode("b", "Bold text")],)

        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertEqual(str(context.exception), "All parent nodes must have a tag")

if __name__ == "__main__":
    unittest.main()