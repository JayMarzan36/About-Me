import wx, os, time, threading
from PIL import Image


import splash
import find_file

class App(wx.Frame):
    def __init__(self, parent, title):
        super(App, self).__init__(parent, title=title, size=(1000, 600))
        
        splash.MySplashScreen()
        time.sleep(3)
        
        icon = wx.Icon("data\splash_img.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        
        self.selected_image_path = ""
        self.exe_signiture = [b"MZ", b"\\x7fELF", b"\\xFF\xD8"]

        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.image_button_explore = wx.Button(self.panel, label="Browse Images")
        self.image_button_explore.Bind(wx.EVT_BUTTON, self.browse_image_Files)
        vbox.Add(self.image_button_explore, 0, wx.ALL | wx.EXPAND, 5)

        self.full_system_search = wx.Button(self.panel, label="System Search")
        self.full_system_search.Bind(wx.EVT_BUTTON, self.system_Search)
        vbox.Add(self.full_system_search, 0, wx.ALL | wx.EXPAND, 5)

        self.show_oversize = wx.Button(self.panel, label="Show OverSized")
        self.show_oversize.Bind(wx.EVT_BUTTON, self.show_over)
        vbox.Add(self.show_oversize, 0, wx.ALL | wx.EXPAND, 5)

        self.show_sig_files = wx.Button(self.panel, label="Show Sig")
        self.show_sig_files.Bind(wx.EVT_BUTTON, self.show_sig)
        vbox.Add(self.show_sig_files, 0, wx.ALL | wx.EXPAND, 5)

        self.show_safe_files = wx.Button(self.panel, label="Show Safe")
        self.show_safe_files.Bind(wx.EVT_BUTTON, self.show_safe)
        vbox.Add(self.show_safe_files, 0, wx.ALL | wx.EXPAND, 5)

        self.path_text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.HSCROLL)
        vbox.Add(self.path_text, 1, wx.ALL | wx.EXPAND, 5)

        self.panel.SetSizer(vbox)

        self.all_files = None
        self.avg = 0
        self.average_file_size = []
        self.files_over_size = []
        self.files_with_sig = []
        self.safe_files = []
        self.unable_to_open = []

        self.Show()

    def show_safe(self, event):
        def dipsplay_safe():
            self.path_text.Clear()
            for f in self.safe_files:
                self.path_text.AppendText(f + "\n")
        dipsplay_safe_thread = threading.Thread(target= dipsplay_safe)
        dipsplay_safe_thread.start()

    def show_sig(self, event):
        self.path_text.Clear()
        def display_sig():
            for f in self.files_with_sig:
                self.path_text.AppendText(f + "\n")
        display_sig_thread = threading.Thread(target= display_sig)
        display_sig_thread.start()

    def show_over(self, event):
        self.path_text.Clear()
        def display_over():
            for f in self.files_over_size:
                self.path_text.AppendText(f + f"      Over size limit \n")
        display_over_thread = threading.Thread(target= display_over)
        display_over_thread.start()

    def system_Search(self, event):
        def system_search_thread():
            found_files = find_file.main(file_type=".png")
            found_files2 = find_file.main(file_type=".jpg")
            found_files = found_files + found_files2
            self.all_files = found_files

            for f in found_files:
                self.average_file_size.append(str(os.path.getsize(f)))

            total_sum = 0
            for i in self.average_file_size:
                total_sum += int(i)
            num_values = len(self.average_file_size)
            self.avg = int(total_sum / num_values / 1024)

            items_to_insert = []

            for f in found_files:
                type = self.check_Image(file_path=f, file_size_kb=self.avg)
                if type[0] == "S":
                    self.safe_files.append(f)
                if type[0] == "C":
                    self.unable_to_open.append(f)
                    items_to_insert.append((f + "      Unable to open \n", 'orange'))
                if len(type) == 2:
                    if type[1] in self.exe_signiture:
                        self.files_with_sig.append(f + "         " + str(type[1]))
                    else:
                        self.files_over_size.append(f)
                    items_to_insert.append((f + f"       {type[1]} \n", 'red'))

            for item, bg_color in items_to_insert:
                self.path_text.AppendText(item)

        search_thread = threading.Thread(target=system_search_thread)
        search_thread.start()

    def browse_image_Files(self, event):
        dialog = wx.FileDialog(self, "Select a File", "", "", "Image files (*.png;*.jpg)|*.png;*.jpg|All files (*.*)|*.*", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        result = dialog.ShowModal()
        self.selected_image_path = dialog.GetPath()
        self.check_Image(self.selected_image_path, popb=True)

    def check_Image(self, file_path, popb=False, file_size_kb=150):
        try:
            with Image.open(file_path) as image_file:
                image_data = image_file.tobytes()
                for sig in self.exe_signiture:
                    if sig in image_data:
                        if popb:
                            self.pop_up(f"Unsafe, detected embedded .exe with signiture {sig}", "WARNING")
                        else:
                            return ['W', f"EXE Signiture: {sig}"]
                    
                if os.path.getsize(file_path) >= file_size_kb:
                    if popb:
                        self.pop_up("Caution, image above average size 150kb", "Caution")
                    return ['C', f'Above avg file size: {file_size_kb}']
                if popb:
                    self.pop_up("Safe, detected NO embedded .exe", "SAFE")
            return ['S']
        except:
            return ['C']

    def pop_up(self, string: str, type: str):
        dialog = wx.MessageDialog(self, string, type, wx.OK)
        dialog.ShowModal()

def main():
    

    if __name__ == "__main__":
        app = wx.App()
        frame = App(None, title='Detect')
        
        
        app.MainLoop()
main()