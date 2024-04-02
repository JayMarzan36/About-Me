import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Test of BoxSizer")
        
        # Create a vertical box sizer
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Create a horizontal box sizer for the top row of buttons
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.panel = wx.Panel(self)
        
        # Create the buttons
        self.btn1 = wx.Button(self.panel, label="Button 1")
        self.btn2 = wx.Button(self.panel, label="Button 2")
        self.btn3 = wx.Button(self.panel, label="Button 3")
        self.btn4 = wx.Button(self.panel, label="Button 4")
        
        # Add the buttons to the sizers
        hbox.Add(self.btn1, proportion=1, flag=wx.CENTER | wx.ALL, border=5)
        hbox.Add((0, 0), proportion=4, flag=wx.EXPAND)
        hbox.Add(self.btn2, proportion=1, flag=wx.CENTER | wx.ALL, border=5)
        
        # Create another horizontal box sizer for the bottom row of buttons
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(self.btn3, proportion=1, flag=wx.CENTER | wx.ALL, border=5)
        hbox1.Add((0, 0), proportion=4, flag=wx.EXPAND)
        hbox1.Add(self.btn4, proportion=1, flag=wx.CENTER | wx.ALL, border=5)
        
        # Add both horizontal sizers to the vertical sizer
        vbox.Add(hbox, proportion=1, flag=wx.CENTER | wx.ALL, border=5)
        vbox.Add(hbox1, proportion=1, flag=wx.CENTER | wx.ALL, border=5)
        
        self.panel.SetSizer(vbox)
        vbox.SetSizeHints(self)
        self.Centre()

if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()
