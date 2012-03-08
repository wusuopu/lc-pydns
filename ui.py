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
# @QQ: 346202141
# @ICQ: wosuopu@gmail.com
# @时间(date): 2012-03-08
# 


login = """
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <requires lib="gtk+" version="2.24"/>
  <!-- interface-naming-policy project-wide -->
  <object class="GtkWindow" id="window_login">
    <property name="width_request">300</property>
    <property name="height_request">150</property>
    <property name="can_focus">False</property>
    <property name="title" translatable="yes">LC-pydns v1.0</property>
    <property name="resizable">False</property>
    <property name="window_position">center</property>
    <property name="icon">logo.ico</property>
    <property name="opacity">0.90000000000000002</property>
    <signal name="destroy" handler="main_quit" swapped="no"/>
    <child>
      <object class="GtkFixed" id="fixed_login">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <child>
          <object class="GtkLabel" id="label_mail">
            <property name="width_request">100</property>
            <property name="height_request">25</property>
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="label" translatable="yes">邮箱：</property>
          </object>
          <packing>
            <property name="x">15</property>
            <property name="y">25</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel" id="label_pswd">
            <property name="width_request">100</property>
            <property name="height_request">25</property>
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="label" translatable="yes">密码：</property>
          </object>
          <packing>
            <property name="x">15</property>
            <property name="y">70</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="entry_mail">
            <property name="width_request">150</property>
            <property name="height_request">25</property>
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="invisible_char">●</property>
            <property name="primary_icon_activatable">False</property>
            <property name="secondary_icon_activatable">False</property>
            <property name="primary_icon_sensitive">True</property>
            <property name="secondary_icon_sensitive">True</property>
          </object>
          <packing>
            <property name="x">120</property>
            <property name="y">25</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="entry_pswd">
            <property name="width_request">150</property>
            <property name="height_request">25</property>
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="visibility">False</property>
            <property name="invisible_char">●</property>
            <property name="primary_icon_activatable">False</property>
            <property name="secondary_icon_activatable">False</property>
            <property name="primary_icon_sensitive">True</property>
            <property name="secondary_icon_sensitive">True</property>
          </object>
          <packing>
            <property name="x">120</property>
            <property name="y">70</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="button_login">
            <property name="label" translatable="yes">登陆</property>
            <property name="use_action_appearance">False</property>
            <property name="width_request">80</property>
            <property name="height_request">25</property>
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="receives_default">True</property>
            <accelerator key="Return" signal="clicked"/>
            <signal name="clicked" handler="on_button_login_clicked" swapped="no"/>
          </object>
          <packing>
            <property name="x">113</property>
            <property name="y">110</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>
"""

