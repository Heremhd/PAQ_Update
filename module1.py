import pandas as pd #used for retrieving data from Excel
import tkinter as tk #used for making a std UI
import os #adjusts app based on Windows/Linux/Unix etc
import re #regex
from styleframe import StyleFrame
import openpyxl as xl

def getSLRPReport(path):

    try:
        for file_path in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_path)) and (re.search("SLRP", file_path)):
                SLRPReport = path+file_path
                break
    except FileNotFoundError:
        print(f"ERROR: SLRP report not found in location: {path}")
    except PermissionError:
        print(f"ERROR: Permission denied access to {path}")
    except OSError as e:
        print(f"ERROR: Issues with Operating System Compatibility: {e}")
    return SLRPReport

def getCopySLRPReport(path):
    SLRP_Report = StyleFrame.read_excel(getSLRPReport(path), "Incentives Summary")
    SLRP_copy = SLRP_Report

    # Get the header row from the original Excel file
    original_header_row = SLRP_Report.iloc[0]

    # Extract cell sizes from the header row

    # Apply header cell sizes to the target Excel file
    #for col, size in cell_sizes.items():
    #   SLRP_copy.set_column_width(columns=col, width=size)

    # Get header colors from the header row
    header_colors = {}
    for col in original_header_row.columns:
        cell_style = SLRP_Report.get_col_style(col)
        header_colors[col] = cell_style.fgColor if cell_style else None

    # Apply header colors to the target Excel file
    for col, color in header_colors.items():
        if color:
            SLRP_copy.apply_column_style(cols_to_style=col, styler_obj=StyleFrame.Style(fg_color=color))

    # Save the modified target Excel file
    SLRP_copy.to_excel(".\\DP2Z Analysis\\cum.xlsx").save()


