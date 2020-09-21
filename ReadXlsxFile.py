from openpyxl import Workbook
from openpyxl import load_workbook
import pandas as pd 
import os


def readXlsxFile():
    df = pd.read_excel (input("Enter Name of the file with Xlsx :  "))
    print (df)


readXlsxFile()
