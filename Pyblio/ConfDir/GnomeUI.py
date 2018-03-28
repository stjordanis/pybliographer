# -*- coding: utf-8 -*-
# This file is part of pybliographer
#
# Copyright (C) 2018 Germán Poo-Caamaño <gpoo@gnome.org>
# Copyright (C) 1998-2004 Frederic GOBRY <gobry@pybliographer.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#

import gtk

from Pyblio import Config, Fields
from Pyblio.GnomeUI import  Editor

Config.define ('gnomeui/default', """ Graphical description of the
default field. """)

Config.define ('gnomeui/monospaced', """ A monospaced font, for native edition """)

def _text_get ():

    v = Config.get ('base/fields').data

    fields = [ x.name.lower() for x in v.values() if
               x.type is Fields.Text or x.type is Fields.LongText ]
    fields.sort ()

    return fields

def _on_multiline_select (item, multi, user):

    h = Config.get ('base/fields').data

    for k, v in multi.items ():

        if not h.has_key (k): continue
        
        if v: h [k].widget = Editor.Text
        else: h [k].widget = Editor.Entry
        
    return True


Config.define ('gnomeui/multiline',
               """ Fields displayed in a multi-line widget """,

               Config.Dict (Config.Element (_text_get),
                            Config.Boolean ()),

               hook = _on_multiline_select)


# --------------------------------------------------



Config.set ('gnomeui/monospaced',
            gtk.gdk.Font ('-*-*-*-r-normal-*-*-*-*-*-c-*-iso8859-1'))



h = Config.get ('base/fields').data

Fields.AuthorGroup.widget = Editor.AuthorGroup
Fields.Text.widget        = Editor.Entry
Fields.URL.widget         = Editor.URL
Fields.Reference.widget   = Editor.Reference

Fields.Date.widget        = Editor.Date
Fields.Date.justification = gtk.JUSTIFY_RIGHT

for f, w in (('author', 150),
             ('editor', 150),
             ('title',  200),
             ('booktitle', 200),
             ('date', 50),
             ('-author/editor-', 150),
             ('-author/title-', 250)):
    
    if not h.has_key (f): continue

    h [f].width = w
    

Config.set ('gnomeui/default',  (150, gtk.JUSTIFY_LEFT, Editor.Entry))

multi = {}

if h.has_key ('abstract'): multi ['abstract'] = 1

Config.set ('gnomeui/multiline', multi) 

