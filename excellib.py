import openpyxl as op


# Loading and processing of the safety matrix


class ExcelService:

    # Initialization of the safety matrix coordinates

    def __init__(self, row_start, row_end, column_start, column_end):
        self.sh = None
        self.ws = None
        self.wb = None
        self.row_start = row_start
        self.row_end = row_end
        self.column_start = column_start
        self.column_end = column_end
        self.matrix_conf = {}

    def load_wb(self, path, sheet_name):
        self.wb = op.load_workbook(path)
        self.sh = self.wb[sheet_name]

    def read_matrix(self):

        for row in range(self.row_start, self.row_end):

            #for column in range(self.column_start, self.column_end):
            self.matrix_conf[self.sh[f'{self.column_start}{row}'].value] = 1
            #print(f'{self.column_start}{row}')
        print(self.matrix_conf)
