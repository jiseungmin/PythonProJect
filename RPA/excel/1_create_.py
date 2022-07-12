# 파일 만들기
import openpyxl
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "SHEET"
wb.save('test.xlsx')
wb.close()
