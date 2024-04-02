import wx
from wx.adv import SplashScreen
class MySplashScreen(wx.adv.SplashScreen):
    def __init__(self, parent=None):
        # Load the splash image (replace with your own image)
        bitmap = wx.Bitmap(name="data\splash_img.jpg", type=wx.BITMAP_TYPE_JPEG)
        
        # Specify splash screen style and duration
        splash_style = wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT
        duration = 3000  # milliseconds
        
        # Call the constructor with the specified arguments
        super().__init__(bitmap=bitmap, splashStyle=splash_style,
                         milliseconds=duration, parent=None,
                         id=-1, pos=wx.DefaultPosition,
                         size=wx.DefaultSize, style=wx.STAY_ON_TOP | wx.BORDER_NONE)
        
        # Bind the close event to an exit handler
        self.Bind(wx.EVT_CLOSE, self.OnExit)

    def OnExit(self, event):
        # Ensure the program continues after closing the splash screen
        event.Skip()
        self.Hide()