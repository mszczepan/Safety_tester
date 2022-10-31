import excellib as el

matrix = el.ExcelService(4, 8, 4, 8)
matrix.load_wb(".\macierz_test.xlsx", "Arkusz1")
print(matrix.read_matrix())



