from evaluation import Evaluation
from config import eval_config


class EvaluateTokenizer:
    """ This class run evaluaion module to evaluate each of the tokenizer techniques effectiveness. """

    def __init__(self) -> None:
        self.eval = Evaluation(eval_config.INPUT_TEXT,
                               eval_config.HUMAN_TOKENS, eval_config.TOKENIZER)

    def run(self) -> None:
        self.eval.evaluate()


if __name__ == '__main__':
    example = EvaluateTokenizer()
    example.run()
