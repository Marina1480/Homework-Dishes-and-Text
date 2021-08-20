import os
import time

files_path = os.path.join(os.getcwd(), "1file.txt")
print(files_path)


def read_sort_and_write_file(path):
    files_list = ["1file.txt", "2file.txt", "3file.txt"]
    res_dict = {}

    for file_t in files_list:
        new_list = []
        with open(file_t, 'r', encoding='utf-8') as file:
            new_list.append(file_t)
            new_list.append(file.read())
        with open(file_t, 'r', encoding='utf-8') as file:
            res_dict[len(file.readlines())] = new_list

    sorted_dict = {}
    sorted_keys = list(res_dict.keys())
    sorted_keys.sort()
    for key in sorted_keys:
        sorted_dict[key] = res_dict[key]
    print(sorted_dict)

    with open("Final.txt", 'w', encoding='utf-8') as file:
        for id, val in enumerate(sorted_dict):
            file.writelines(f'{list(sorted_dict.values())[id][0]}' + '\n')
            file.writelines(f'{str(list(sorted_dict.keys())[id])}' + '\n')
            file.writelines(f'{list(sorted_dict.values())[id][1]}' + '\n')

    return


read_sort_and_write_file(files_path)
