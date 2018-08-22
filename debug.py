import win32gui
from win32gui import GetWindowText, GetForegroundWindow
cWindow = GetWindowText(GetForegroundWindow())
print(cWindow)

def updateWindow():
    global cWindow
    if cWindow != GetWindowText(GetForegroundWindow()):
        cWindow = GetWindowText(GetForegroundWindow())
        print(cWindow)
       # print(win32gui.GetClassName(GetForegroundWindow()))

        if "Google Chrome" in cWindow:
            print("Chrome Found")
            print(win32gui.FindWindow("Chrome_WidgetWin_1", None))
        else:
            print("Chrome not found")
        
while True:
    updateWindow()
