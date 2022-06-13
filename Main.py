# Project Qualitron
# Reading specific format of the Qualitron Machine
# June 13 2022

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
import os
import datetime
from functions.select_files import *

import pandas as pd
import numpy as np

# ----------------------------------------------------------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------------------------------------------------------


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

