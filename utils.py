import json
import os
import re


def read_latex() -> str:
    texts = []
    for fn in os.listdir("data"):
        if fn.endswith(".tex"):
            with open(os.path.join("data", fn), "r", encoding="utf-8") as f:
                text = ""
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    idx = [i for i, c in enumerate(line) if c == "%"]
                    for i in idx:
                        if i == 0 or line[i - 1] != "\\":
                            line = line[:i].strip()
                            break
                    text += line + "\n"
                texts.append(text)
    content = "\n".join(texts)
    content = re.sub(r'\n+', '\n\n', content).strip()
    return content


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
