import re

PUNCTUATIONS = ['.', ',', ':', ';', '?', '!', '-', '"', '“', '”',
                '/', '\\', '<', '>', '(', ')', '[', ']', '{', '}']
SPECIAL_CHARS = ['#', '$', '€', '%', '@', '*', '&',
                 '_', '|', '=', '+', '^', '`', '~', '<<', '>>']


class TetunRegexTokenizer:
    """Tokenizes text using regular expressions."""

    def __init__(self, patterns: str, split: bool = False):
        """
        Args:
            patterns (str): a regular expression to match the tokens.
            split (bool): if True, use re.split() to tokenize text, else use re.findall().            
        """
        self.patterns = patterns
        self.split = split

    def tokenize(self, text: str) -> list:
        """
        Args:
            text (str): the text to be tokenized.
        Returns:
            A list of tokens.
        """
        if self.split:
            tokens = re.split(self.patterns, text)
        else:
            tokens = re.findall(self.patterns, text)
        return tokens


class TetunStandardTokenizer(TetunRegexTokenizer):
    """ Tokenize text by word, punctuations, or special characters delimiters. """

    def __init__(self):
        patterns = (
            # e.g.: Área, área, ne'e, Ne'ebé, kompañia, ida-ne'e, ida-ne'ebé.
            r"[A-Za-záéíóúñ]+(?:[-’'][A-Za-záéíóúñ]+)*"
            r"|"
            r"[\d.]+"
            r"|"
            r"[" + re.escape("".join(PUNCTUATIONS + SPECIAL_CHARS)) + "]"
        )
        super().__init__(patterns)


class TetunWhiteSpaceTokenizer(TetunRegexTokenizer):
    """ Tokenize text by whitespace delimiter. """

    def __init__(self):
        patterns = r"\s+"
        super().__init__(patterns, split=True)


class TetunBlankLineTokenizer(TetunRegexTokenizer):
    """ Tokenize a text, treating any sequence of blank lines as a delimiter. """

    def __init__(self, split=True):
        patterns = r"s*\n\s*\n\s*"
        super().__init__(patterns, split=True)


class TetunSimpleTokenizer(TetunRegexTokenizer):
    """ Tokenize strings and numbers and ignore punctuations and special characters. """

    def __init__(self):
        patterns = (
            r"[A-Za-záéíóúñ]+(?:[-’'][A-Za-záéíóúñ]+)*"
            r"|"
            r"[\d.]+"
        )
        super().__init__(patterns)


if __name__ == '__main__':
    sample_text = """Macadique, 22 Novembru 2021 - MdF liuhosi kompañia AMOR, iha segunda (22/11) ne’e 
    ofisializa programa "HABURAS" ho montante inisiál $23.000,00. 
    Nune'e progama ne'e sei sai programa ida-ne'ebé di'ak liu ba joven sira iha ne'ebá."""

    sample_text_lower = sample_text.lower()

    print(
        f"\nEXAMPLES:\n========\n1) Standard tokenizer:\n {TetunStandardTokenizer().tokenize(sample_text)} \n")
    print(
        f"\nEXAMPLES (lowercase):\n========\n2) White Space tokenizer:\n {TetunWhiteSpaceTokenizer().tokenize(sample_text_lower)} \n")
    print(
        f"\nEXAMPLES (lowercase):\n========\n3) Blank tokenizer:\n {TetunBlankLineTokenizer().tokenize(sample_text_lower)} \n")
    print(
        f"4) Basic tokenizer (lowercase):\n {TetunSimpleTokenizer().tokenize(sample_text_lower)}")
