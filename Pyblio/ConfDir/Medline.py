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

from Pyblio import Config

Config.define ('medline/mapping',
               """ A hash table containing field names correspondances """,
               Config.Dict (Config.String (), Config.String ()))

Config.set ('medline/mapping', {
    'UI' : 'medlineref',
    'AU' : 'author',
    'DP' : 'date',
    'TI' : 'title',
    'LA' : 'language',
    'MH' : 'keywords',
    'AD' : 'affiliation',
    'AB' : 'abstract',
    'AD' : 'authoraddress',
    'TA' : 'journal',
    'CY' : 'country',
    'PG' : 'pages',
    'IP' : 'number',
    'VI' : 'volume',
    })
