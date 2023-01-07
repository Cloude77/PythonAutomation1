from openpyxl import load_workbook

workbook = load_workbook(filename="C:/Users/SergeyML/Desktop/Excell/TestCoder.xlsx")
sheet = workbook.active

# Color list
workbook_sheet = workbook['Code test']
workbook_sheet.title = 'Code test'
workbook_sheet.sheet_properties.tabColor = 'FF0000'
workbook.save('C:/Users/SergeyML/Desktop/Excell/TestCoder.xlsx')

# --------------------------------------------------------------

