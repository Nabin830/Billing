import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\pande\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\pande\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("Main.py", base=base)]


cx_Freeze.setup(
    name = "Billing",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":['tcl86t.dll','tk86t.dll', 'Photo','bills']}},
    version = "1.0",
    description = "Billing | Developed By Ma aafai la ho sir",
    executables = executables
    )