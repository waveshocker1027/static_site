import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_multiple(self):
        node = HTMLNode(
            tag="a",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        result = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(result, expected)

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p")
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_props_to_html_single(self):
        node = HTMLNode(
            tag="img",
            props={"src": "image.png"},
        )
        result = node.props_to_html()
        expected = ' src="image.png"'
        self.assertEqual(result, expected)

    def test_repr(self):
        node = HTMLNode(
            tag="p",
            value="Hello",
            children=[],
            props={"class": "text"},
        )
        repr_str = repr(node)
        self.assertIn("HTMLNode", repr_str)
        self.assertIn("p", repr_str)
        self.assertIn("Hello", repr_str)

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_anchor(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_with_multiple_props(self):
        node = LeafNode(
            "a",
            "Link",
            {"href": "https://example.com", "target": "_blank"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://example.com" target="_blank">Link</a>'
        )

    def test_leaf_missing_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_repr(self):
        node = LeafNode("span", "text", {"class": "highlight"})
        repr_str = repr(node)
        self.assertIn("LeafNode", repr_str)
        self.assertIn("span", repr_str)
        self.assertIn("text", repr_str)

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                LeafNode(None, " text "),
                LeafNode("i", "italic"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold</b> text <i>italic</i></p>"
        )

    def test_nested_parents(self):
        inner = ParentNode(
            "span",
            [LeafNode("b", "deep")]
        )
        outer = ParentNode("div", [inner])
        self.assertEqual(
            outer.to_html(),
            "<div><span><b>deep</b></span></div>"
        )

    def test_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "text")],
            {"class": "container"}
        )
        self.assertEqual(
            node.to_html(),
            '<div class="container"><p>text</p></div>'
        )

    def test_no_children_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_no_tag_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "text")])

    def test_empty_children_list(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

if __name__ == "__main__":
    unittest.main()
