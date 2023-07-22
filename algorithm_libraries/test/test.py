import argparse
import glob
import os
import subprocess
from typing import List

import pandas as pd
import yaml

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("--lang", type=str, default="python")
parser.add_argument("--filepath", type=str, default="misc/sample")

args = parser.parse_args()
extension = {"python": "py", "rust": "rs", "cpp": "cpp"}[args.lang]

markdown_template = f"# Libraries for {args.lang}"

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
    elif language == "cpp":
        return ["g++", "-std=c++17", "-o", "a.out", get_excution_file(language, filepath), "&&", "./a.out"]


def find_status_file(language: str) -> None:
    status_file_path = f"{os.getcwd()}/algorithm_libraries/{language}/status.yml"
    obj = {"categories": []}
    if os.path.exists(status_file_path):
        with open(status_file_path) as file:
            obj = yaml.safe_load(file)
    files = glob.glob(f"{os.getcwd()}/algorithm_libraries/{language}/**/*.{extension}")

    for file in files:
        category_name = file.split("/")[-2]
        feature_name = file.split("/")[-1].split(".")[0]
        if category_name not in [x["name"] for x in obj["categories"]]:
            obj["categories"].append({"name": category_name, "features": []})
        category = [x for x in obj["categories"] if x["name"] == category_name][0]
        if feature_name not in [x["name"] for x in category["features"]]:
            category["features"].append({"name": feature_name, "status": "unknown"})
    with open(status_file_path, "w") as file:
        yaml.dump(obj, file)


def write_readme(language: str):
    md_file_path = f"{os.getcwd()}/algorithm_libraries/{language}/README.md"
    status_file_path = f"{os.getcwd()}/algorithm_libraries/{language}/status.yml"
    data = []
    # statusの読み込みor作成

    with open(status_file_path) as file:
        obj = yaml.safe_load(file)
        for category in obj["categories"]:
            category_name = category["name"]
            for feature in category["features"]:
                if feature["status"] == "ok":
                    data.append([category_name, feature["name"], "✅"])
                elif feature["status"] == "unknown":
                    data.append([category_name, feature["name"], "❓"])
                else:
                    data.append([category_name, feature["name"], "❌"])
        df = pd.DataFrame(data, columns=["category", "feature", "status"])
        text = markdown_template + df.to_markdown(index=False)

    with open(md_file_path, "w") as file:
        file.write(text)


def update_status_file(language: str, filepath: str, status: str):
    status_file_path = f"{os.getcwd()}/algorithm_libraries/{language}/status.yml"
    obj = {"categories": []}
    if os.path.exists(status_file_path):
        with open(status_file_path) as file:
            obj = yaml.safe_load(file)
    category_name = filepath.split("/")[-2]
    feature_name = filepath.split("/")[-1].split(".")[0]
    caterogies = []
    for category in obj["categories"]:
        if category["name"] != category_name:
            caterogies.append(category)
            continue

        c = []
        for feature in category["features"]:
            if feature["name"] == feature_name:
                feature["status"] = status
            c.append(feature)
        caterogies.append({"name": category["name"], "features": c})
    obj["categories"] = caterogies
    with open(status_file_path, "w") as file:
        yaml.dump(obj, file)


if __name__ == "__main__":
    find_status_file(args.lang)
    for file in glob.glob(
        f"{os.getcwd()}/algorithm_libraries/{args.lang}/**/*.{extension}"
    ):
        category_name = file.split("/")[-2]
        feature_name = file.split("/")[-1].split(".")[0]
        filepath = f"{category_name}/{feature_name}"
        try:
            with open(get_test_yml(filepath)) as file:
                obj = yaml.safe_load(file)
                cmd = get_command(args.lang, filepath)
                for x in obj["cases"]:
                    input_text = x["in"].rstrip().encode()
                    ans_text = x["out"].rstrip().encode()
                    output_text = subprocess.Popen(
                        cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE
                    ).communicate(input_text)[0]
                    output_text = output_text.rstrip()
                    try:
                        assert (
                            ans_text == output_text
                        ), f"input: {input_text}\n ans: {ans_text}\n output: {output_text}"
                        update_status_file(args.lang, filepath, "ok")
                    except:
                        update_status_file(args.lang, filepath, "ng")
                        raise
        except:
            print(f"skip {filepath}")
    write_readme(args.lang)
