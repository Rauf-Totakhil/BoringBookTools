from openpyxl import Workbook
from openpyxl import load_workbook
import pandas as pd
import os


def addExceelsheet():
    global workbook
    workbook = Workbook()
    sheet = workbook.active

    sheet["A1"] =input("Enter Name for sheet A1 : ")
    sheet["B1"] = input("Enter Name for Sheet B1 : ")
    sheet["C1"]=input("Enter Name for sheet C1 : ")

    workbook.save(filename=input("Wrtie Excelsheet to create it : "))

addExceelsheet()
