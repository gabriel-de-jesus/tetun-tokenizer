# Tetun Tokenizer

## Description
Tetun tokenizer is a set of rule-based tokenization techniques for Tetun, where some techniques are devised specifically for Tetun based on the established Tetun INL standard and others are derived from commonly used tokenization rules.


## Main Features
- [ ] _Standard tokenizer:_ This tokenizer segments the input text into individual tokens based on word boundaries, punctuation, and special characters.
- [ ] _Simple tokenizer:_ It extracts only strings and numbers from the input text while discarding punctuations and special characters.
- [ ] _Word tokenizer:_ This tokenizer extracts word units from the input text, excluding numbers, punctuation, and special characters.
- [ ] _Sentence tokenizer:_ It splits sentences using ending delimiters such as periods (.), question marks (?), and exclamation marks (!). Titles represented by periods, such as Dr. and Ph.D., are preserved.
- [ ] _Blank line tokenizer:_ This tokenizer segments the input text based on the presence of blank lines.


## Installation

You can install the Tetun tokenizer via pip:

```
pip install tetun-tokenizer

```

Clone source code:

```
git clone https://github.com/gabriel-de-jesus/tetun-tokenizer.git

```


## Usage

To utilize the Tetun tokenizer, simply import the desired tokenizer feature/class from the `tokenizer` module within the Tetun tokenizer package. Here are some examples demonstrating its usage:

1. Utilizing  `TetunStandardTokenizer` to tokenize the input text.

```python
from tetuntokenizer.tokenizer import TetunStandardTokenizer

# Instantiate TetunStandardTokenizer
tetun_tokenizer = TetunStandardTokenizer()

# Input text
text = "Ha'u mak ita-nia maluk di'ak. Ha'u iha $0.25 atu fó ba ita."

# Tokenize the text
output = tetun_tokenizer.tokenize(text)

# Print the output
print(output)
```

Expected output:

```
["Ha'u", 'mak', 'ita-nia', 'maluk', "di'ak", '.', "Ha'u", 'iha', '$', '0.25', 'atu', 'fó', 'ba', 'ita', '.']
```

2. Using `TetunSentenceTokenizer` to tokenize the input text.

```python
from tetuntokenizer.tokenizer import TetunSentenceTokenizer

tetun_tokenizer = TetunSentenceTokenizer()

text = "Ha'u ema-ida ne'ebé baibain de'it. Tebes ga? Ita-nia maluk Dr. ka Ph.D sira hosi U.S.A mós dehan!"
output = tetun_tokenizer.tokenize(text)
print(output)
```

Expected output:

```
["Ha'u ema-ida ne'ebé baibain de'it.", 'Tebes ga?', 'Ita-nia maluk Dr. ka Ph.D sira hosi U.S.A mós dehan!']
```

3. Utilizing `TetunBlankLineTokenizer` to tokenize the input text.

```python
from tetuntokenizer.tokenizer import TetunBlankLineTokenizer

tetun_tokenizer = TetunBlankLineTokenizer()

text = """
        Ha'u mak ita-nia maluk di'ak.
        Ha'u iha $0.25 atu fó ba ita.
        """
output = tetun_tokenizer.tokenize(text)
print(output)
```

Expected output:

```
["\n            Ha'u mak ita-nia maluk di'ak.\n            Ha'u iha $0.25 atu fó ba ita.\n            "]
```

4. Using `TetunSimpleTokenizer` to tokenize a given text.

```python
from tetuntokenizer.tokenizer import TetunSimpleTokenizer

tetun_tokenizer = TetunSimpleTokenizer()

text = "Ha'u mak ita-nia maluk di'ak. Ha'u iha $0.25 atu fó ba ita."
output = tetun_tokenizer.tokenize(text)
print(output)
```

Expected output:

```
["Ha'u", 'mak', 'ita-nia', 'maluk', "di'ak", "Ha'u", 'iha', '0.25', 'atu', 'fó', 'ba', 'ita']
```

5. Using `TetunWordTokenizer` to tokenize the input text.

```python
from tetuntokenizer.tokenizer import TetunWordTokenizer

tetun_tokenizer = TetunWordTokenizer()

text = "Ha'u mak ita-nia maluk di'ak. Ha'u iha $0.25 atu fó ba ita."
output = tetun_tokenizer.tokenize(text)
print(output)
```

Expected output:

```
["Ha'u", 'mak', 'ita-nia', 'maluk', "di'ak", "Ha'u", 'iha', 'atu', 'fó', 'ba', 'ita']
```

You can also use the tokenizer to tokenize a text from a file. Below is an example:

```python
# Assume that we use Path instead of a string for the file path
from pathlib import Path
from tetuntokenizer.tokenizer import TetunSimpleTokenizer


file_path = Path("myfile/example.txt")

try:
    with file_path.open('r', encoding='utf-8') as f:
    contents = [line.strip() for line in f]
except FileNotFoundError:
    print(f"File not found at: {file_path}")

# You can also lowercase the contents before tokenizing them.
lowercase_contents = contents.lower()

tetun_tokenizer = TetunSimpleTokenizer()

output = '\n'.join(tetun_tokenizer.tokenize(str(lowercase_contents)))
print(output)

```

This is the example of the output:

```
ha'u
orgullu
dezenvolve
ha'u-nia
lian
tetun 
...
```

## Citation
If you use this repository or any of its contents for your research, academic work, or publication, we kindly request that you cite it as follows:

````
@misc{jesus-nunes-2024,
  author       = {Gabriel de Jesus and Sérgio Nunes},
  title        = {Data Collection Pipeline for Low-Resource Languages: A Case Study on Constructing a Tetun Text Corpus},
  year         = {2024},
  note         = {Accepted at LREC-COOLING, 2024},
}
````


## Acknowledgement
This work is financed by National Funds through the Portuguese funding agency, FCT - Fundação para a Ciência e a Tecnologia under the PhD scholarship grant number SFRH/BD/151437/2021.


## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/gabriel-de-jesus/tetun-tokenizer/blob/main/LICENSE)


## Contact Information
If you have any questions, feedback, or concerns regarding the corpus, please feel free to contact mestregabrieldejesus[at]gmail.com.