ui = """
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <requires lib="gtk+" version="2.24"/>
  <!-- interface-naming-policy project-wide -->
  <object class="GtkListStore" id="liststore_domain">
    <columns>
      <!-- column-name id -->
      <column type="gchararray"/>
      <!-- column-name 标星 -->
      <column type="gboolean"/>
      <!-- column-name 域名 -->
      <column type="gchararray"/>
      <!-- column-name 状态 -->
      <column type="gchararray"/>
      <!-- column-name 备注 -->
      <column type="gchararray"/>
    </columns>
  </object>
  <object class="GtkListStore" id="liststore_linetype">
    <columns>
      <!-- column-name 线路类型 -->
      <column type="gchararray"/>
    </columns>
    <data>
      <row>
        <col id="0" translatable="yes">默认</col>
      </row>
      <row>
        <col id="0" translatable="yes">电信</col>
      </row>
      <row>
        <col id="0" translatable="yes">联通</col>
      </row>
      <row>
        <col id="0" translatable="yes">教育网</col>
      </row>
      <row>
        <col id="0" translatable="yes">移动</col>
      </row>
      <row>
        <col id="0" translatable="yes">铁通</col>
      </row>
      <row>
        <col id="0" translatable="yes">国内</col>
      </row>
      <row>
        <col id="0" translatable="yes">国外</col>
      </row>
      <row>
        <col id="0" translatable="yes">搜索引擎</col>
      </row>
      <row>
        <col id="0" translatable="yes">百度</col>
      </row>
      <row>
        <col id="0" translatable="yes">Google</col>
      </row>
      <row>
        <col id="0" translatable="yes">有道</col>
      </row>
      <row>
        <col id="0" translatable="yes">必应</col>
      </row>
      <row>
        <col id="0" translatable="yes">搜搜</col>
      </row>
      <row>
        <col id="0" translatable="yes">搜狗</col>
      </row>
    </data>
  </object>
  <object class="GtkListStore" id="liststore_record">
    <columns>
      <!-- column-name rid -->
      <column type="gchararray"/>
      <!-- column-name 主机 -->
      <column type="gchararray"/>
      <!-- column-name 记录类型 -->
      <column type="gchararray"/>
      <!-- column-name 线路类型 -->
      <column type="gchararray"/>
      <!-- column-name 记录值 -->
      <column type="gchararray"/>
      <!-- column-name MX优先级 -->
      <column type="gchararray"/>
      <!-- column-name TTL -->
      <column type="gchararray"/>
      <!-- column-name 状态 -->
      <column type="gchararray"/>
      <!-- column-name 备注 -->
      <column type="gchararray"/>
    </columns>
  </object>
  <object class="GtkListStore" id="liststore_recordtype">
    <columns>
      <!-- column-name 记录类型 -->
      <column type="gchararray"/>
    </columns>
    <data>
      <row>
        <col id="0" translatable="yes">A</col>
      </row>
      <row>
        <col id="0" translatable="yes">CNAME</col>
      </row>
      <row>
        <col id="0" translatable="yes">MX</col>
      </row>
      <row>
        <col id="0" translatable="yes">TXT</col>
      </row>
      <row>
        <col id="0" translatable="yes">NS</col>
      </row>
      <row>
        <col id="0" translatable="yes">AAAA</col>
      </row>
      <row>
        <col id="0" translatable="yes">SRV</col>
      </row>
      <row>
        <col id="0" translatable="yes">URL</col>
      </row>
    </data>
  </object>
  <object class="GtkWindow" id="Mainwindow">
    <property name="can_focus">False</property>
    <property name="title" translatable="yes">LC-pydns v1.0</property>
    <property name="window_position">center</property>
    <property name="icon">logo.ico</property>
    <property name="opacity">0.90000000000000002</property>
    <property name="mnemonics_visible">False</property>
    <signal name="delete-event" handler="main_quit" swapped="no"/>
    <child>
      <object class="GtkVBox" id="vbox1">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <child>
          <object class="GtkVBox" id="vbox2">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <child>
              <object class="GtkLabel" id="label_info">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="xalign">0.0099999997764825821</property>
                <property name="label" translatable="yes">&lt;b&gt;个人信息：&lt;/b&gt;</property>
                <property name="use_markup">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkHBox" id="hbox1">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <child>
                  <object class="GtkLabel" id="label_email0">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="xalign">0.0099999997764825821</property>
                    <property name="label" translatable="yes">&lt;b&gt;邮箱：&lt;/b&gt;</property>
                    <property name="use_markup">True</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="padding">5</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="label_info_email">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="xalign">0.10000000149011612</property>
                    <property name="label" translatable="yes">mail</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="padding">5</property>
                    <property name="position">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="label1">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="xalign">0.10000000149011612</property>
                    <property name="label" translatable="yes">&lt;b&gt;邮箱认证：&lt;/b&gt;</property>
                    <property name="use_markup">True</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="padding">5</property>
                    <property name="position">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="label_info_mailverified">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="xalign">0.10000000149011612</property>
                    <property name="label" translatable="yes">mail_verified</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="padding">5</property>
                    <property name="position">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="label2">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="xalign">0.10000000149011612</property>
                    <property name="label" translatable="yes">&lt;b&gt;账号状态：&lt;/b&gt;</property>
                    <property name="use_markup">True</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="padding">5</property>
                    <property name="position">4</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="label_info_status">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="xalign">0.10000000149011612</property>
                    <property name="label" translatable="yes">status</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="padding">5</property>
                    <property name="position">5</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkHSeparator" id="hseparator1">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="padding">5</property>
                <property name="position">2</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">False</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkHPaned" id="hpaned">
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <child>
              <object class="GtkViewport" id="viewport1">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <child>
                  <object class="GtkVBox" id="vbox3">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkHBox" id="hbox2">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="spacing">5</property>
                        <child>
                          <object class="GtkLabel" id="label3">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">&lt;b&gt;我的域名&lt;/b&gt;</property>
                            <property name="use_markup">True</property>
                          </object>
                          <packing>
                            <property name="expand">False</property>
                            <property name="fill">False</property>
                            <property name="padding">15</property>
                            <property name="position">0</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkButton" id="button_dpause">
                            <property name="label" translatable="yes">暂停/启用</property>
                            <property name="use_action_appearance">False</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <signal name="clicked" handler="on_button_dpause_clicked" swapped="no"/>
                          </object>
                          <packing>
                            <property name="expand">False</property>
                            <property name="fill">False</property>
                            <property name="position">1</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkButton" id="button_dfresh">
                            <property name="label" translatable="yes">刷新</property>
                            <property name="use_action_appearance">False</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <signal name="clicked" handler="on_button_dfresh_clicked" swapped="no"/>
                          </object>
                          <packing>
                            <property name="expand">False</property>
                            <property name="fill">False</property>
                            <property name="position">2</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkButton" id="button_ddel">
                            <property name="label" translatable="yes">删除</property>
                            <property name="use_action_appearance">False</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <signal name="clicked" handler="on_button_ddel_clicked" swapped="no"/>
                          </object>
                          <packing>
                            <property name="expand">False</property>
                            <property name="fill">False</property>
                            <property name="position">3</property>
                          </packing>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">False</property>
                        <property name="fill">False</property>
                        <property name="position">0</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkScrolledWindow" id="scrolledwindow1">
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="hscrollbar_policy">automatic</property>
                        <property name="vscrollbar_policy">automatic</property>
                        <child>
                          <object class="GtkTreeView" id="treeview_domain">
                            <property name="width_request">220</property>
                            <property name="height_request">400</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="model">liststore_domain</property>
                            <property name="enable_search">False</property>
                            <property name="search_column">0</property>
                            <property name="show_expanders">False</property>
                            <property name="enable_grid_lines">horizontal</property>
                            <signal name="row-activated" handler="on_treeview_domain_row_activated" swapped="no"/>
                          </object>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">True</property>
                        <property name="fill">True</property>
                        <property name="position">1</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkHBox" id="hbox4">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <child>
                          <object class="GtkLabel" id="label5">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">输入要解析的域名：</property>
                          </object>
                          <packing>
                            <property name="expand">False</property>
                            <property name="fill">False</property>
                            <property name="position">0</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkEntry" id="entry1">
                            <property name="width_request">110</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="invisible_char">●</property>
                            <property name="primary_icon_activatable">False</property>
                            <property name="secondary_icon_activatable">False</property>
                            <property name="primary_icon_sensitive">True</property>
                            <property name="secondary_icon_sensitive">True</property>
                          </object>
                          <packing>
                            <property name="expand">False</property>
                            <property name="fill">False</property>
                            <property name="position">1</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkButton" id="button_dadd">
                            <property name="label" translatable="yes">添加</property>
                            <property name="use_action_appearance">False</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <signal name="clicked" handler="on_button_dadd_clicked" object="entry1" swapped="no"/>
                          </object>
                          <packing>
                            <property name="expand">False</property>
                            <property name="fill">False</property>
                            <property name="position">2</property>
                          </packing>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">False</property>
                        <property name="fill">False</property>
                        <property name="padding">5</property>
                        <property name="position">2</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkLabel" id="label4">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="xalign">0</property>
                        <property name="yalign">0</property>
                        <property name="xpad">5</property>
                        <property name="label" translatable="yes">添加域名后再到域名注册的地方将 DNS 修改为：
f1g1ns1.dnspod.net
f1g1ns2.dnspod.net</property>
                        <property name="selectable">True</property>
                        <attributes>
                          <attribute name="foreground" value="#ffff00000000"/>
                        </attributes>
                      </object>
                      <packing>
                        <property name="expand">True</property>
                        <property name="fill">True</property>
                        <property name="position">3</property>
                      </packing>
                    </child>
                  </object>
                </child>
              </object>
              <packing>
                <property name="resize">False</property>
                <property name="shrink">True</property>
              </packing>
            </child>
            <child>
              <object class="GtkViewport" id="viewport2">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <child>
                  <object class="GtkVBox" id="vbox4">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkHBox" id="hbox3">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="spacing">5</property>
                        <child>
                          <object class="GtkLabel" id="label_rdomain">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">&lt;请先选择域名&gt;</property>
                          </object>
                          <packing>
                            <property name="expand">False</property>
                            <property name="fill">False</property>
                            <property name="padding">15</property>
                            <property name="position">0</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkButton" id="button_rpause">
                            <property name="label" translatable="yes">暂停/启用</property>
                            <property name="use_action_appearance">False</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <signal name="clicked" handler="on_button_rpause_clicked" swapped="no"/>
                          </object>
                          <packing>
                            <property name="expand">False</property>
                            <property name="fill">False</property>
                            <property name="position">1</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkButton" id="button_rdel">
                            <property name="label" translatable="yes">删除</property>
                            <property name="use_action_appearance">False</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <signal name="clicked" handler="on_button_rdel_clicked" swapped="no"/>
                          </object>
                          <packing>
                            <property name="expand">False</property>
                            <property name="fill">False</property>
                            <property name="position">2</property>
                          </packing>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">False</property>
                        <property name="fill">False</property>
                        <property name="position">0</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkScrolledWindow" id="scrolledwindow2">
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="hscrollbar_policy">automatic</property>
                        <property name="vscrollbar_policy">automatic</property>
                        <child>
                          <object class="GtkTreeView" id="treeview_record">
                            <property name="width_request">450</property>
                            <property name="height_request">400</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="model">liststore_record</property>
                            <property name="enable_search">False</property>
                            <property name="search_column">0</property>
                            <property name="show_expanders">False</property>
                            <property name="enable_grid_lines">both</property>
                          </object>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">True</property>
                        <property name="fill">True</property>
                        <property name="position">1</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkTable" id="table1">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="n_rows">3</property>
                        <property name="n_columns">6</property>
                        <child>
                          <object class="GtkLabel" id="label7">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">主机</property>
                          </object>
                          <packing>
                            <property name="top_attach">1</property>
                            <property name="bottom_attach">2</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkLabel" id="label8">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">记录类型</property>
                          </object>
                          <packing>
                            <property name="left_attach">1</property>
                            <property name="right_attach">2</property>
                            <property name="top_attach">1</property>
                            <property name="bottom_attach">2</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkLabel" id="label9">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">线路类型</property>
                          </object>
                          <packing>
                            <property name="left_attach">2</property>
                            <property name="right_attach">3</property>
                            <property name="top_attach">1</property>
                            <property name="bottom_attach">2</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkLabel" id="label10">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">记录值</property>
                          </object>
                          <packing>
                            <property name="left_attach">3</property>
                            <property name="right_attach">4</property>
                            <property name="top_attach">1</property>
                            <property name="bottom_attach">2</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkLabel" id="label11">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">MX</property>
                          </object>
                          <packing>
                            <property name="left_attach">4</property>
                            <property name="right_attach">5</property>
                            <property name="top_attach">1</property>
                            <property name="bottom_attach">2</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkLabel" id="label12">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">TTL</property>
                          </object>
                          <packing>
                            <property name="left_attach">5</property>
                            <property name="right_attach">6</property>
                            <property name="top_attach">1</property>
                            <property name="bottom_attach">2</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkEntry" id="entry_host">
                            <property name="width_request">50</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="invisible_char">●</property>
                            <property name="primary_icon_activatable">False</property>
                            <property name="secondary_icon_activatable">False</property>
                            <property name="primary_icon_sensitive">True</property>
                            <property name="secondary_icon_sensitive">True</property>
                          </object>
                          <packing>
                            <property name="top_attach">2</property>
                            <property name="bottom_attach">3</property>
                            <property name="x_options"></property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkEntry" id="entry_value">
                            <property name="width_request">50</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="invisible_char">●</property>
                            <property name="invisible_char_set">True</property>
                            <property name="primary_icon_activatable">False</property>
                            <property name="secondary_icon_activatable">False</property>
                            <property name="primary_icon_sensitive">True</property>
                            <property name="secondary_icon_sensitive">True</property>
                          </object>
                          <packing>
                            <property name="left_attach">3</property>
                            <property name="right_attach">4</property>
                            <property name="top_attach">2</property>
                            <property name="bottom_attach">3</property>
                            <property name="x_options"></property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkEntry" id="entry_mx">
                            <property name="width_request">50</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="invisible_char">●</property>
                            <property name="text" translatable="yes">5</property>
                            <property name="invisible_char_set">True</property>
                            <property name="primary_icon_activatable">False</property>
                            <property name="secondary_icon_activatable">False</property>
                            <property name="primary_icon_sensitive">True</property>
                            <property name="secondary_icon_sensitive">True</property>
                          </object>
                          <packing>
                            <property name="left_attach">4</property>
                            <property name="right_attach">5</property>
                            <property name="top_attach">2</property>
                            <property name="bottom_attach">3</property>
                            <property name="x_options"></property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkEntry" id="entry_ttl">
                            <property name="width_request">50</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="invisible_char">●</property>
                            <property name="text" translatable="yes">600</property>
                            <property name="invisible_char_set">True</property>
                            <property name="primary_icon_activatable">False</property>
                            <property name="secondary_icon_activatable">False</property>
                            <property name="primary_icon_sensitive">True</property>
                            <property name="secondary_icon_sensitive">True</property>
                          </object>
                          <packing>
                            <property name="left_attach">5</property>
                            <property name="right_attach">6</property>
                            <property name="top_attach">2</property>
                            <property name="bottom_attach">3</property>
                            <property name="x_options"></property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkLabel" id="label6">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="xalign">0</property>
                            <property name="label" translatable="yes">添加记录：</property>
                            <attributes>
                              <attribute name="weight" value="heavy"/>
                            </attributes>
                          </object>
                        </child>
                        <child>
                          <object class="GtkButton" id="button_radd">
                            <property name="label" translatable="yes">添加</property>
                            <property name="use_action_appearance">False</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <signal name="clicked" handler="on_button_radd_clicked" swapped="no"/>
                          </object>
                          <packing>
                            <property name="left_attach">4</property>
                            <property name="right_attach">5</property>
                            <property name="x_options"></property>
                            <property name="y_options"></property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkComboBox" id="combobox_rtype">
                            <property name="width_request">80</property>
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="model">liststore_recordtype</property>
                            <property name="has_entry">True</property>
                            <property name="entry_text_column">0</property>
                          </object>
                          <packing>
                            <property name="left_attach">1</property>
                            <property name="right_attach">2</property>
                            <property name="top_attach">2</property>
                            <property name="bottom_attach">3</property>
                            <property name="x_options"></property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkComboBox" id="combobox_ltype">
                            <property name="width_request">80</property>
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="model">liststore_linetype</property>
                            <property name="has_entry">True</property>
                            <property name="entry_text_column">0</property>
                          </object>
                          <packing>
                            <property name="left_attach">2</property>
                            <property name="right_attach">3</property>
                            <property name="top_attach">2</property>
                            <property name="bottom_attach">3</property>
                            <property name="x_options"></property>
                          </packing>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">True</property>
                        <property name="fill">True</property>
                        <property name="position">2</property>
                      </packing>
                    </child>
                  </object>
                </child>
              </object>
              <packing>
                <property name="resize">True</property>
                <property name="shrink">True</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">True</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
        <child>
          <object class="GtkHSeparator" id="hseparator2">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="padding">5</property>
            <property name="position">2</property>
          </packing>
        </child>
        <child>
          <object class="GtkStatusbar" id="statusbar">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="spacing">5</property>
            <child>
              <object class="GtkLabel" id="label_status">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">作者：&lt;b&gt;龙昌&lt;/b&gt; 博客：&lt;b&gt;http://www.xefan.com&lt;/b&gt;</property>
                <property name="use_markup">True</property>
                <property name="selectable">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">0</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">False</property>
            <property name="position">3</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>
"""
