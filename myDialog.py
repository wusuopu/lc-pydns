#!/usr/bin/env python
#-*- coding:utf-8 -*-
## 
#  Copyright (C) 
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation.
# 本程序是免费软件，基于GPL许可发布。
# 
##
# @文件名(file): myDialog.py
# @作者(author): 龙昌锦(LongChangjin)
# @博客(blog): http://www.xefan.com
# @邮箱(mail): admin@xefan.com
# @时间(date): 2012-02-28
# 
from os import _exit as exit
try:
    import pygtk
    pygtk.require('2.0')
except Exception, e:
    pass
try:
    import gtk
    import gobject
except importError, e:
    exit(1)


class ErrorDialog:
    def __init__(self, parent=None,text=None):
        dialog = gtk.MessageDialog(parent, 
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, message_format=text)
        self.res = dialog.run()
        dialog.destroy()
        #dialog.show_all()
        #dialog.connect("delete-event", self.delete)
        #dialog.connect("response", self.resp)
    #def delete(self, widget, data=None):
    #    print "del:",
    #    widget.response(-4)
    #    return False
    #def resp(self, res, data=None):
    #    self.res = res
    #    print "res:",
    #    print res

class WarningDialog:
    def __init__(self, parent=None,text=None):
        dialog = gtk.MessageDialog(parent, 
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_WARNING, gtk.BUTTONS_OK, message_format=text)
        self.res = dialog.run()
        dialog.destroy()

class InfoDialog:
    def __init__(self, parent=None,text=None):
        dialog = gtk.MessageDialog(parent, 
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_INFO, gtk.BUTTONS_OK, message_format=text)
        self.res = dialog.run()
        dialog.destroy()

class QueDialog:
    def __init__(self, parent=None,text=None):
        dialog = gtk.MessageDialog(parent, 
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, message_format=text)
        self.res = dialog.run()
        dialog.destroy()
        
        
if __name__ == "__main__":
    d = QueDialog()
    #print d.res
    gtk.main()
    

