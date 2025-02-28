from pathlib import Path
import tetun_tokenizer

# Define file paths
INPUT_TEXT = Path("data/input.txt")
HUMAN_TOKENS = Path("data/human_tokens.txt")

# Initialize tokenizer (modify as needed for evaluation)
TOKENIZER = tetun_tokenizer.TetunStandardTokenizer()
