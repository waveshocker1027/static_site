def split_nodes_delimiter(old_nodes, delimiter, text_type):
    from textnode import TextType, TextNode

    new_nodes = []

    for node in old_nodes:
        # Only split TEXT nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        # If no delimiter found, keep as-is
        if len(parts) == 1:
            new_nodes.append(node)
            continue

        # If uneven number of parts → missing closing delimiter
        if len(parts) % 2 == 0:
            raise Exception("Invalid markdown syntax: missing closing delimiter")

        for i, part in enumerate(parts):
            if part == "":
                continue

            # Even index → normal text
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes
