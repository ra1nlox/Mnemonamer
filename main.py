from wonderwords import RandomWord
import click
import os
import re


def generate_new_file_name(size):
    generator = RandomWord()
    new_file_name = ""
    for i in range(size):
        word = generator.word(include_categories=["adjective", "noun", "verb"])
        if i == size - 1:
            new_file_name += f"{word}"
        else:
            new_file_name += f"{word}-"

    return new_file_name


@click.command()
@click.option(
    "--word-count",
    "-wc",
    "words_count",
    required=False,
    default=6,
    help="How many words will generate for a filename",
)
@click.argument("path")
def main(path: str, words_count: int):
    print(
        "WARNING! THIS ACTION CAN BE DESTRUCTIVE. IT WILL RENAME ALL FILES IN THE SPECIFIED DIRECTORY. MAKE SURE YOU'RE IN THE RIGHT DIRECTORY AND IT WON'T AFFECT THE FILES YOU DON'T WANT TO RENAME."
    )
    print("")
    ip = input("Confirm? (y/N): ")
    if ip.lower() != "y":
        return
    file_list = os.listdir(path)
    for item in file_list:
        if re.fullmatch("[A-Za-z]+(?:-[A-Za-z]+)*[.][A-Za-z0-9]+", item):
            print(f"Already renamed, avoiding changing the name: {item}")
            continue
        name, ext = os.path.splitext(item)
        abspath = os.path.join(os.path.abspath(item).strip(item), path.strip("./"))
        if not os.path.isfile(os.path.join(abspath, item)):
            print("Not a file, skipping")
            continue
        new_name = generate_new_file_name(words_count) + ext

        os.rename(os.path.join(abspath, item), os.path.join(abspath, new_name))
        print(f"Renamed {item} -> {new_name}")


if __name__ == "__main__":
    main()
