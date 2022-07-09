import sys,subprocess,time
from pathlib import Path
from archicad import ACConnection


print("!================================Running vsgdl.py====================================!")
LP_XMLConverter = r"C:\Program Files\GRAPHISOFT\ARCHICAD 25\LP_XMLConverter.exe"  #此处地址视情况更改
action = sys.argv[1]
source = Path(sys.argv[2])


parent_folder = source.parent
if source.is_dir():
	if source.name == "scripts":
		obj_name = parent_folder.name[:-4] 
		parent_folder = parent_folder.parent
		source = source.parent
	else: 
		obj_name = source.name[:-4] 
elif source.is_file():
	obj_name = source.stem
else:
	print("Not a Directory or a File passed as an agrument")
	exit()

match action:
	# case "libpart2xml":
	# 	print("---Decompiling GSM to XML......")
	# 	dest = parent_folder.joinpath(obj_name).with_suffix(".xml")
	# case "xml2libpart":
	# 	print("---Compiling XML to GSM......")
	# 	dest = parent_folder.joinpath(obj_name).with_suffix(".gsm")
	case "libpart2hsf":
		print("---Decompiling GSM to HSF......")
		dest = parent_folder / f'{obj_name}_HSF'
	case "hsf2libpart":
		print("---Compiling HSF to GSM......")
		dest = parent_folder / f'{obj_name}.gsm'

print("Action:       ",action)
print("Source:       ",source)
print("Folder:       ",parent_folder)
print("Name:         ",obj_name)
print("Destination:  ",dest)
print("")

def execLP_XML(action, source, dest, pswd = False):
	print("Excecuting LP_XMLConverter")
	if pswd :
		pswd_arg = '-password'
		LP_XML_args = [LP_XMLConverter, action, pswd_arg, pswd,  source, dest]
	else:
		LP_XML_args = [LP_XMLConverter, action, source, dest]

	result = subprocess.run(LP_XML_args, stdout=subprocess.PIPE)
	print(result.stdout)

	if action == "hsf2libpart":
		conn = ACConnection.connect (19723)#要输入AC进程的端口，否则可能失效
		acc = conn.commands
		act = conn.types
		acc.ExecuteAddOnCommand (act.AddOnCommandId ('AdditionalJSONCommands', 'ReloadLibraries'))
		print("---Auto Reloading Library......")


execLP_XML(action, source, dest)
print(f"!==============================={time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))}=================================!")
