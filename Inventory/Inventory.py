import wx

class Inventory(wx.Frame):

    def __init__(self, *args, **kw):
        super(Inventory, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.listbox = wx.ListBox(panel)
        hbox.Add(self.listbox, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        btnPanel = wx.Panel(panel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        newBtn = wx.Button(btnPanel, wx.ID_ANY, 'New item', size=(90, 30))
        renBtn = wx.Button(btnPanel, wx.ID_ANY, 'Rename item', size=(90, 30))
        delBtn = wx.Button(btnPanel, wx.ID_ANY, 'Delete item', size=(90, 30))
        clrBtn = wx.Button(btnPanel, wx.ID_ANY, 'Clear all', size=(90, 30))

        self.Bind(wx.EVT_BUTTON, self.NewItem, id=newBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnRename, id=renBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDelete, id=delBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnClear, id=clrBtn.GetId())
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnRename)

        vbox.Add((-1, 20))
        vbox.Add(newBtn)
        vbox.Add(renBtn, 0, wx.TOP, 5)
        vbox.Add(delBtn, 0, wx.TOP, 5)
        vbox.Add(clrBtn, 0, wx.TOP, 5)

        btnPanel.SetSizer(vbox)
        hbox.Add(btnPanel, 0.6, wx.EXPAND | wx.RIGHT, 20)
        panel.SetSizer(hbox)

        self.SetTitle('Inventory')
        self.Centre()

    def NewItem(self, event):

        text1 = wx.GetTextFromUser('Enter a new item', 'Insert dialog')
        text2 = wx.GetTextFromUser("Enter its price", 'Insert dialog')
        text = [text1+" for "+text2+" Rs. "]
        if text != '':
            self.listbox.Append(text)

    def OnRename(self, event):

        sel = self.listbox.GetSelection()
        text = self.listbox.GetString(sel)
        renamed1 = wx.GetTextFromUser('Enter a new name', 'Rename dialog')
        renamed2 = wx.GetTextFromUser('Enter its price', 'Rename dialog')
        renamed = [renamed1+" for "+renamed2+" Rs. "]
        if renamed != '':
            self.listbox.Delete(sel)
            item_id = self.listbox.Insert(renamed, sel)
            self.listbox.SetSelection(item_id)

    def OnDelete(self, event):

        sel = self.listbox.GetSelection()
        if sel != -1:
            self.listbox.Delete(sel)

    def OnClear(self, event):
        self.listbox.Clear()


def main():

    app = wx.App()
    ex = Inventory(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()