import pandas as pd  # used for retrieving data from Excel
import os  # adjusts app based on Windows/Linux/Unix etc
import re  # regex
from styleframe import StyleFrame, Styler, utils
import openpyxl as xl

analyticsDirectory = '.\\DP2Z Analysis\\'

# os.chdir("\\tymx-fs-002v\restricted\DPC\DPCZ Career Field Teams")

os.chdir("c:\\users\\aiden\\onedrive\\desktop")


def console_loop():
    print("Welcome to the PAQ database entry TUI please select one of the following options and hit enter:")
    while True:
        print("A). Update PAQ database with SLRP data from the most current")
        usrSelect = input()
        if not re.match("[AaBbCc]", usrSelect):
            print("ERROR: Invalid option. Please Enter A Letter Corresponding to the menu and press enter")
        elif re.match("[Aa]", usrSelect):
            getCopySLRPReport(analyticsDirectory)


def getSLRPReport(path):
    try:
        for file_path in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_path)) and (re.search("SLRP", file_path)):
                SLRPReport = path + file_path
                break
    except FileNotFoundError:
        print(f"ERROR: SLRP report not found in location: {path}")
    except PermissionError:
        print(f"ERROR: Permission denied access to {path}")
    except OSError as e:
        print(f"ERROR: Issues with Operating System Compatibility: {e}")
    return SLRPReport


def getCopySLRPReport():
    path = analyticsDirectory
    SLRP_Report = pd.read_excel(getSLRPReport(path), "Incentives Summary")
    filtered_df = SLRP_Report[SLRP_Report["Org Struc Code"].str.contains("dpcpaq", case=False, na=False, regex=True)]
    filtered_df2 = filtered_df[
        filtered_df["Career Field"].str.contains("Scientist And Engineer", case=False, na=False, regex=True)]
    filtered_df = filtered_df.merge(filtered_df2)
    filter_RI = filtered_df[
        filtered_df["NOA1 Desc"].str.contains("Recruitment Incentive", case=False, na=False, regex=True)]
    filter_SLRP = filtered_df[
        filtered_df["NOA1 Desc"].str.contains("Student Loan Repayment", case=False, na=False, regex=True)]
    filter_RI = filter_RI[[
        'Employee Number', 'FY', 'Name Employee', 'Pay Plan', 'Series', 'Grade', 'Career Field',
        'STEM Series', 'MCO Series', 'MCO Risk Level',
        'Org Struc Code', 'Owning Cmd Id', 'Own Cmd', 'Own Cmd Desc', 'Unit',
        'Location', 'Record Status', 'PEC', 'PEC Desc', 'Incentive Type',
        '.Pay Period Ending Date', 'Nature of Action (HR).Effective Date',
        'NOA1', 'NOA1 Desc', 'Retention Incentive Pay Last PPE',
        'Retention Incentive Percent', 'Student Loan Repayment Amount',
        'Annual Amount']]
    filter_SLRP = filter_SLRP[[
        'Employee Number', 'FY', 'Name Employee', 'Pay Plan', 'Series', 'Grade', 'Career Field',
        'STEM Series', 'MCO Series', 'MCO Risk Level',
        'Org Struc Code', 'Owning Cmd Id', 'Own Cmd', 'Own Cmd Desc', 'Unit',
        'Location', 'Record Status', 'PEC', 'PEC Desc', 'Incentive Type',
        '.Pay Period Ending Date', 'Nature of Action (HR).Effective Date',
        'NOA1', 'NOA1 Desc', 'Retention Incentive Pay Last PPE',
        'Retention Incentive Percent', 'Student Loan Repayment Amount',
        'Annual Amount']]
    sf1 = StyleFrame(filter_RI, styler_obj=Styler(font_size=8))
    sf2 = StyleFrame(filter_SLRP, styler_obj=Styler(font_size=8))
    sf2.apply_headers_style(styler_obj=Styler(bold=True, bg_color=utils.colors.grey, font_size=8))
    sf1.apply_headers_style(styler_obj=Styler(bold=True, bg_color=utils.colors.grey, font_size=8))

    with pd.ExcelWriter(
            ".//DP2Z Analysis//temp.xlsx",
            mode="w",
            engine="openpyxl",
            # if_sheet_exists="overlay",
    ) as writer:
        sf1.to_excel(writer, sheet_name="Recruitment Incentive")
        sf2.to_excel(writer, sheet_name="Student Loan Repayment").close()
