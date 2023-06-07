from pathlib import Path
from typing import List
import tetun_tokenizer

# File paths
INPUT_TEXT = Path("data/input.txt")
HUMAN_TOKENS = Path("data/human_tokens.txt")

# Tokenizer - adjust the technique to be evaluated accordingly
TOKENIZER = tetun_tokenizer.TetunStandardTokenizer()
