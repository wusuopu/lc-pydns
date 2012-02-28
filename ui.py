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
# @文件名(file): ui.py
# @作者(author): 龙昌锦(LongChangjin)
# @博客(blog): http://www.xefan.com
# @邮箱(mail): admin@xefan.com
# @时间(date): 2012-02-28
# 
from myDialog import *
import api
import thread
import time

#build = gtk.Builder()

class Login:
    def main_quit(self,widget, data=None):
        gtk.main_quit()
    def res_code(self, code, text=None):
        if code == '1':
            #self.window.destroy()
            back = True
        elif code == '-1':
            ErrorDialog(self.window, "登陆失败！")
            back =  False
        elif code == '400':
            ErrorDialog(self.window, "网络出错！")
            back = False
        else:
            ErrorDialog(self.window, "错误：" + text)
            back = False
        return back
    def __init__(self):
        self.__build = gtk.Builder()
        self.__build.add_from_file("login.glade")
        self.__build.connect_signals(self)
        self.window = self.__build.get_object("window_login")
        self.entry_mail = self.__build.get_object("entry_mail")
        self.entry_pswd = self.__build.get_object("entry_pswd")
        #fixed = self.__build.get_object("window_login")
        #fixed.modify_text(gtk.STATE_NORMAL, gtk.gdk.Color(0, 0, 1, 0))
        #fixed.set_property("style", "red")
        #print fixed.get_style()
        self.window.show_all()
    def on_button_login_clicked(self, widget):
        if self.entry_mail.get_text_length() == 0:
            ErrorDialog(self.window, "用户名不能为空！")
            return
        if self.entry_pswd.get_text_length() == 0:
            ErrorDialog(self.window, "密码不能为空！")
            return
        self.__mail = self.entry_mail.get_text()
        self.__pswd = self.entry_pswd.get_text()
        gtk.threads_enter()
        self.window.set_sensitive(False)
        time.sleep(1)
        dns = api.UserDetail(self.__mail, self.__pswd)
        dns()
        if self.res_code(dns.code, dns.message) == True:
            m = Main(self.__mail, self.__pswd, dns.status, dns.email_verified)
            self.window.destroy()
            m.button_dfresh.clicked()
            m.main()
        self.window.set_sensitive(True)
        gtk.threads_leave()
        
        
        
