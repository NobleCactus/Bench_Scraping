# This program takes staff currently residing on Deloitte's bench, takes a screenshot of their DPN profiles, and
# sends it to a folder where they can be more easily sifted through.

# Packages used are:
#  - pandas for Excel sheet manipulation
#  - openpyxl is required for pandas to work
#  - Selenium for taking screenshots
#  - Time for allowing URLs to load in order to take screenshots
#  - os for getting the name of the user currently logged in to provide for file paths

import pandas as pd
from selenium import webdriver
import time
import os
import openpyxl
from selenium.webdriver.chrome.service import Service
from Additional_Functions import create_practice_dict, get_most_practitioners, get_least_practitioners

# Opens new browser using Chromedriver, which will need to be installed from
# https://chromedriver.storage.googleapis.com/index.html?path=109.0.5414.74/ for this to work. Make sure chromedriver
# is downloaded to local Downloads folder, or else manually update the path in Service to where it is located.
cur_user = os.getlogin()
ser = Service(r"C:\\Users\\" + cur_user + "\\Downloads\\chromedriver_win32\\chromedriver.exe")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=ser, options=op)

# Reads Excel file
open_file = pd.ExcelFile(r"C:\\Users\\" + cur_user + "\\Downloads\\Vetted GPS Availability with GPS Security Ranks 1_25_2023.xlsx")
# Navigates to the correct sheet in the Excel file using columns A (Name of practitioner), D (URL to DNET profile),
# and O (Offering Portfolio)
open_sheet = pd.read_excel(open_file, 'Cons Availability', usecols='A, D, O')


# Initial opening and access of Deloitte.com will require a sign in,which is why the sleep time is 60 seconds for the
# first entry in the Excel file. Subsequent URLs will not require another sign in and will have
# significantly reduced sleep times (sleep allows time for the page to load prior to the screenshot being taken)
browser.get(open_sheet['Resume URL'][0])
time.sleep(60)
browser.save_screenshot("C:\\Users\\" + cur_user + "\\Documents\\DPN Profiles\\" + open_sheet['Practitioner '][0] + ".png")

# Total number of consultants on the bench would be used if trying to use this script on the entire data set.
# For the purpose of this demonstration, only the first 15 profiles will be used.
consultants_on_bench = len(open_sheet['Resume URL'])

# Calls functions from Additional Functions to get the percentage of practitioners from each portfolio and find out which
# portfolio has the most / least amount of practitioners on the bench
practice_dict = create_practice_dict(open_sheet['Offering Portfolio'])
most_practitioners = get_most_practitioners(consultants_on_bench, practice_dict)
least_practitioners = get_least_practitioners(consultants_on_bench, practice_dict)
print('The practice with the most consultants on the bench is ' + most_practitioners[0] + ' with a total percentage of ' + str(most_practitioners[1]) + '%')
print('The practice with the least consultants on the bench is ' + least_practitioners[0] + ' with a total percentage of ' + str(least_practitioners[1]) + '%')

for consultant in range(1, 15):
   browser.get(open_sheet['Resume URL'][consultant])
   time.sleep(5)
   browser.save_screenshot("C:\\Users\\" + cur_user + "\\Documents\\DPN Profiles\\" + open_sheet['Practitioner '][consultant] + ".png")

browser.quit()


