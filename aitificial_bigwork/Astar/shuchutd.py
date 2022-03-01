import pandas as pd
import openpyxl

def shuchutd(Map,allx=42,ally=42):
    # 先打开我们的目标表格，再打开我们的目标表单
    wb=openpyxl.load_workbook(r'通道输出.xlsx')
    ws = wb['Sheet1']
    for x in range(0,allx):
        for y in range(0,ally):
            ws.cell(row = x+1, column =y+ 1).value =Map[x][y]
        # 保存操作
    wb.save(r'通道输出.xlsx')