from task_1 import save_csv_file, save_pickle_file
import pickle
import json


def json_to_pickle(name_file):
    with open(f'{name_file}.json', 'r', encoding='utf-8') as file_json:
        data = json.load(file_json)
        save_pickle_file(data=data, name_file=f'task_6.pickle')


def pickle_to_csv(name_file):
    with open(f'{name_file}.pickle', 'rb') as file_pickle:
        data = pickle.load(file_pickle)
        keys = data[0].keys()
        save_csv_file(data=data, name_file=f'{name_file}.csv', fieldnames=keys)


if __name__ == '__main__':
    pickle_to_csv('task_6')
