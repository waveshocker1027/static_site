class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if not self.props:
            return ""

        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str

    def __repr__(self):
        return (
            f"HTMLNode(tag={self.tag}, "
            f"value={self.value}, "
            f"children={self.children}, "
            f"props={self.props})"
        )


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # children must always be None for a leaf node
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        # If no tag, return raw text
        if self.tag is None:
            return self.value

        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

    def __repr__(self):
        return (
            f"LeafNode(tag={self.tag}, "
            f"value={self.value}, "
            f"props={self.props})"
        )


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if children is None:
            raise ValueError("ParentNode must have children")

        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")

        if self.children is None:
            raise ValueError("ParentNode must have children")

        props_str = self.props_to_html()

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"

    def __repr__(self):
        return (
            f"ParentNode(tag={self.tag}, "
            f"children={self.children}, "
            f"props={self.props})"
        )


