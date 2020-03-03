import imp
import os
import fnmatch


def load_from_folder(path_relative_to_shc_root):
    if path_relative_to_shc_root[0] != "/":
        path_relative_to_shc_root = "/" + path_relative_to_shc_root
    if path_relative_to_shc_root[-1:] != "/":
        path_relative_to_shc_root = path_relative_to_shc_root + "/"
    
    root_path = os.getcwd() + path_relative_to_shc_root
    pattern = '*.py'

    not_sorted_item_list = {}

    for root, dirs, files in os.walk(root_path):
        for filename in fnmatch.filter(files, pattern):
            file_path = os.path.join(root, filename)

            # don't load up any of the templates
            if fnmatch.fnmatch(filename, '*template.py') or fnmatch.fnmatch(filename, '*abstract.py') or fnmatch.fnmatch(filename, '__init__.py'):
                continue

            # extract just the item name from the full path
            item_name = file_path.split(root_path)[-1][0:-3]

            not_sorted_item_list[item_name] = imp.load_source(
                item_name, file_path)
    return not_sorted_item_list

def load_from_folder_and_sort(folder, sort=True):
    not_sorted_input_list = load_from_folder(folder)
    sorted_input_list = {}
    if sort:
        for key in sorted(not_sorted_input_list):
            sorted_input_list[key] = not_sorted_input_list[key]
        return sorted_input_list
    else:
        return not_sorted_input_list

def load_input(sort=True):
    return load_from_folder_and_sort("/shc_input/", sort)

def load_filter(sort=True):
    return load_from_folder_and_sort("/shc_filter/", sort)

def load_mask(sort=True):
    return load_from_folder_and_sort("/phases/masks/", sort)