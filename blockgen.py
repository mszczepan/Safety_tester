import clr

clr.AddReference('C:\\Program Files\\Siemens\\Automation\\Portal V16\PublicAPI\\V16\\Siemens.Engineering.dll')
from System.IO import DirectoryInfo, FileInfo

import Siemens.Engineering as tia
import Siemens.Engineering.HW.Features as hwf
import Siemens.Engineering.Compiler as comp
import Siemens.Engineering.Download as dl
import os

#tia.TiaPortalMode.WithUserInterface
mytia = tia.TiaPortal(tia.TiaPortalMode.WithUserInterface)
project_path = FileInfo('D:\\01_TIA_tester\\Project1\\Project1.ap16')
projects = mytia.Projects
project = projects.Open(project_path)
for device in project.Devices:
    print(device.Name)
    print("------------")

for deviceItem in device.DeviceItems:

    print(deviceItem.Name)
print("------------")
print(device.DeviceItems[1].Name)
software_container = tia.IEngineeringServiceProvider(device.DeviceItems[1]).GetService[hwf.SoftwareContainer]()
software_base = software_container.Software
#plc_block = software_base.BlockGroup.Blocks.Find("safety_tester")
#plc_block.Export(FileInfo('D:\\01_TIA_tester\\safety_tester.xml'), tia.ExportOptions.WithDefaults)
software_base.BlockGroup.Blocks.Import(FileInfo('D:\\01_TIA_tester\\safety_tester12.xml'), tia.ImportOptions.Override)


#((IEngineeringServiceProvider)deviceItem).GetService<SoftwareContainer>()
#software_container = tia.IEngineeringServiceProvider(deviceItem).GetService[hwf.SoftwareContainer]()
#software_base = software_container.Software
#plc_block = software_base.BlockGroup.Blocks.Find("Main")
#PlcBlock plcBlock = plcSoftware.BlockGroup.Blocks.Find("MyBlock");
#plcBlock.Export(new FileInfo(string.Format(@”D:\Samples\{0}.xml”, plcBlock.Name)), ExportOptions.WithDefaults);

for dev in project.Devices:
    print(dev)
#D:\01_TIA_tester\Project1
# processes = tia.TiaPortal.GetProcesses()
# print(processes)
#print ('Starting TIA with UI')
#mytia = tia.TiaPortal(tia.TiaPortalMode.WithUserInterface)