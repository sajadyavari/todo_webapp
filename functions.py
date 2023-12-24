file_path="list.txt"
def get_lists(filepath=file_path):
    with open(filepath, 'r') as file_local:
        lists_local = file_local.readlines()
    return lists_local


def write_lists(doing,filepath=file_path):
    with open(filepath, 'w') as file_local:
        file_local.writelines(doing)

