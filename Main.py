from asyncio import constants
from fileinput import filename
from hashlib import new
from openpyxl import *
from Tract import Tract
from Logic import extractBook, compareRows, Compare
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell

# workbook = xlsxwriter.Workbook('rich_strings.xlsx')
# worksheet = workbook.add_worksheet()

#create final book
workbook = xlsxwriter.Workbook('bookReport.xlsx')
worksheet = workbook.add_worksheet()

red = workbook.add_format()
red.set_font_color('red')

strikethrough = workbook.add_format()
strikethrough.set_font_strikeout()

#copys the contents of the original book
bookOne = extractBook('Alberta_2023_complete.xlsx')
bookTwo = extractBook('Alberta_2023_original.xlsx')

#checks to ensure both books have the same number of rows
if (len(bookOne) != len(bookTwo)):
    print('The two books have different data lengths')
else:
    print('Comparing books')

for rowIndex, row in enumerate(bookOne):
    for columnIndex, column in enumerate(row):

        newData = bookTwo[rowIndex][columnIndex]

        ReplaceRow = '--' + str(newData) + '-- +' + str(newData)
        AddRow = '+' + str(newData)

#Check if the two cell values are the same 
        if Compare(column, newData):
            worksheet.write(rowIndex, columnIndex, str(column))

#If they aren't the same check which value changed
        else:
            if column is None:
                if newData == '':
                    #if both values are blank
                    worksheet.write(rowIndex, columnIndex, str(''))
                else:
                    #If the old value was blank
                    worksheet.write(rowIndex, columnIndex, str(newData), red) 
            else: 
                #if niether values are blank
                worksheet.write_rich_string(rowIndex, columnIndex, red, str(newData), strikethrough, ' ' + str(column))

workbook.close()