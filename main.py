# Project Qualitron
# Reading specific format of the Qualitron Machine
# June 13 2022

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
import os
import re
import datetime
from itertools import chain


import pandas as pd
import numpy as np


# ----------------------------------------------------------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------------------------------------------------------
def convert_date_format(date):
    """
    This function convert a datetime format date in a string format
    :param date: Date in datetime format
    :return: A string in the followinf way  day_month_year. EX: 16_05_2022
    """

    date_convert = date.strftime('%d') + '_' + date.strftime('%m') + '_' + date.strftime('%Y')

    return date_convert


def find_type_files(product_path, type_var='PartialStat'):
    """
    This function filter the files by their common format ('PartialStat', 'GlobalStat', 'GroupStat')
    :param product_path: str, indicating the path of the folder where the files are located
    :param type_var: str, the type of formato to filter between 'PartialStat', 'GlobalStat', 'GroupStat'
    :return type_list: A list containing only the files that correspond to the specified filter
    """
    # Empty list
    type_list = []

    # Filtering by file type
    for path, _, files in os.walk(product_path):
        for file_elem in files:
            if type_var in file_elem:
                type_list.append(file_elem)

    return type_list


def find_day_files(files_list, day):
    """
    This function filter the files that where taken in a specific date using the information located in their name.
    :param files_list: A list of multiple files.
    :param day: The day in str format. Indicate the day used for the filter (15_05_2022).
    :return files_filter_day: A list containing only the files that correspond to the specified date.
    """
    # Empty list
    files_filter_day = []

    # Filtering by day in the name of the file
    for file_elem in files_list:
        if day in file_elem:
            files_filter_day.append(file_elem)

    return files_filter_day


def find_range_day_files(files_list, day_ini, day_fin):
    """
    This function filter the files that where taken in a specific period of time using the information located in their
     name.
    :param files_list: A list of multiple files
    :param day_ini: The initial day in str format (15_05_2022).
    :param day_fin: The final day in str format ( 18_06_2022).
    :return files_filter_range: A list containing only the files that correspond to these specified period of time
    """
    # Empty list
    aux_list = []
    # Converting to datetime format
    ini_d = datetime.datetime.strptime(day_ini, '%d_%m_%Y').date()
    fin_d = datetime.datetime.strptime(day_fin, '%d_%m_%Y').date()

    while ini_d <= fin_d:
        # Filtering the range of files
        aux_list.append(find_day_files(files_list, convert_date_format(ini_d)))
        # Move forward one day
        ini_d = ini_d + datetime.timedelta(days=1)

    # Chaining everything in one list
    files_filter_range = list(chain(*aux_list))

    return files_filter_range


# ----------------------------------------------------------------------------------------------------------------------
# Variables Definition and Path
# ----------------------------------------------------------------------------------------------------------------------
# Path
source_dir = ".\\data_qualitron"
format_path = os.path.join(source_dir, 'Artik blanco')

# Type of file
type_file = 'PartialStat'

# Range of data
info_date = 'day'  # 'range'
if info_date == 'day':
    day_filter_ini = '14_05_2022'
elif info_date == 'range':
    day_filter_fin = convert_date_format(datetime.date.today())
    day_filter_ini = convert_date_format(datetime.date.today() - datetime.timedelta(days=1))
elif info_date == 'range_test':
    day_filter_ini = '14_05_2022'
    day_filter_fin = '15_05_2022'

# ----------------------------------------------------------------------------------------------------------------------
# Main Code
# ----------------------------------------------------------------------------------------------------------------------
# Filtering by file type
type_files = find_type_files(format_path, type_file)

# Filtering by info range
if info_date == 'day':
    files_filter = find_day_files(type_files, day_filter_ini)
elif info_date == 'range_test':
    files_filter = find_range_day_files(type_files, day_filter_ini, day_filter_fin)


for file in files_filter:
    print(file)


# ----------------------------------------------------------------------------------------------------------------------
# Executing CODE
# ----------------------------------------------------------------------------------------------------------------------
def qualitron_main():
    print('Hola')




# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print('Running the Qualitron data mining process')
    qualitron_main()

