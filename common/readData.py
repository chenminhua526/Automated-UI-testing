import os
import openpyxl


class ReadExcel:

    def __init__(self, file, sheet_name):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file = os.path.join(path, 'testData', file)
        self.sheet_name = sheet_name

    # 获取sheet
    def get_sheet(self):
        wb = openpyxl.load_workbook(self.file)
        sheet = wb[self.sheet_name]
        return sheet

    # 获取行数
    def get_rows(self):
        sheet = self.get_sheet()
        return sheet.max_row

    # 获取单行数据
    def get_row_data(self, row):
        sheet = self.get_sheet()
        col_data = []
        for i in sheet[row]:
            col_data.append(i.value)
        return col_data

    # 获取除首行外的所有数据
    def get_all_data(self):
        data = []
        rows = self.get_rows()
        for i in range(1, rows):
            data.append(self.get_row_data(i))
        return data

    # 逐行判断类名和方法名，返回正确的测试数据
    def get_case_data(self, class_name, method_name):
        data = self.get_all_data()
        for i in data:
            if i[0] == class_name:
                if i[1] == method_name:
                    value = i[2]
                    return value
