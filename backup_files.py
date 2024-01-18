from slrp_module import *
from tkinter import messagebox
import os


class Backup:

    def __init__(self, date, btype, path):
        self.date = date
        self.type = btype
        self.location = path

    def setBtype(self, loc2file: str) -> str:
        """
        :param loc2file: file path of file
        :return: string containing information of backup data
        """
        if os.path.isfile(loc2file):
            if re.match('SLRP', loc2file):
                return "Excel File for Student Loans and Recruitment Incentives"

    def setBdate(self, loc2file: str) -> str:
        """
        :param loc2file: filepath of file
        :return: string containing the date/time of backup and when last modified
        """
        if os.path.isfile(loc2file):
            dateLastMod = os.path.getmtime(loc2file)
            return dateLastMod
        else:
            messagebox.showinfo(title="FILE not found", message="ERROR: FILE NOT FOUND!")

    def buDirectory(self):
        curr_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        if not os.path.isfile(curr_dir + r'/backups'):
            os.mkdir(rf'{curr_dir}/backups', 777)

    # def gotoBackups(self):
