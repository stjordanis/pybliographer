# This file is part of pybliographer
# 
# Copyright (C) 1998,1999,2000 Frederic GOBRY
# Email : gobry@idiap.ch
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
# $Id$

''' This module defines some common exceptions '''

import string

def format (prefix, lines):
    return prefix + string.join (lines, '\n' + prefix)
    
class ParserError:

    def __init__ (self, errors, file = None):
        if file:
            self.file = file + ':'
        else:
            self.file = ''
            
        self.errors = errors or []
        return

    def __repr__ (self):
        return format (self.file, self.errors)

class FormatError:

    def __init__ (self, message):
        self.message = message
        return

    def __repr__ (self):
        return self.message
    