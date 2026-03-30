def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()

    raise Exception("No H1 header found")
