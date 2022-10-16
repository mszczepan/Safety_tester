
import clr

clr.AddReference('C:\\Program Files\\Siemens\\Automation\\Portal V16\PublicAPI\\V16\\Siemens.Engineering.dll')
from System.IO import DirectoryInfo, FileInfo

import Siemens.Engineering as tia
import Siemens.Engineering.HW.Features as hwf
import Siemens.Engineering.Compiler as comp
import Siemens.Engineering.Download as dl
import os

print ('Starting TIA with UI')
mytia = tia.TiaPortal(tia.TiaPortalMode.WithUserInterface)