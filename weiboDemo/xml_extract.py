import xml.etree.cElementTree as cET


def get_corpus(path):
    tree = cET.parse(path)
    root = tree.getroot()

    texts = []
    tags = []
    for child in root:
        sentences = child.findall("sentence")
        for sentence in sentences:
            if sentence.text:
                tags.append(sentence.get("emotion_tag"))
                texts.append(sentence.text)
    return texts, tags


if __name__ == "__main__":
    texts, tags = get_corpus("datasets/evsam02.xml")
    print(texts)
    print(tags)
    print(len(tags))
    print(len(texts))




