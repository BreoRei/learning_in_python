from os import path as pth
NAME_FILE = 'INFO.md'


def print_txt(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'''
        путь до файла:    {result[0]}
        имя файла:        {result[1]}
        расширение файла: {result[2]}''')
        return result
    return wrapper


@print_txt
def get_path(data=NAME_FILE):
    path_ = pth.abspath(data)
    file_name = pth.basename(path_)
    index_name = path_.index(file_name)
    path_file = path_[:index_name]
    name, extension = file_name.split('.')
    return path_file, name, extension


if __name__ == '__main__':
    path_tuple = get_path()

