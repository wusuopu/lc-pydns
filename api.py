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
# @文件名(file): api.py
# @作者(author): 龙昌锦(LongChangjin)
# @博客(blog): http://www.xefan.com
# @邮箱(mail): admin@xefan.com
# @时间(date): 2012-02-28
# 
import httplib, urllib
try: import json
except: import simplejson as json
import socket
import re


class Error(StandardError):
    def __init__(self, code, message):
        self.code = code
        self.message = message
        StandardError.__init__(self, message)

class DnsApi:
    """Api base class"""
    def __init__(self, login_email, login_pswd, **kw):
        self.message = ""
        self.base_url = "dnsapi.cn"
        self.params = {
            "login_email":login_email,
            "login_password":login_pswd,
            "format":"json"
        }
        self.params.update(kw)
        self.path = None

    def request(self, **kw):
        """
            request function,POST methon
            -1: login fail
            -8: login too often
            1: success
            2: only allow post
            3: unknown error
        """
        self.params.update(kw)
        if self.__class__.__name__ == "DnsApi":
            return
        name = re.sub(r'([A-Z])', r'.\1', self.__class__.__name__)
        self.path = "/" + name[1:]
        conn = httplib.HTTPSConnection(self.base_url)
        headers = {"Content-type":"application/x-www-form-urlencoded", "Accept":"text/json", "User-Agent":"LC-pydns/1.0 (admin@longchangjin.cn)"}
        conn.request("POST", self.path, urllib.urlencode(self.params), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        ret = json.loads(data)
        if ret.get("status", {}).get("code") == "1":
            return ret
        else:
            #raise Exception(ret.get("status", {}).get("code"))
            raise Error(ret.get("status", {}).get("code"), ret.get("status", {}).get("message"))


#获取API版本号
class InfoVersion(DnsApi):
    """get API version"""
    def __init__(self, email, pswd, **kw):
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        try:
            ret = self.request()
            self.version = ret['status']['message']
            self.code = ret['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#用户Api
#获取用户信息
class UserDetail(DnsApi):
    """get user info"""
    def __init__(self, email, pswd, **kw):
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        try:
            ret = self.request()
            self.code = ret['status']['code']

            user = ret['info']['user']
            self.id = user['id']
            self.email = user['email']
            self.status = user['status']
            self.email_verified = user['email_verified']
            self.tel_verified = user['telephone_verified']
            self.real_name = user['real_name']
            self.user_type = user['user_type']
            self.tel = user['telephone']
            self.im = user['im']
            self.balance = user['balance']
            self.smsbalance = user['smsbalance']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#修改用户
class UserModify(DnsApi):
    """update user info"""
    def __init__(self, email, pswd, name, tel, im, **kw):
        """
        email:login_email
        pswd:login_password
        name:real_name,want to changed value
        tel:telephone,want to changed value
        im:qq,want to changed value
        """
        kw.update(dict(real_name=name,
                       telephone=tel,
                       im=im))
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 8:telephone is error
        code 9:qq is error
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#修改密码
class UserpasswdModify(DnsApi):
    """changed user password"""
    def __init__(self, email, pswd, oldpw, newpd, **kw):
        """
        oldpw:old_password
        newpw:new_password
        """
        kw.update(dict(old_password=oldpw,
                       new_password=newpd))
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 8:old password is error
        code 9:new password is error
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#修改邮箱
class UseremailModify(DnsApi):
    """changed user email"""
    def __init__(self, email, pswd, old_mail, new_mail, passwd, **kw):
        """
        old_mail: old email
        new_mail: new email
        passwd:the password
        """
        kw.update(dict(old_email=old_mail,
                       new_email=new_mail,
                       password=passwd))
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 8:old email is error
        code 9:new email is error
        code 10:password is error
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#获取用户日志
class UserLog(DnsApi):
    """get user log"""
    def __init__(self, email, pswd, **kw):
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        try:
            ret = self.request()
            self.code = ret['status']['code']
            self.log = ret['log']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#获取手机验证码
class TelephoneverifyCode(DnsApi):
    """get telephone verify code"""
    def __init__(self, email, pswd, tel, **kw):
        """
        tel: telephone number
        """
        kw.update(dict(telephone=tel))
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 4:user has verified
        code 5:tel is invalid
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            self.verify_code = ret['user']['verify_code']
            self.verify_desc = ret['user']['verify_desc']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'


#域名Api
#添加新域名
class DomainCreate(DnsApi):
    """add new domain"""
    def __init__(self, email, pswd, domain, **kw):
        """
        domain:no www,eg:longchangjin.cn
        group_id:[]
        is_mark:[yes|no]
        """
        kw.update(dict(domain=domain))
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 6:domain is invalid
        code 7:domain has existed
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            self.id = ret['domain']['id']
            self.punycode = ret['domain']['punycode']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#获取域名列表
class DomainList(DnsApi):
    """get domains list"""
    def __init__(self, email, pswd, **kw):
        """
        type:{all,mine,share,ismark,pause}
        offset:first is NO. 0
        length:total item number
        group_id:get the group's domain
        """
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 6:offset is invalid
        code 7:length is invalid
        code 9:list is empty
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            
            info = ret['info']
            self.domain_total = info['domain_total']
            self.all_total = info['all_total']
            self.mine_total = info['mine_total']
            self.share_total = info['share_total']
            self.ismark_total = info['ismark_total']
            self.pause_total = info['pause_total']
            self.domains = ret['domains']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#删除域名
class DomainRemove(DnsApi):
    """remove domain"""
    def __init__(self, email, pswd, domain_id, **kw):
        """
        domain_id:get from DomainList
        """
        kw.update(dict(domain_id=domain_id))
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:doamin has been disable
        code 6:domain_id is error
        code 7:domain is locked
        code 8:vip domain can't remove
        code 9:is not the owner of domain
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#设置域名状态
class DomainStatus(DnsApi):
    """set doamin status"""
    def __init__(self, email, pswd, domain_id, **kw):
        """
        domain_id:get from DomainList
        status:{enable,disable}
        """
        kw.update(dict(domain_id=domain_id))
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:domain has been disable
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domain_id is error
        code 7:domain is locked
        code 8:is not the owner of domain
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#获取域名日志
class DomainLog(DnsApi):
    """get domain log"""
    def __init__(self, email, pswd, domain_id, **kw):
        """
        domain_id:get from DomainList
        """
        kw.update(dict(domain_id=domain_id))
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domain_id is error
        code 8:is not the owner of domain
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            self.log = ret['log']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#
#添加域名共享
class DomainshareCreate(DnsApi):
    """set domain share"""
    def __init__(self, email, pswd, domain_id, mail, mode, **kw):
        """
        domain_id:get from DomainList
        mail:share to mail
        mode:share mode,{r|rw}
        """
        kw.update({"domain_id":domain_id, "email":mail, "mode":mode})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:domain has been disable
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domain_id is error
        code 7:mail is error
        code 8:mail is not exist
        code 9:share is exist
        code 10:share count is max
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#域名共享列表
class DomainshareList(DnsApi):
    """get share list"""
    def __init__(self, email, pswd, domain_id, **kw):
        """
        domain_id:get from DomainList
        """
        kw.update({"domain_id":domain_id})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domain_id is error
        code 7:share is empty
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            self.share = ret['share']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#修改域名共享
class DomainshareModify(DnsApi):
    """change share"""
    def __init__(self, email, pswd, domain_id, mail, mode, **kw):
        """
        domain_id:get from DomainList
        mail:share to mail
        mode:share mode,{r|rw}
        """
        kw.update({"domain_id":domain_id, "email":mail, "mode":mode})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:domain has been disable
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domain_id is error
        code 7:mail is error
        code 8:mail is not exist
        code 9:share is not exist
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#删除域名共享
class DomainshareRemove(DnsApi):
    """remove share"""
    def __init__(self, email, pswd, domain_id, mail, **kw):
        """
        domain_id:get from DomainList
        mail:share to mode
        """
        kw.update({"domain_id":domain_id, "email":mail})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:domain has been disable
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domain_id is error
        code 7:mail is error
        code 8:mail is not exist
        code 9:share is not exist
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#
#域名过户
class DomainTransfer(DnsApi):
    """doamin transfer"""
    def __init__(self, email, pswd, domain_id, mail, **kw):
        """
        doamin_id:get from DomainList
        mail:transfer to mail
        """
        kw.update({"domain_id":domain_id, "email":mail})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:domain has been disable
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domain_id is error
        code 7:mail is error
        code 8:mail is not exist
        code 9:can't transfer to myself
        code 10:person domain can't transfer to enterprise
        code 11:enterprise domain can;t transfer to person
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#锁定域名
class DomainLock(DnsApi):
    """lock domain"""
    def __init__(self, email, pswd, domain_id, days, **kw):
        """
        domain_id:get from DomainList
        days:lock days
        """
        kw.update({"domain_id":domain_id, "days":days})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:domain has been disable
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domain_id is error
        code 7:is not the owner of domain
        code 8:days is error
        code 9:days is overtop limit
        code 21:domaim has been locked
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']

            lock = ret['lock']
            self.domain_id = lock['domain_id']
            self.lock_code = lock['lock_code']
            self.lock_end = lock['lock_end']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#锁定状态
class DomainLockstatus(DnsApi):
    """get lock status"""
    def __init__(self, email, pswd, domain_id, **kw):
        """
        doamin_id:get from DomainList
        """
        kw.update({"domain_id":domain_id})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:domain has been disable
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domain_id is error
        code 7:domain is not locked
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']

            lock = ret['lock']
            self.lock_status = lock['lock_status']
            self.start_at = lock['start_at']
            self.end_at = lock['end_at']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#锁定解锁
class DomainUnlock(DnsApi):
    """unlock"""
    def __init__(self, email, pswd, domain_id, lock_code, **kw):
        """
        domain_id:get from DomainList
        lock_code:domain lock code
        """
        kw.update({"domain_id":domain_id, "lock_code":lock_code})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:domain has been disable
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domain_id is error
        code 7:is not the owner of domain
        code 8:doamin is not locked
        code 9:lock_code is error
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#域名绑定列表
class DomainaliasList(DnsApi):
    def __init__(self, email, pswd, domain_id, **kw):
        """
        domain_id:get from DomainList
        """
        kw.update({"domain_id":domain_id})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domain_id is error
        code 7:alias is empty
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            self.alias = ret['alias']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#添加域名绑定
class DomainaliasCreate(DnsApi):
    """add doamin alias"""
    def __init__(self, email, pswd, domain_id, domain, **kw):
        """
        domain_id:get from DomainList
        domain:want to alias domain,no www
        """
        kw.update({"domain_id":domain_id, "domain":domain})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:domain has been disable
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domain_id is error
        code 7:domain is error
        code 8:domain has been added
        code 9:domain is been alias
        code 10:domaim count is max
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            self.alias = ret['alias']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#删除域名绑定
class DomainaliasRemove(DnsApi):
    """remove domain alias"""
    def __init__(self, email, pswd, domain_id, alias_id, **kw):
        """
        domain_id:get from DomainList
        alias_id:get from DomainaliasList
        """
        kw.update({"domain_id":domain_id, "alias_id":alias_id})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:domain has been disable
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domain_id is error
        code 7:alias_id is error
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#获取域名分组
class DomaingroupList(DnsApi):
    """get domain group"""
    def __init__(self, email, pswd, **kw):
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        group type has system and user;systen can't be changed
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            self.groups = ret['groups']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#添加域名分组
class DomaingroupCreate(DnsApi):
    """add domain group"""
    def __init__(self, email, pswd, group_name, **kw):
        """
        group_name:the new group name
        """
        kw.update({"group_name":group_name})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 7:group_name is error
        code 8:group_name is exist
        code 9:group count is max
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            self.groups = ret['groups']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#修改域名分组
class DomaingroupModify(DnsApi):
    """change group name"""
    def __init__(self, email, pswd, group_id, group_name, **kw):
        """
        group_id:the group id
        group_name:change to the name
        """
        kw.update({"group_id":group_id,"group_name":group_name})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 6:group_id is error
        code 7:group_name is error
        code 8:group_name is exist
        code 9:group count is max
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#删除域名分组
class DomaingroupRemove(DnsApi):
    """remove group"""
    def __init__(self, email, pswd, group_id, **kw):
        """
        group_id:the group id
        """
        kw.update({"group_id":group_id})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 6:group_id is error
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#设置域名分组
class DomainChangegroup(DnsApi):
    def __init__(self, email, pswd, domain_id, group_id, **kw):
        """
        domain_id:get from DomainList
        group_id:the group id
        """
        kw.update({"domain_id":domain_id,"group_id":group_id})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 6:domain_id is error
        code 7:group_id is error
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#设置域名星标
class DomainIsmark(DnsApi):
    def __init__(self, email, pswd, domain_id, is_mark, **kw):
        """
        domain_id:the domain id
        is_mark:{yes|no}
        """
        kw.update({"domain_id":domain_id,"is_mark":is_mark})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 6:domain_id is error
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#设置域名备注
class DomainRemark(DnsApi):
    def __init__(self, email, pswd, domain_id, remark, **kw):
        """
        domain_id:the domain id
        remark:the domain remark.if want to clear it,please submit null
        """
        kw.update({"domain_id":domain_id,"remark":remark})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 6:domain_id is error
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#获取域名权限
class DomainPurview(DnsApi):
    def __init__(self, email, pswd, domain_id, **kw):
        """
        domain_id:the domain id
        """
        kw.update({"domain_id":domain_id})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 6:domain_id is error
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            self.purview = ret['purview']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#记录Api
#获取等级允许的记录类型
class RecordType(DnsApi):
    """get the allow type"""
    def __init__(self, email, pswd, domain_grade, **kw):
        """
        domain_grade:{D_Free,D_Plus,D_Extra,D_Expert,D_Ultra}
        """
        kw.update({"domain_grade":domain_grade})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 6:domain_grade is error
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            self.types = ret['types']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#获取等级允许的记录线路
class RecordLine(DnsApi):
    """get the allow line"""
    def __init__(self, email, pswd, domain_grade, **kw):
        """
        domain_grade:{D_Free,D_Plus,D_Extra,D_Expert,D_Ultra}
        """
        kw.update({"domain_grade":domain_grade})
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 6:domain_grade is error
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            self.lines = ret['lines']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#添加记录
class RecordCreate(DnsApi):
    """add record"""
    def __init__(self, email, pswd, **kw):
        """
        domain_id:get from DomainList
        sub_domain:the host record,eg:www
        record_type:get from RecordType,upper,eg:CNAME
        record_line:get from RecordLine,Chinese,eg:默认
        value:the record value,eg:IP:200.200.200.200, CNAME:www.xefan.com
        mx:{1-20},only when record_type is MX
        ttl:{1-6048000}
        """
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:domain has been disable
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:argument is error
        code 7:is not the owner of domain
        code 21:domain is locked
        code 22:sub_domain is invalid
        code 23:sub domain count is max
        code 24:analyze error
        code 25:record count is max
        code 26:record_line is error
        code 27:record_type is error
        code 30:mx value is error
        code 31:URL record count is max
        code 32:NS record count is max
        code 33:AAAA record count is max
        code 34:record is invalid
        code 35:@ NS value must be defualt
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            record = ret['record']
            self.id = record['id']
            self.name = record['name']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#记录列表
class RecordList(DnsApi):
    """get record list"""
    def __init__(self, email, pswd, **kw):
        """
        domain_id:get from DomainList
        offset:the first is NO.0
        length:the total item number
        """
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domain_id is error
        code 7:offset is invalid
        code 8:length is invalid
        code 9:is not the owner of domain
        code 10:no item
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            self.total = ret['info']['record_total']
            self.records = ret['records']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#修改记录
class RecordModify(DnsApi):
    def __init__(self, email, pswd, **kw):
        """
        domain_id:get from DomainList
        record_id:get from RecordList
        sub_domain:the host record,eg:www
        record_type:get from RecordType,upper,eg:CNAME
        record_line:get from RecordLine,Chinese,eg:默认
        value:the record value,eg:IP:200.200.200.200, CNAME:www.xefan.com
        mx:{1-20},only when record_type is MX
        ttl:{1-6048000}
        """
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:domain has been disable
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domian_id is error
        code 7:is not the owner of domain
        code 8:record_id is error
        code 21:domain is locked
        code 22:sub_domain is invalid
        code 23:sub domain count is max
        code 24:analyze error
        code 25:record count is max
        code 26:record_line is error
        code 27:record_type is error
        code 29:ttl is too small
        code 30:mx value is error
        code 31:URL record count is max
        code 32:NS record count is max
        code 33:AAAA record count is max
        code 34:record is invalid
        code 35:IP is not allowed
        code 36:@ NS value must be defualt
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            record = ret['record']
            self.id = record['id']
            self.name = record['name']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#删除记录
class RecordRemove(DnsApi):
    def __init__(self, email, pswd, **kw):
        """
        domain_id:get from DomainList
        record_id:get from RecordList
        """
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:domain has been disable
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domian_id is error
        code 7:is not the owner of domain
        code 8:record_id is error
        code 21:domain is locked
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#更新动态DNS记录
class RecordDdns(DnsApi):
    def __init__(self, email, pswd, **kw):
        """
        domain_id:get from DomainList
        record_is:get from RecordList
        sub_domain:the host record,eg:www
        record_line:get from RecordLine,Chinese,eg:默认
        """
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:domain has been disable
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domian_id is error
        code 7:is not the owner of domain
        code 8:record_id is error
        code 21:domain is locked
        code 22:sub_domain is invalid
        code 23:sub domain count is max
        code 24:analyze error
        code 25:record count is max
        code 26:record_line is error
        """
        try:
            ret = self.request()
            self.code = ret['status']['code']
            record = ret['record']
            self.id = record['id']
            self.name = record['name']
            self.value = record['value']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#设置记录备注
class RecordRemark(DnsApi):
    def __init__(self, email, pswd, **kw):
        """
        domain_id:the domain id
        record_id:the record id
        remark:the doamin remark.If want to clear,please submit null
        """
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code 6:domain_id is error
        code 6:record_id is error
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'

#设置记录状态
class RecordStatus(DnsApi):
    def __init__(self, email, pswd, **kw):
        """
        domain_id:the domain id
        record_id:the record id
        status:{enable|disable}
        """
        DnsApi.__init__(self,email, pswd, **kw)

    def __call__(self):
        """
        code -15:domain has been disable
        code -7:enterprise user need to upgrade
        code -8:agent user need to upgrade
        code 6:domian_id is error
        code 7:is not the owner of domain
        code 8:record_id is error
        code 21:domain is locked
        """
        try:
            self.code = self.request()['status']['code']
        except Error, e:
            self.code = e.code
            self.message = e.message
        except Exception, e:
            self.code = '400'


