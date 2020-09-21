from openpyxl import Workbook
from openpyxl import load_workbook
import pandas as pd 
import os

def readXlrbFile():
    df = pd.read_excel (r'Enter the of the file with xlrx',engine='odf')
    print (df)

readXlrbFile()

