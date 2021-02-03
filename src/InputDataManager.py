#!/usr/bin/python3
from os.path import isfile, join
import os
from os import listdir


class InputDataManager:
    def __init__(self):
        pass

    def get_data(self, file_path):
        """
        Extract data from file.
        """
        all_data = []
        with open(file_path, 'r') as f:
            data = f.read()
            all_data.append(data)    
        
        return all_data


    def get_all_filenames(self, data_directory_path):
        """
        Get a list of all file names in the directory.
        """
        all_filenames = [f for f in listdir(
            data_directory_path) if isfile(join(data_directory_path, f))]

        return all_filenames