class Main:
    def main(self):
        gtk.main()
    def main_quit(self,widget, data=None):
        gtk.main_quit()
    def res_code(self, code, text):
        if code == '1':
            back = True
        elif code == '-1':
            ErrorDialog(self.window, "登陆失败！")
            back = False
        elif code == '400':
            ErrorDialog(self.window, "网络出错！")
            back = False
        else:
            ErrorDialog(self.window, "错误：" + text)
            back = False
        return back
    def __init__(self, mail="", pswd="", status="", verified=""):
        self.__mail = mail
        self.__pswd = pswd
        self.__build = gtk.Builder()
        self.__build.add_from_file("ui.glade")
        self.__build.connect_signals(self)
        self.window = self.__build.get_object("Mainwindow")

        self.button_dfresh = self.__build.get_object("button_dfresh")
        #self.hpaned = self.__build.get_object("hpaned")
        #self.button_dpause = self.__build.get_object("button_dpause")
        #self.button_dadd = self.__build.get_object("button_dadd")
        #self.button_ddel = self.__build.get_object("button_ddel")

        self.label_rdomain = self.__build.get_object("label_rdomain")
        #self.button_rpause = self.__build.get_object("button_rpause")
        #self.button_radd = self.__build.get_object("button_radd")
        #self.button_rdel = self.__build.get_object("button_rdel")
        
        self.treeview_domain = self.__build.get_object("treeview_domain")
        self.treeview_record = self.__build.get_object("treeview_record")
        self.liststore_domain = self.__build.get_object("liststore_domain")
        self.liststore_record = self.__build.get_object("liststore_record")
        self.liststore_recordtype = self.__build.get_object("liststore_recordtype")
        self.liststore_linetype = self.__build.get_object("liststore_linetype")

        self.entry_host = self.__build.get_object("entry_host")
        self.combobox_rtype = self.__build.get_object("combobox_rtype")
        self.combobox_ltype = self.__build.get_object("combobox_ltype")
        self.entry_value = self.__build.get_object("entry_value")
        self.entry_mx = self.__build.get_object("entry_mx")
        self.entry_ttl = self.__build.get_object("entry_ttl")

        self.label_info_email = self.__build.get_object("label_info_email")
        self.label_info_mailverified = self.__build.get_object("label_info_mailverified")
        self.label_info_status = self.__build.get_object("label_info_status")
        self.label_info_email.set_text(mail)
        self.label_info_mailverified.set_text(verified)
        self.label_info_status.set_text(status)
        self.__current_domain = None
        
        self.window.show_all()
        self.__creat_columns()
    def __creat_columns(self):
        dlist = [u"星标", u"域名", u"状态", u"备注"]
        rlist = [u"主机", u"记录类型", u"线路类型", u"记录值", u"MX优先级", u"TTL", u"状态", u"备注"]
        #域名列表
        column = [None] * len(dlist)
        cell = [None] * (len(dlist) + 1)
        for i in xrange(0, len(dlist)):
            if i == 0:
                cell[i] = gtk.CellRendererText()
                cell[i].set_property("visible", False)
                cell[i+1] = gtk.CellRendererToggle()
                column[i] = gtk.TreeViewColumn(dlist[i], cell[i], text=0)
                column[i].pack_start(cell[i+1], False)
                column[i].add_attribute(cell[i+1], "active", 1)
                self.treeview_domain.append_column(column[i])
                continue
            cell[i+1] = gtk.CellRendererText()
            column[i] = gtk.TreeViewColumn(dlist[i], cell[i+1], text=i+1)
            self.treeview_domain.append_column(column[i])
        cell[4].set_property("editable", True)
        cell[1].connect("toggled", self.__domain_mark)
        cell[4].connect("edited", self.__domain_remark)
        #记录列表
        column = [None] * len(rlist)
        cell = [None] * (len(rlist) + 1)
        cell[0] = gtk.CellRendererText()        #did
        cell[0].set_property("visible", False)
        column[0] = gtk.TreeViewColumn(rlist[0], cell[0], text=0)
        cell[1] = gtk.CellRendererText()        #主机
        cell[1].set_property("editable", True)
        cell[1].connect("edited", self.__record_modify, 1)
        column[0].pack_start(cell[1], False)
        column[0].add_attribute(cell[1], "text", 1)
        self.treeview_record.append_column(column[0])

        for i in xrange(1, 3):
            cell[i+1] = gtk.CellRendererCombo()
            column[i] = gtk.TreeViewColumn(rlist[i], cell[i+1], text=i+1)
            if i == 1:
                cell[i+1].set_property("model", self.__build.get_object("liststore_recordtype"))
            elif i == 2:
                cell[i+1].set_property("model", self.__build.get_object("liststore_linetype"))
            cell[i+1].set_property("has-entry", True)
            cell[i+1].set_property("text-column", 0)
            cell[i+1].set_property("width", 50)
            cell[i+1].set_property("editable", True)
            cell[i+1].connect("changed", self.__record_changed, i+1)
            self.treeview_record.append_column(column[i])
        
        for i in xrange(3, len(rlist)):
            cell[i+1] = gtk.CellRendererText()
            cell[i+1].set_property("editable", True)
            cell[i+1].connect("edited", self.__record_modify, i+1)
            column[i] = gtk.TreeViewColumn(rlist[i], cell[i+1], text=i+1)
            self.treeview_record.append_column(column[i])
        cell[i].set_property("editable", False)

    #域名操作
    #修改星标
    def __domain_mark(self, cell, path, data=None):
        i = self.liststore_domain.get_iter(path)
        v = self.liststore_domain[path][1]
        m = "yes" if v == False else "no"
        d_id = self.liststore_domain[path][0]
        dns = api.DomainIsmark(self.__mail, self.__pswd, d_id, is_mark=m)
        dns()
        if self.res_code(dns.code, dns.message) == True:
            self.liststore_domain.set_value(i, 1, not v)
    #修改备注
    def __domain_remark(self, cell, path, new_text, data=None):
        i = self.liststore_domain.get_iter(path)
        v = self.liststore_domain[path][4]
        if v == new_text:
            return
        d_id = self.liststore_domain[path][0]
        dns = api.DomainRemark(self.__mail, self.__pswd, d_id, remark=new_text)
        dns()
        if self.res_code(dns.code, dns.message) == True:
            self.liststore_domain.set_value(i, 4, new_text)
    #双击列表
    def on_treeview_domain_row_activated(self, tree, path, col, data=None):
        d_id = self.liststore_domain[path][0]
        dns = api.RecordList(self.__mail, self.__pswd, domain_id=d_id)
        dns()
        if self.res_code(dns.code, dns.message) == True:
            self.label_rdomain.set_text("当前域名："+self.liststore_domain[path][2])
            self.__current_domain = d_id
            self.liststore_record.clear()
            for r in dns.records:
                l = []
                l.append(r["id"])
                l.append(r["name"])
                l.append(r["type"])
                l.append(r["line"])
                l.append(r["value"])
                l.append(r["mx"])
                l.append(r["ttl"])
                s = "启用" if r["enabled"] == '1' else "暂停"
                l.append(s)
                l.append(r["remark"])
                self.liststore_record.append(l)
    #暂停/启用域名
    def on_button_dpause_clicked(self, widget, data=None):
        select = self.treeview_domain.get_selection()
        l =  select.get_selected()
        if l[1] == None:
            ErrorDialog(self.window, "请先选择要操作的域名！")
            return
        path = self.liststore_domain.get_string_from_iter(l[1])
        s = "enable" if self.liststore_domain[path][3] == "暂停" else "disable"
        d_id = self.liststore_domain[path][0]
        dns = api.DomainStatus(self.__mail, self.__pswd, d_id, status=s)
        dns()
        if self.res_code(dns.code, dns.message) == True:
            self.liststore_domain[path][3] = "启用" if s == "enable" else "暂停"
    #删除域名
    def on_button_ddel_clicked(self, widget, data=None):
        select = self.treeview_domain.get_selection()
        l =  select.get_selected()
        if l[1] == None:
            ErrorDialog(self.window, "请先选择要操作的域名！")
            return
        dialog = QueDialog(self.window, "删除域名同时会将该域名下所有记录删除，确定要删除吗?")
        if dialog.res != -8:
            return
        path = self.liststore_domain.get_string_from_iter(l[1])
        d_id = self.liststore_domain[path][0]
        dns = api.DomainRemove(self.__mail, self.__pswd, d_id)
        dns()
        if self.res_code(dns.code, dns.message) == True:
            self.liststore_domain.remove(l[1])
            if self.__current_domain == d_id:
                self.__current_domain = None
                self.liststore_record.clear()
                self.label_rdomain.set_text("<请先选择域名>")
    #刷新域名列表
    def on_button_dfresh_clicked(self, widget, data=None):
        self.liststore_domain.clear()
        dns = api.DomainList(self.__mail, self.__pswd, type="all")
        dns()
        if self.res_code(dns.code, dns.message) == True:
            for domain in dns.domains:
                d = []
                d.append(domain["id"])
                m = True if domain["is_mark"] == "yes" else False
                d.append(m)
                d.append(domain["name"])
                m = "启用" if domain["status"] == "enable" else "暂停"
                d.append(m)
                d.append(domain["remark"])
                self.liststore_domain.append(d)
    #添加域名按钮
    def on_button_dadd_clicked(self, widget, data=None):
        domain = widget.get_text()
        if len(domain) == 0:
            ErrorDialog(self.window, "请先输入要添加的域名！")
            return
        dns = api.DomainCreate(self.__mail, self.__pswd, domain)
        dns()
        if self.res_code(dns.code, dns.message) == True:
            self.liststore_domain.append([dns.id, False, dns.punycode, "启用", ""])
            widget.set_text("")

    #记录操作
    #暂停/启用 记录
    def on_button_rpause_clicked(self, widget, data=None):
        select = self.treeview_record.get_selection()
        l =  select.get_selected()
        if l[1] == None:
            ErrorDialog(self.window, "请先选择要操作的记录！")
            return
        path = self.liststore_record.get_string_from_iter(l[1])
        s = "enable" if self.liststore_record[path][7] == "暂停" else "disable"
        d_id = self.__current_domain
        r_id = self.liststore_record[path][0]
        dns = api.RecordStatus(self.__mail, self.__pswd, domain_id=d_id, record_id=r_id, status=s)
        dns()
        if self.res_code(dns.code, dns.message) == True:
            self.liststore_record[path][7] = "启用" if s == "enable" else "暂停"
    #删除记录
    def on_button_rdel_clicked(self, widget, data=None):
        select = self.treeview_record.get_selection()
        l =  select.get_selected()
        if l[1] == None:
            ErrorDialog(self.window, "请先选择要操作的域名！")
            return
        dialog = QueDialog(self.window, "确定要删除吗?")
        if dialog.res != -8:
            return
        path = self.liststore_record.get_string_from_iter(l[1])
        d_id = self.__current_domain
        r_id = self.liststore_record[path][0]
        dns = api.RecordRemove(self.__mail, self.__pswd, domain_id=d_id, record_id=r_id)
        dns()
        if self.res_code(dns.code, dns.message) == True:
            self.liststore_record.remove(l[1])
    #添加记录
    def on_button_radd_clicked(self, widget, data=None):
        host = self.entry_host.get_text()
        value = self.entry_value.get_text()
        mx = self.entry_mx.get_text()
        ttl = self.entry_ttl.get_text()
        rtype = self.combobox_rtype.get_active_text()
        ltype = self.combobox_ltype.get_active_text()
        if self.__current_domain == None:
            ErrorDialog(self.window, "请先选择域名！")
            return
        if host == "" or value == "" or mx == "" or ttl == "" or rtype == "" or ltype == "":
            ErrorDialog(self.window, "主机名、记录类型、线路类型、记录值不能为空！")
            return
        d_id = self.__current_domain
        dns = api.RecordCreate(self.__mail, self.__pswd, domain_id=d_id,
                            sub_domain=host, record_type=rtype, record_line=ltype,
                            value=value, mx=mx, ttl=ttl)
        dns()
        if self.res_code(dns.code, dns.message) == True:
            self.liststore_record.append([dns.id, dns.name, rtype, ltype, value, mx, ttl, "启用", ""])
            self.entry_host.set_text("")
            self.entry_value.set_text("")
            self.entry_mx.set_text("")
            self.entry_ttl.set_text("")
    #修改记录
    def __record_change(self, path):
        dns = api.RecordModify(self.__mail, self.__pswd, domain_id=self.__current_domain,
                               record_id=self.liststore_record[path][0],
                               sub_domain=self.liststore_record[path][1],
                               record_type=self.liststore_record[path][2],
                               record_line=self.liststore_record[path][3],
                               value=self.liststore_record[path][4],
                               mx=self.liststore_record[path][5],
                               ttl=self.liststore_record[path][6])
        dns()
        return self.res_code(dns.code, dns.message)
    #修改记录/线路类型
    def __record_changed(self, com, path, new_iter, data=None):
        if data == 2:
            v = self.liststore_recordtype.get_value(new_iter, 0)
        elif data == 3:
            v = self.liststore_linetype.get_value(new_iter, 0)
        old_text = self.liststore_record[path][data]
        self.liststore_record[path][data] = v
        if self.__record_change(path) == False:
            self.liststore_record[path][data] = old_text
    #修改记录
    def __record_modify(self, cell, path, new_text, data=None):
        if new_text == "":
            ErrorDialog(self.window, "请输入内容！")
            return
        old_text = self.liststore_record[path][data]
        if old_text != new_text:
            if data == 8:
                d_id = self.__current_domain
                r_id = self.liststore_record[path][0]
                dns = api.RecordRemark(self.__mail, self.__pswd, domain_id=d_id,record_id=r_id, remark=new_text)
                dns()
                if self.res_code(dns.code, dns.message) == True:
                    self.liststore_record[path][data] = new_text
                return
            self.liststore_record[path][data] = new_text
            if self.__record_change(path) == False:
                self.liststore_record[path][data] = old_text
            
    
if __name__ == "__main__":
    gtk.gdk.threads_init()
    Login()
    gtk.threads_enter()
    gtk.main()
    gtk.threads_leave()
    

