import glob
from typing import List
import nltk
import click
from nltk.tokenize import sent_tokenize, word_tokenize

def list_files(path: str) -> List[str]:
    return glob.glob(path)

def tokenize(in_str: str, max_len=1024) -> List[str]:
    nltk.download('punkt')
    return [" ".join(word_tokenize(t))[:max_len] for t in sent_tokenize(in_str)]


def prepare_mixture(local_input_dir: str, local_output_dir: str, max_token_string_len: int)-> List[str]:
    txt_files = list_files(local_input_dir)
    mixture = []
    for txt_file in txt_files:
        with open(txt_file) as f:
            mixture.__add__(tokenize(f.read()))
    return mixture



@click.command()
@click.argument('local-input-dir', type=click.Path(exists=True, dir_okay=True, file_okay=False))
@click.argument('local-output-dir', type=click.Path(exists=False, dir_okay=True, file_okay=False))
@click.option('--max-token-string-len', '-m', type=int, default=1024)
def main(local_output_dir, local_input_dir, max_token_string_len):
    prepare_mixture(local_output_dir, local_input_dir, max_token_string_len)

if __name__ == '__main__':
    main()
