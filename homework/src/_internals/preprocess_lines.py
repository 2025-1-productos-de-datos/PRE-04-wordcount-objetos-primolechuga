class PreprocessLinesMixin:
    def preprocess_lines(self):
        """Preprocess lines by normalizing and cleaning text."""
        print("Preprocessing lines...")
        print(f"Original lines: {self.lines}")
        self.preprocessed_lines = [line.lower().strip() for line in self.lines]
        print(f"Preprocessed lines: {self.preprocessed_lines}")