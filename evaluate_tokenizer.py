from evaluation import Evaluation
from config import eval_config


class EvaluateTokenizer:
    """ This class runs evaluation module to evaluate the effectiveness of the tokenizer techniques. """

    def __init__(self) -> None:
        self.eval = Evaluation(
            eval_config.INPUT_TEXT,
            eval_config.HUMAN_TOKENS,
            eval_config.TOKENIZER
        )

    def run(self) -> None:
        self.eval.evaluate()


if __name__ == '__main__':
    evaluate = EvaluateTokenizer()
    evaluate.run()
