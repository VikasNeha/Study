from win32com.client import Dispatch

Auto = Dispatch("AutoItX3.Control")
Auto.WinWait("Authentication Required", "", "50")
if Auto.WinExists("Authentication Required"):
    Auto.WinActivate("Authentication Required")
    Auto.Send("asd")
    Auto.Send("{TAB}")
    Auto.Send("asd")
    Auto.Send("{ENTER}")