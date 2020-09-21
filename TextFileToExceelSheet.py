from openpyxl import Workbook
from openpyxl import load_workbook
import pandas as pd 
import os


def txtFileToExcelsheet():
    """ This Function used for to Convert Txt File to Excel Sheet
    """
    read_file = pd.read_csv (input("Enter text File Name with txt  : "))
    read_file.to_csv (input("Enter CVS file Name  :  "), index=None)

txtFileToExcelsheet()