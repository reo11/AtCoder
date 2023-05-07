import argparse
import os
import yaml
import subprocess
import markdown
import pandas as pd
from typing import List

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--lang', type=str, default="python")
parser.add_argument('--filepath', type=str, default="misc/sample")

args = parser.parse_args()
extension = {"python": "py", "rust": "rs", "cpp": "cpp"}[args.lang]

markdown_template = f"""
# Libraries for {args.lang}

"""

def get_test_yml(filepath: str) -> List[str]:
    path = f"{os.getcwd()}/algorithm_libraries/test/{filepath}.yml"
    assert os.path.exists(path), f"file not found: {path}"
    return path

def get_excution_file(language: str, filepath: str) -> List[str]:
    path = f"{os.getcwd()}/algorithm_libraries/{language}/{filepath}.{extension}"
    assert os.path.exists(path), f"file not found: {path}"
    return path

def get_command(language: str, filepath: str) -> List[str]:
    target_languages = ["python"]
    assert language in target_languages, f"language must be in {target_languages}"

    if language == "python":
        return ["python3", get_excution_file(language, filepath)]

def write_readme(language: str):
    md_file_path = f"{os.getcwd()}/algorithm_libraries/{language}/README.md"
    status_file_path = f"{os.getcwd()}/algorithm_libraries/{language}/status.yml"
    data = []
    with open(status_file_path) as file:
        obj = yaml.safe_load(file)
        for category in obj["categories"]:
            category_name = category["name"]
            for feature in category["features"]:
                if feature["status"] == "ok":
                    data.append([category_name, feature["name"], "✅"])
                else:
                    data.append([category_name, feature["name"], "❌"])
        df = pd.DataFrame(data, columns=["category", "feature", "status"])
        text = markdown_template + df.to_markdown()

    with open(md_file_path, 'w') as file:
        file.write(text)


if __name__ == "__main__":
    with open(get_test_yml(args.filepath)) as file:
        obj = yaml.safe_load(file)
        cmd = get_command(args.lang, args.filepath)
        for x in obj["cases"]:
            input_text = x["in"].rstrip().encode()
            ans_text = x["out"].rstrip().encode()
            output_text = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate(input_text)[0]
            output_text = output_text.rstrip()
            assert ans_text == output_text, f"input: {input_text}\n ans: {ans_text}\n output: {output_text}"
    write_readme(args.lang)