import os
import sys

from ._internals.count_words import CountWordsMixin
from ._internals.preprocess_lines import PreprocessLinesMixin
from ._internals.read_all_lines import ReadAllLinesMixin
from ._internals.split_into_words import SplitIntoWordsMixin
from ._internals.write_word_counts import WriteWordCountsMixin


class ParseArgsMixin:
    def parse_args(self):
        if len(sys.argv) != 3:
            print("Usage: python3 -m homework <input_folder> <output_folder>")
            sys.exit(1)
        self.input_folder = sys.argv[1]
        self.output_folder = sys.argv[2]


class WordCountApp(
    ParseArgsMixin,
    ReadAllLinesMixin,
    PreprocessLinesMixin,
    SplitIntoWordsMixin,
    CountWordsMixin,
    WriteWordCountsMixin,
):
    def __init__(self):
        self.input_folder = None
        self.output_folder = None
        self.lines = None
        self.preprocessed_lines = None
        self.words = None
        self.word_counts = None

    def run(self):

        self.parse_args()
        self.read_all_lines()
        self.preprocess_lines()
        self.split_into_words()
        self.count_words()
        self.write_word_counts()

if __name__ == "__main__":
    WordCountApp().run()
 