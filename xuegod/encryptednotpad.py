import wx,os,random
from Crypto.Cipher import AES
from hashlib import sha1

BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * (chr(BS - len(s) % BS).encode())
unpad = lambda s : s[0:-s[-1]]

class passDlg(wx.Dialog):
    def __init__(self,*args,**kwargs):
        super(passDlg,self).__init__(*args,**kwargs)
        panel = wx.Panel(self)
        self.texts=[]
        for text in ['密   码:','新密码:','新密码:']:
            label = wx.StaticText(self, -1, text)
            passwd = wx.TextCtrl(self,size=(200,20),style = wx.TE_PASSWORD)
            self.texts.append((label,passwd))
        boxes = [wx.BoxSizer() for _ in range(3)]
        [box.Add(text[0]) for box,text in zip(boxes,self.texts)]
        [box.Add(text[1]) for box,text in zip(boxes,self.texts)]
        box_main = wx.BoxSizer(wx.VERTICAL)
        [box_main.Add(box) for box in boxes]
        button_ok = wx.Button(self, wx.ID_OK,'确定')
        button_cancel = wx.Button(self, wx.ID_CANCEL,'取消')
        box = wx.BoxSizer()
        box.Add(button_ok)
        box.Add(button_cancel)
        box_main.Add(box,flag = wx.EXPAND | wx.LEFT, border = 70)
        self.SetSizer(box_main)

