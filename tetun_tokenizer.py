import re
from typing import List
from config import tetun_patterns


class TetunRegexTokenizer:
    """ The base tokenizer class. """

    def __init__(self, patterns: str, split: bool = False) -> None:
        """
        :param patterns: regular expression patterns to match the tokens.
        :param split: if True, use re.split() to tokenize text, else use re.findall().            
        """
        self.patterns = patterns
        self.split = split

    def tokenize(self, text: str) -> List[str]:
        """ 
        :param text: the text to be tokenized.
        :return: a list of tokens.
        """
        if self.split:
            tokens = re.split(self.patterns, text)
        else:
            tokens = re.findall(self.patterns, text)
        return tokens


class TetunStandardTokenizer(TetunRegexTokenizer):
    """ Tokenize text by word, punctuations, symbols, or special characters delimiters. """

    def __init__(self) -> None:
        patterns = f"{tetun_patterns.TETUN_TEXT_PATTERN}|{tetun_patterns.DIGITS_PATTERN}|{tetun_patterns.PUNCTUATIONS_SYMBOLS_PATTERN}"
        super().__init__(patterns)


class TetunSentenceTokenizer(TetunRegexTokenizer):
    """ Tokenize text by .?! delimiters. """

    def __init__(self) -> None:
        patterns = f"{tetun_patterns.SENTENCE_DELIMITER_PATTERN}"
        super().__init__(patterns, split=True)


class TetunBlankLineTokenizer(TetunRegexTokenizer):
    """ Tokenize a text, treating any sequence of blank lines as a delimiter. """

    def __init__(self) -> None:
        patterns = f"{tetun_patterns.SEQUENCE_BLANKLINES_PATTERN}"
        super().__init__(patterns, split=True)


class TetunSimpleTokenizer(TetunRegexTokenizer):
    """ Tokenize strings and numbers and ignore punctuations and special characters. """

    def __init__(self) -> None:
        patterns = f"{tetun_patterns.TETUN_TEXT_PATTERN}|{tetun_patterns.DIGITS_PATTERN}"
        super().__init__(patterns)


class TetunWordTokenizer(TetunRegexTokenizer):
    """ Tokenize strings and ignore numbers, punctuations and special characters. """

    def __init__(self) -> None:
        patterns = f"{tetun_patterns.TETUN_TEXT_PATTERN}"
        super().__init__(patterns)
