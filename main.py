import excellib as el
from openpyxl.utils import get_column_letter
import clr


matrix = el.ExcelService(4, 8, 4, 8)
matrix.load_wb(".\macierz_test.xlsx", "Arkusz1")
matrix.read_matrix()
# x={'a':[0,1,2,3]}
# x['a'].append(5)
# print(x['a'][4])



# clr.AddReference('C:\\Program Files\\Siemens\\Automation\\Portal V16\PublicAPI\\V16\\Siemens.Engineering.dll')
# from System.IO import DirectoryInfo, FileInfo
#
# import Siemens.Engineering as tia
# import Siemens.Engineering.HW.Features as hwf
# import Siemens.Engineering.Compiler as comp
# import Siemens.Engineering.Download as dl
# import os
#
# print ('Starting TIA with UI')
# mytia = tia.TiaPortal(tia.TiaPortalMode.WithUserInterface)