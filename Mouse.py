
import win32gui
import win32api
from win32.lib import win32con
import time
import win32process
import datetime
import win32ui
import sys
from ctypes import *

class POINT(Structure):
    _fields_ = [("x", c_ulong),("y", c_ulong)]

    

def mouse_move(x,y):
    win32api.SetCursorPos([x, y])
    
def GetPosition():
    po = POINT()
    win32api.GetCursorPos(byref(po))
    return int(po.x), int(po.y)

def Click(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    
def DoubleClick(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def ClickController(handle):
    if (handle == 0): 
        return
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN,0,0)
    win32gui.SendMessage(handle, win32con.WM_KEYUP,0,0) 

def DoubleClickController(handle):
    if (handle == 0): 
        return
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN,0,0)
    win32gui.SendMessage(handle, win32con.WM_KEYUP,0,0) 
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN,0,0)
    win32gui.SendMessage(handle, win32con.WM_KEYUP,0,0) 


   