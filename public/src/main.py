from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    html_node = HTMLNode(None, None, None, {
        "href": "https://www.google.com", 
        "target": "_blank",})
    leaf_node = LeafNode("p", "This is a paragraph of text.")
    
    print(leaf_node.to_html())


if __name__ == "__main__":
    main()