class NotepadFrame(wx.Frame):
    def __init__(self,*args,**kwargs):
        defaults_args = (None,-1)
        default_kwargs = dict(title = 'EncNotePad',size=wx.DefaultSize)
        if len(args)<2:
            args = args+defaults_args[len(args):]
        default_kwargs.update(kwargs)
        super(NotepadFrame,self).__init__(*args,**default_kwargs)
        self.InitUI()
        accelTbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('S'), 2)])  
        self.SetAcceleratorTable(accelTbl) 
        self.enc = False
        self.passwd = ''
        
    def InitUI(self):
        menubar = wx.MenuBar()
        menu = wx.Menu()
        menu.Append(0, '新建')
        menu.Append(1, '打开')
        menu.Append(2, '保存')
        menu.Append(3, '另存为')
        menu.Append(4, '加密')
        menu.Append(5, '退出')
        menubar.Append(menu,'文件')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnNew, id = 0)
        self.Bind(wx.EVT_MENU, self.OnOpen, id = 1)
        self.Bind(wx.EVT_MENU, self.OnSave, id =2)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, id =3)
        self.Bind(wx.EVT_MENU, self.OnEncrypt, id =4)
        self.Bind(wx.EVT_MENU, self.OnExit, id =5)
        self.panel = wx.Panel(self, -1)
        self.editor = wx.TextCtrl(self.panel,style=wx.TE_MULTILINE,size=wx.DefaultSize)
        self.panel.Bind(wx.EVT_SIZE,self.OnSize)
        self.box = wx.BoxSizer()
        self.box.Add(self.editor)
        self.panel.SetSizer(self.box)


    def OnSize(self,event):
        self.editor.SetSize(event.Size)

    def OnNew(self,event):
        self.editor.SetValue('')
        self.SetTitle('EncNotePad -- Untitled')
        self.filename = None
        self.enc = False

    def OnOpen(self,event):
        file_ext = 'encnotepad(*.enc)|*.enc|Text(*.txt)|*.txt|All files(*.*)|*.*'
        dlg = wx.FileDialog(self,"Open File...",
            os.getcwd(),
            style = wx.FD_OPEN,
            wildcard = file_ext)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.ReadFile()
            self.SetTitle('EncNotePad -- '+self.filename)
        dlg.Destroy()


    def OnSave(self,event):
        if hasattr(self,'filename') and self.filename:
            self.SaveFile()
        else:
            self.OnSaveAs(event)

    def OnSaveAs(self,event):
        file_ext = 'encnotepad(*.enc)|*.enc|Text(*.txt)|*.txt|All files(*.*)|*.*'
        dlg = wx.FileDialog(self,"Open File...",
            os.getcwd(),
            style = wx.FD_SAVE,
            wildcard = file_ext)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.SaveFile()
        dlg.Destroy()

    def OnEncrypt(self,event):
        if not self.enc:
            dlg = wx.TextEntryDialog(self.panel,'密  码:','输入密码','',style = wx.TE_PASSWORD | wx.OK | wx.CANCEL)
            if dlg.ShowModal() == wx.ID_OK:
                self.passwd = dlg.GetValue()
                self.enc = True
            if not self.passwd:
                self.enc=False
            dlg.Destroy()
        else:
            passdlg = passDlg(self,title='设置密码',size=(260,150))
            if passdlg.ShowModal()==wx.ID_OK:
                if self.passwd == passdlg.texts[0][1].GetValue():
                    if passdlg.texts[1][1].GetValue()==passdlg.texts[2][1].GetValue():
                        self.passwd = passdlg.texts[1][1].GetValue()
                    else:
                        wx.MessageBox("两次密码输入不一致!", "错误",wx.OK)
                else:
                    wx.MessageBox("密码输入不正确!", "错误",wx.OK)
                if not self.passwd:
                    self.enc=False
            passdlg.Destroy()

    def OnExit(self,event):
        self.Destroy()

    def ReadFile(self):
        with open(self.filename, 'rb') as f:
            data = f.read()
            res = self.DecFile(data)
            self.editor.SetValue(res)

    def SaveFile(self):
        with open(self.filename, 'wb') as f:
            data = self.editor.GetValue()
            data = self.EncFile(data)
            f.write(data)

    def genEncrypto(self,iv=None):
        hashor = sha1()
        hashor.update(self.passwd.encode())
        passwd = hashor.digest()
        hashor.update(self.passwd.encode())
        passwd += hashor.digest()[:12]
        iv = ''.join([chr(random.randint(0,127)) for _ in range(AES.block_size)]) if not iv else iv
        decryptor = AES.new(passwd, AES.MODE_CBC, iv)
        return decryptor,iv

    def hash(sefl,data):
        hashor = sha1()
        hashor.update(data.encode() if type(data) is str else data)
        return hashor.digest()

    def EncFile(self,data): #加密的文件 self.enc=True
        if not self.enc:
            return data
        encryptor,iv = self.genEncrypto()
        data = data.encode()
        data = encryptor.encrypt(pad(data))
        a = self.passwd
        for _ in range(3):
            a = self.hash(a)
        head = a+iv.encode()+data
        tail = self.hash(self.hash(head)+'ryan'.encode())
        data = head + tail
        return data

    def DecFile(self,data):
        data = self.TestData(data)
        if not data[0]:
            return data[1]
        self.enc = True
        dlg = wx.TextEntryDialog(self.panel,'密  码:','输入密码','',style = wx.TE_PASSWORD | wx.OK | wx.CANCEL)
        if dlg.ShowModal() == wx.ID_OK:
            passwd = dlg.GetValue()
        dlg.Destroy()
        passwd_in_file, data = data[1:]
        a = passwd
        for _ in range(3):
            a = self.hash(a)
        if a!=passwd_in_file:
            wx.MessageBox("密码输入不正确!", "错误",wx.OK)
            return ''
        self.passwd = passwd
        iv,data = data[:AES.block_size],data[AES.block_size:]
        decryptor,iv = self.genEncrypto(iv)
        return unpad(decryptor.decrypt(data))

    def TestData(self,data):  #返回是否加密，非加密的话返回False,data;加密的话返回:True,hash(passwd),data
        if len(data)<=40+AES.block_size or (len(data)-40-AES.block_size)%AES.block_size:
            return False, data
        tail = data[-20:]
        if self.hash(self.hash(data[:-20])+'ryan'.encode()) != tail:
            return False, data
        return True,data[:20],data[20:-20]

if __name__=='__main__':
    app = wx.App()
    frame = NotepadFrame()
    frame.Show()
    app.MainLoop()
