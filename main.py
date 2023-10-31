from module1 import *
analyticsDirectory = '.\\DP2Z Analysis\\'


#os.chdir("\\tymx-fs-002v\restricted\DPC\DPCZ Career Field Teams")
os.chdir("c:\\users\\aiden\\onedrive\\desktop")

def main():
    print("Welcome to the PAQ database entry TUI please select one of the following options and hit enter:")

    while True:
        print ("A). Update PAQ database with SLRP data from the most current")
        usrSelect=input()
        if (not re.match("[AaBbCc]", usrSelect)):
            print("ERROR: Invalid option. Please Enter A Letter Corresponding to the menu and press enter")
        elif (re.match("[Aa]", usrSelect)):
            getCopySLRPReport(analyticsDirectory)


if __name__ == "__main__":
    main()