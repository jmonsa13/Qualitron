# Project Qualitron
# Reading specific format of the Qualitron Machine
# June 13, 2022

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
import os
import datetime
import pandas as pd

from functions.select_files import find_type_files, find_day_files, find_range_day_files

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# ----------------------------------------------------------------------------------------------------------------------
# SQL keys definition
# ----------------------------------------------------------------------------------------------------------------------
# Reading secrets
load_dotenv('./.env')

server = os.environ.get("SERVER")
database = os.environ.get("DATABASE")

table_calidad = os.environ.get("TABLE_CALIDAD")
table_defectos = os.environ.get("TABLE_DEFECTOS")

username = os.environ.get("USER_SQL")
password = os.environ.get("PASSWORD")

# ----------------------------------------------------------------------------------------------------------------------
# SQL connection definition
# ----------------------------------------------------------------------------------------------------------------------
# Connecting to the sql database
connection_str = "DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s" % (server, database, username, password)
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_str})

conn = create_engine(connection_url)
# ----------------------------------------------------------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------------------------------------------------------
def read_qualitron_files_product(source_dir, folder, planta, qualitron, type_file='PartialStat', info_date='range_test',
                                 day_filter_ini='20_05_2022', day_filter_fin='05_06_2022'):
    # Path
    format_path = os.path.join(source_dir, folder)

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

    for filename in files_filter:
        print(filename)

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

                            general_data.append([fecha, planta, qualitron, folder, tone, calidad_str, calidad_und])
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

                    general_data.append([fecha, planta, qualitron, folder, tone, calidad_str, calidad_und])

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
                        # Capture General defect
                        calidad_general = lines[j].split()[0]

                        # If there is a tab. Run loop internally to get specific defects
                        if lines[j + 1][0] == "\t":
                            # Initial variables
                            j += 1
                            flag_internal = True

                            while flag_internal is True:
                                # Capture Values
                                calidad_str = lines[j].split()[0]
                                calidad_und = int(lines[j].split()[-1].strip(')'))

                                # Saving the data
                                quality_data.append(
                                    [fecha, planta, qualitron, folder, calidad_type, calidad_general,
                                     calidad_str, calidad_und])

                                # Contador
                                j += 1

                                # Exit loop - Checking for a
                                if lines[j][0] != "\t":
                                    flag_internal = False
                                    j -= 1

                        # If there is not "tab" get de value and save the defect
                        else:
                            # Capture General defect value
                            calidad_str = "_"
                            calidad_und = int(lines[j].split()[-1].strip(')'))

                            # Saving the data
                            quality_data.append([fecha, planta, qualitron, folder, calidad_type, calidad_general,
                                                 calidad_str, calidad_und])

                        # Contador
                        j += 1
                        # Exit loop - Checking for empty line
                        if lines[j] == "\n":
                            flag = False
                i += 1
            else:
                break  # Exit the for loop

    return general_data, quality_data


# ----------------------------------------------------------------------------------------------------------------------
# Executing CODE
# ----------------------------------------------------------------------------------------------------------------------
def qualitron_main(day_filter_ini, day_filter_fin, filename):
    # Collecting the data
    # ------------------------------------------------------------------------------------------------------------------
    # Empty list
    general_qual = []
    quality_qual = []

    # Path of the main database
    database_dir = ".\\00_Master_database\\Qualitron_Ruta.xlsx"

    # Reading the souce database
    source_df = pd.read_excel(database_dir)

    # Keeping the row with connection
    source_df = source_df[source_df['Red'] == 'Si']

    # Looping to the different Qualitron by IP
    for index, row in source_df.iterrows():

        # Getting the planta and qualitron name
        planta = row['Planta']
        qualitron = row['Qualitron']

        # Debugging message
        print('------------------------------------------------------------------------------------------------------')
        print('------------------------------------------------------------------------------------------------------')
        print(planta)
        print(qualitron)

        # Folder inside the path
        source_dir = row['Ruta'] + ':\\Statistics'
        dirs = os.listdir(source_dir)

        # Collecting the quality data of each format inside the source folder
        for folder in dirs:
            # Debugging message
            print(folder)
            print('-----------------------------------------------')

            # Getting the info
            general, quality = read_qualitron_files_product(source_dir, folder, planta, qualitron,
                                                            type_file='PartialStat',
                                                            info_date='range_test', day_filter_ini=day_filter_ini,
                                                            day_filter_fin=day_filter_fin)
            # Joining the list
            general_qual += general
            quality_qual += quality


    # Pandas dataframe creation
    # ------------------------------------------------------------------------------------------------------------------
    # Columns name
    general_column = ['fecha', 'planta', 'qualitron', 'producto', 'tono', 'calidad', 'valor_unidad']
    quality_column = ['fecha', 'planta', 'qualitron', 'producto', 'calidad', 'defecto', 'defecto_especifico',
                      'valor_unidad']

    # Creation of the Dataframe with general quality data
    df = pd.DataFrame(general_qual, columns=general_column)

    # Creation of the Dataframe with quality data
    df_quality = pd.DataFrame(quality_qual, columns=quality_column)
    # ------------------------------------------------------------------------------------------------------------------
    # Export the dataframe to excel file
    # ------------------------------------------------------------------------------------------------------------------
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('.\\01_Resultados\\' + filename)

    # Write each dataframe to a different worksheet.
    df.to_excel(writer, sheet_name='General_Quality', index=False)
    df_quality.to_excel(writer, sheet_name='Defects', index=False)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

    # ------------------------------------------------------------------------------------------------------------------
    # Export the dataframe to json format
    # ------------------------------------------------------------------------------------------------------------------
    # df.to_json('.\\01_Resultados\\' + 'General_Quality.json', orient="records", lines=True)
    # df_quality.to_json('.\\01_Resultados\\' + 'Defects.json', orient="records", lines=True)

    # ------------------------------------------------------------------------------------------------------------------
    # Export the dataframe to csv format
    # ------------------------------------------------------------------------------------------------------------------
    # df.to_csv('.\\01_Resultados\\' + 'General_Quality.csv',  index=False)
    # df_quality.to_csv('.\\01_Resultados\\' + 'Defects.csv',  index=False)

    # ------------------------------------------------------------------------------------------------------------------
    # Export the dataframe to SQL DB
    # ------------------------------------------------------------------------------------------------------------------
    # print('Sending info to calidadGeneral')
    # df.to_sql(table_calidad, conn, if_exists='append', index=False)

    # print('Sending info to defectosGeneral')
    # df_quality.to_sql(table_defectos, conn, if_exists='append', index=False)

    # Range of data
    # info_date = 'range_test'  # 'range'
    # if info_date == 'day':
    #     day_filter_ini = '15_05_2022'
    # elif info_date == 'range':
    #     day_filter_fin = convert_date_format(datetime.date.today())
    #     day_filter_ini = convert_date_format(datetime.date.today() - datetime.timedelta(days=1))
    # elif info_date == 'range_test':
    #     day_filter_ini = '20_05_2022'
    #     day_filter_fin = '05_06_2022'

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print('Running the Qualitron data mining process')
    qualitron_main(day_filter_ini='10_01_2023', day_filter_fin='10_01_2023', filename='Qualitron_Enero_2023_10.xlsx')
