# -*- coding: utf-8 -*-
#
# This file is part of pybliographer
#
# Copyright (C) 2018 Germán Poo-Caamaño <gpoo@gnome.org>
# Copyright (C) 1998-2004 Frederic GOBRY <gobry@pybliographer.org
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
#

# Perform the first initialisation of Gnome, so that the options passed to
# the script are not passed to Gnome

import sys
import string

from gettext import gettext as _

# correctly identify the program
import pygtk
pygtk.require('2.0')

import gtk

from Pyblio import version

files = sys.argv[2:]
sys.argv = sys.argv[:2] + ['--'] + files


def _vnum(t):
    return string.join(map(str, t), '.')


ui_version = _("This is Pybliographic %s [Python %s, Gtk %s, PyGTK %s]") % (
    version.version, _vnum(sys.version_info[:3]),
    _vnum(gtk.gtk_version), _vnum(gtk.pygtk_version))

# clean up our garbage
sys.argv = sys.argv[:2] + files

del sys, files
