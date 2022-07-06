# Project Qualitron
# Reading specific format of the Qualitron Machine
# June 13 2022

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
import os
import datetime
import pandas as pd

from functions.select_files import convert_date_format, find_type_files, find_day_files, find_range_day_files

# ----------------------------------------------------------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Variables Definition and Path
# ----------------------------------------------------------------------------------------------------------------------
# Path
source_dir = ".\\data_qualitron"
folder = 'Artik blanco'
format_path = os.path.join(source_dir, folder)

# Type of file
type_file = 'PartialStat'

# Range of data
info_date = 'range_test'  # 'range'
if info_date == 'day':
    day_filter_ini = '14_05_2022'
elif info_date == 'range':
    day_filter_fin = convert_date_format(datetime.date.today())
    day_filter_ini = convert_date_format(datetime.date.today() - datetime.timedelta(days=1))
elif info_date == 'range_test':
    day_filter_ini = '14_05_2022'
    day_filter_fin = '15_05_2022'

# Columns name
general_column = ['Fecha', 'Tono', 'Calidad', 'Valor_und']
quality_column = ['Fecha', 'Calidad', 'Defecto', 'Valor_und']

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

# TODO: Sort the files by date using their name information and create a df with 3 columns (filename, date(datetime),
#  info_group)

# Empty list
general_data = []
quality_data = []

# Row assign
row_data = 20

for filename in files_filter:
    # Flag to avoid capture general data
    flag_datos_gen = True

    # Filename path
    filename_path = os.path.join(format_path, filename)

    # Reading the lines of the files
    with open(filename_path, 'r', encoding="utf-16") as f:
        lines = f.readlines()

    # Capturing the date (last row)
    date_str = lines[-1].strip('SYSTEM').strip()
    fecha = datetime.datetime.strptime(date_str, '%d/%m/%Y, %H:%M:%S')

    # Initial position
    start_i = 10

    # Capturing the quality
    for i, line in enumerate(lines[start_i:]):
        # Checking for empty line
        if line != "\n":
            # Checking for quality data
            if line.split()[0] == 'Primera':
                if flag_datos_gen is False:
                    # Tone color
                    tone = lines[i + start_i - 2].split(' ')[0].strip()
                    # General Quality
                    for j in range(i + start_i, i + start_i + 5, 1):
                        # capture value
                        calidad_str = lines[j].split()[0]
                        calidad_und = int(lines[j].split()[-1])

                        general_data.append([fecha, tone, calidad_str, calidad_und])
                elif flag_datos_gen is True:
                    flag_datos_gen = False

        # Capturing the 3 last format
        elif line == "\n":
            # B. Perdidas
            tone = lines[i + start_i + 3].split()[0]
            # Capturing the two last values
            for j in range(i + start_i + 4, i + start_i + 6, 1):
                # capture value
                calidad_str = " ".join(lines[j].split()[0:2])
                calidad_und = int(lines[j].split()[-1])

                general_data.append([fecha, tone, calidad_str, calidad_und])

            new_start_i = i + start_i + 13
            break  # Exit the for loop

    # Capturing the desclasamiento
    i = new_start_i
    for line in lines[new_start_i:]:
        # Checking for a line that start with =
        if line[0] != '=':
            # Checking for the initial line of the quality desclasamiento
            if line[0] == '-' and lines[i + 1].split()[0] in ['Segunda', 'Tercera', 'Cuarta', 'Descarte']:
                # Calidad type
                calidad_type = lines[i + 1].split(' ')[0].strip()

                # Initial variables
                j = i + 3
                flag = True
                while flag is True:
                    # capture value
                    calidad_str = lines[j].split()[0]
                    calidad_und = int(lines[j].split()[-1].strip(')'))

                    # Saving the data
                    quality_data.append([fecha, calidad_type, calidad_str, calidad_und])

                    # Contador
                    j += 1
                    # Exit loop - Checking for empty line
                    if lines[j] == "\n":
                        flag = False
            i += 1
        else:
            break  # Exit the for loop

# ----------------------------------------------------------------------------------------------------------------------
# Pandas dataframe creation
# ----------------------------------------------------------------------------------------------------------------------
# Creation of the Dataframe with general quality data
df = pd.DataFrame(general_data, columns=general_column)

# Creation of the Dataframe with quality data
df_quality = pd.DataFrame(quality_data, columns=general_column)
# ----------------------------------------------------------------------------------------------------------------------
# Export the dataframe to excel file
# ----------------------------------------------------------------------------------------------------------------------
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(f'Qualitron_Quality_{folder}.xlsx')

# Write each dataframe to a different worksheet.
df.to_excel(writer, sheet_name='General_Quality', index=False)
df_quality.to_excel(writer, sheet_name='Defects', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()


# df.to_excel('General_quality.xlsx', index=False)
# df_quality.to_excel('Quality_type.xlsx', index=False)
# ----------------------------------------------------------------------------------------------------------------------
# Executing CODE
# ----------------------------------------------------------------------------------------------------------------------
def qualitron_main():
    print('Hola')


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print('Running the Qualitron data mining process')
    qualitron_main()
