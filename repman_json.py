# Project Qualitron
# Exporting dataframe to repman json configuration
# February 02, 2023

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
from datetime import datetime


# ----------------------------------------------------------------------------------------------------------------------
# Json Structure for REPMAN
# ----------------------------------------------------------------------------------------------------------------------
def repman_json_calidad(df, filename, folder):
    """
    Function that create the json format that REPMAN need.
    Input:
        df = Pandas dataframe collected from the Qualitron
        filename = Filename
        folder = Folder path to export the *.jason
    Output:
        None
    """
    # Creating the file
    with open(folder + filename, 'w') as file:
        # --------------------------------------------------------------------------------------------------------------
        # Initial writing
        # --------------------------------------------------------------------------------------------------------------
        # Saving the header as variable
        fecha = datetime.timestamp(df.iloc[0]['fecha'])
        planta = df.iloc[0]["planta"]
        qualitron = df.iloc[0]["qualitron"]
        producto = df.iloc[0]["producto"]

        # Initial part of the row
        file.write(
            f'[{{\n"fecha":{fecha},\n"planta":"{planta}",\n"qualitron":"{qualitron}",\n"producto":"{producto}",\n')

        # Creating the header nested Header
        file.write(f'"cantidades":[\n')
        # --------------------------------------------------------------------------------------------------------------
        # Looping the df
        # --------------------------------------------------------------------------------------------------------------
        for index, row in df.iterrows():
            # Checking if the header was already writer
            if fecha == datetime.timestamp(row['fecha']) and planta == row["planta"] and qualitron == \
                    row['qualitron'] and producto == row['producto']:

                # Writing the nested data
                file.write(f'\t{{\n\t"tono":"{row["tono"]}",\n\t"calidad":"{row["calidad"]}",\n\t'
                           f'"valorUnd":{row["valor_unidad"]}}}')

                # Check if next row is different to avoid the trailing coma
                if index + 1 < len(df) and fecha == datetime.timestamp(df.iloc[index + 1]['fecha']) \
                        and planta == df.iloc[index + 1]["planta"] and qualitron == df.iloc[index + 1]['qualitron'] \
                        and producto == df.iloc[index + 1]['producto']:
                    # Add the coma
                    file.write(',\n')
            else:
                # Closing the Nested data
                file.write(f']\n')

                # Closing the row
                file.write(f'}},\n')

                # ------------------------------------------------------------------------------------------------------
                # Creating the header of the rows
                # ------------------------------------------------------------------------------------------------------
                # Saving the header as variable
                fecha = datetime.timestamp(row['fecha'])
                planta = row["planta"]
                qualitron = row["qualitron"]
                producto = row["producto"]

                # Initial part of the row
                file.write(
                    f'{{\n"fecha":{fecha},\n"planta":"{planta}",\n"qualitron":"{qualitron}",'
                    f'\n"producto":"{producto}",\n')

                # Creating the header nested data
                file.write(f'"cantidades":[\n')

                # Writing the nested data
                file.write(f'\t{{\n\t"tono":"{row["tono"]}",\n\t"calidad":"{row["calidad"]}",\n\t'
                           f'"valorUnd":{row["valor_unidad"]}}}')

                # Check if next row is different to avoid the trailing coma
                if index + 1 < len(df) and fecha == datetime.timestamp(df.iloc[index + 1]['fecha']) \
                        and planta == df.iloc[index + 1]["planta"] and qualitron == df.iloc[index + 1]['qualitron'] \
                        and producto == df.iloc[index + 1]['producto']:
                    # Add the coma
                    file.write(',\n')

        # Closing the json file
        file.write(f']\n')
        file.write(f'}}]')

    return None


def repman_json_defectos(df, filename, folder):
    """
    Function that create the json format that REPMAN need.
    Input:
        df = Pandas dataframe collected from the Qualitron
        filename = Filename
        folder = Folder path to export the *.jason
    Output:
        None
    """
    # Creating the file
    with open(folder + filename, 'w') as file:
        # --------------------------------------------------------------------------------------------------------------
        # Initial writing
        # --------------------------------------------------------------------------------------------------------------
        # Saving the header as variable
        fecha = datetime.timestamp(df.iloc[0]['fecha'])
        planta = df.iloc[0]["planta"]
        qualitron = df.iloc[0]["qualitron"]
        producto = df.iloc[0]["producto"]

        # Initial part of the row
        file.write(
            f'[{{\n"fecha":{fecha},\n"planta":"{planta}",\n"qualitron":"{qualitron}",\n"producto":"{producto}",\n')

        # Creating the header nested Header
        file.write(f'"cantidades":[\n')
        # --------------------------------------------------------------------------------------------------------------
        # Looping the df
        # --------------------------------------------------------------------------------------------------------------
        for index, row in df.iterrows():
            # Checking if the header was already writer
            if fecha == datetime.timestamp(row['fecha']) and planta == row["planta"] and qualitron == \
                    row['qualitron'] and producto == row['producto']:

                # Writing the nested data
                file.write(f'\t{{\n\t"calidad":"{row["calidad"]}",\n\t"defecto":"{row["defecto"]}",'
                           f'\n\t"defectoEspecifico":"{row["defecto_especifico"]}",\n\t'
                           f'"valorUnd":{row["valor_unidad"]}}}')

                # Check if next row is different to avoid the trailing coma
                if index + 1 < len(df) and fecha == datetime.timestamp(df.iloc[index + 1]['fecha']) \
                        and planta == df.iloc[index + 1]["planta"] and qualitron == df.iloc[index + 1]['qualitron'] \
                        and producto == df.iloc[index + 1]['producto']:
                    # Add the coma
                    file.write(',\n')
            else:
                # Closing the Nested data
                file.write(f']\n')

                # Closing the row
                file.write(f'}},\n')

                # ------------------------------------------------------------------------------------------------------
                # Creating the header of the rows
                # ------------------------------------------------------------------------------------------------------
                # Saving the header as variable
                fecha = datetime.timestamp(row['fecha'])
                planta = row["planta"]
                qualitron = row["qualitron"]
                producto = row["producto"]

                # Initial part of the row
                file.write(
                    f'{{\n"fecha":{fecha},\n"planta":"{planta}",\n"qualitron":"{qualitron}",'
                    f'\n"producto":"{producto}",\n')

                # Creating the header nested data
                file.write(f'"cantidades":[\n')

                # Writing the nested data
                file.write(f'\t{{\n\t"calidad":"{row["calidad"]}",\n\t"defecto":"{row["defecto"]}",'
                           f'\n\t"defectoEspecifico":"{row["defecto_especifico"]}",\n\t'
                           f'"valorUnd":{row["valor_unidad"]}}}')

                # Check if next row is different to avoid the trailing coma
                if index + 1 < len(df) and fecha == datetime.timestamp(df.iloc[index + 1]['fecha']) \
                        and planta == df.iloc[index + 1]["planta"] and qualitron == df.iloc[index + 1]['qualitron'] \
                        and producto == df.iloc[index + 1]['producto']:
                    # Add the coma
                    file.write(',\n')

        # Closing the json file
        file.write(f']\n')
        file.write(f'}}]')

    return None

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Main for testing the function
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# df = pd.read_excel('.\\01_Resultados\\Prestigio_Qualitron_Feb_2023.xlsx', sheet_name=0)
# repman_json_calidad(df, 'General_calidad.json', '.\\01_Resultados\\')
#
# df = pd.read_excel('.\\01_Resultados\\Prestigio_Qualitron_Feb_2023.xlsx', sheet_name=1)
# repman_json_defectos(df, 'General_defectos.json', '.\\01_Resultados\\')
