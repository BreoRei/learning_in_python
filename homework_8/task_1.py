import os
import json
import csv
import pickle


def save_json_file(data: list[dict[str, str]], name_file: str) -> None:
    with open(f'{name_file}.json', "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)


def save_csv_file(data: list[dict[str, str]], name_file: str, fieldnames: list[str]) -> None:
    with open(f'{name_file}.csv', "w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def save_pickle_file(data: list[dict[str, str]], name_file: str) -> None:
    with open(f'{name_file}.pickle', "wb") as pickle_file:
        pickle.dump(data, pickle_file)


def get_directory_size(directory: str) -> int:
    total_size = 0
    for dir_path, dir_names, file_names in os.walk(directory):
        for file in file_names:
            fp = os.path.join(dir_path, file)
            total_size += os.path.getsize(fp)
    return total_size


def traverse_directory(directory: str) -> list:
    results = []

    for root, dirs, files in os.walk(directory):

        *_, root_parent, root_name = root.split('/')
        result = {
            "name" : "root-directory",
            "size": get_directory_size(root)
        }
        results.append(result)

        for dir_ in dirs:
            dir_paths = os.path.join(root, dir_)
            dir_size = get_directory_size(dir_paths)
            dir_path = dir_paths.split('/')[-2]

            result = {
                "name": dir_,
                "parent": dir_path,
                "type": "directory",
                "size": dir_size,
            }
            results.append(result)

        for file in files:
            file_paths = os.path.join(root, file)
            file_size = os.path.getsize(file_paths)
            file_path = file_paths.split('/')[-2]

            result = {
                "name": file,
                "parent": file_path,
                "type": "file",
                "size": file_size,
            }
            results.append(result)
    return results


if __name__ == '__main__':
    results = traverse_directory('/home/artem/Python/learning_in_python/homework_1')

    save_json_file(data=results, name_file='results')
    save_csv_file(data=results, name_file='results', fieldnames=results[0].keys())
    save_pickle_file(data=results, name_file='results')
