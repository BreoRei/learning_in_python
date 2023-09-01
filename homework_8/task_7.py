import csv
import pickle


def read_csv_file(name_file):
    with open(f'{name_file}.csv', "r") as csv_file:
        data = list(csv.reader(csv_file))
    return data


def print_pickle_string(data):
    pickle_string = pickle.dumps(data)
    print(pickle_string)


if __name__ == '__main__':
    result = read_csv_file('task_6')
    print_pickle_string(result)
