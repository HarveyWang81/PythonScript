

import wx
import os

class BitMap(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'weixin',size=(300,200))
        pane1 = wx.Panel(self,-1)
        bmp = wx.Image(os.path.join(os.path.dirname(__file__),'weixin.jpg'),wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        self.button = wx.BitmapButton(pane1,-1,bmp,pos=(10,20))

if __name__ == "__main__":
    app = wx.App()
    Frame = BitMap()
    Frame.Show()
    app.MainLoop()
