import json
import os


def read_latex() -> str:
    texts = []
    for fn in os.listdir("data"):
        if fn.endswith(".tex"):
            with open(os.path.join("data", fn), "r") as f:
                texts.append(f.read())
    return "\n".join(texts)


def get_abbreviations(text: str) -> dict:
    with open("abbreviations.json", "r") as f:
        ABBREVS = json.load(f)
    k = ""
    abbrevs = {}
    for c in text:
        if c.isupper():
            k += c
        else:
            if len(k) > 1:
                abbrevs[k] = ABBREVS.get(k, "")
            k = ""
    if len(k) > 1:
        abbrevs[k] = ABBREVS.get(k, "")
    return abbrevs


def print_abbreviations(abbrevs: dict) -> None:
    for k, v in sorted(abbrevs.items()):
        print(f"\\nomenclature{{{k}}}{{{v}}}")
