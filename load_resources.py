import json
import os


def load_resources(resource_path="./datasets/flickr8k/res"):
    vocab_file_path = os.path.join(resource_path, "vocab.json")
    bag_of_words_file = os.path.join(resource_path, "bag_of_words.json")
    doc_freq_file = os.path.join(resource_path, "doc_freq.json")

    with open(vocab_file_path, "r") as f:
        vocab = json.load(f)

    with open(bag_of_words_file, "r") as f:
        bag_of_words = json.load(f)

    with open(doc_freq_file, "r") as f:
        doc_freq = json.load(f)

    return vocab, bag_of_words, doc_freq
