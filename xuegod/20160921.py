import wx

app = wx.App()  # 实例化主循环
win = wx.Frame(None, title='first', size=(410, 335))  # 实例化一个窗口组件
panel = wx.Panel(win)
bt1 = wx.Button(panel, label='open')  # 实例化一个按钮
bt2 = wx.Button(panel, label='save')  # 实例化一个按钮

finename = wx.TextCtrl(panel)  # 实例化一个窗口组件
content = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.HSCROLL)

s_box = wx.BoxSizer()  # 创建尺寸器
s_box.Add(bt2, proportion=1, flag=wx.EXPAND | wx.ALL, border=1)
s_box.Add(finename, proportion=3, flag=wx.EXPAND | wx.ALL, border=1)
s_box.Add(bt1, proportion=1, flag=wx.EXPAND | wx.ALL, border=1)
# 比例           填充                   边框

v_box = wx.BoxSizer(wx.VERTICAL)  # 创建尺寸器
v_box.Add(s_box, proportion=1, flag=wx.EXPAND | wx.ALL, border=1)
v_box.Add(content, proportion=15, flag=wx.EXPAND | wx.ALL, border=1)
panel.SetSizer(v_box)  # 声明主尺寸器

win.Show()
app.MainLoop()
