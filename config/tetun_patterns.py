import re


""" This file contains all the regular expressions for the Tetun tokenizer. """

# E.g.: Ataúru, ne'ebé, ida-ne'ebé, Ofisiál, etc.
TETUN_TEXT_PATTERN = r"[A-Za-zÂÁáãéêÉÊíÍóÓúÚñç]+(?:[-’'][A-Za-zÂÁáãéêÉÊíÍóÓúÚñç]+)*"

# E.g.: 20.000.000.000,45 or 20,000,000,000.45.
# E.g.; char ',' or '.' followed digits will be ignored.
DIGITS_PATTERN = r"\d+(?:[,.]\d+)*"

# These punctuations and symbols will be tokenized as a token in the Tetun standard tokenizer.
PUNCTUATIONS_SYMBOLS = '!,./:;?"“”()[\\]^_`{|}#&§©°$€£μ@*+÷%<=>«»~'
PUNCTUATIONS_SYMBOLS_PATTERN = r"[" + \
    re.escape("".join(PUNCTUATIONS_SYMBOLS)) + "]"

# The .?! chars are considered as sentence delimiter.
SENTENCE_DELIMITER_PATTERN = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s"

# One or more consecutive new lines.
SEQUENCE_BLANKLINES_PATTERN = r"s*\n\s*\n\s*"

# One or more consecutive spaces.
WHITESPACE_PATTERNS = r"\s+"
