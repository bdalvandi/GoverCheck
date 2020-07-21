import wx
from window import MainWin


app = wx.App()
win = MainWin(None)
win.Show()
app.MainLoop()

