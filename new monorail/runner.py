import subprocess
import win32gui, win32con

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)
command1 = subprocess.Popen(['python', 'ht.py'])
command2 = subprocess.Popen(['python', 'index.py'])
