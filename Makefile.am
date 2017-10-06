# This file is part of pybliographer
# 
# Copyright (C) 1998-2004 Frederic GOBRY
# Email : gobry@pybliographer.org
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

pybdir  = $(datadir)/$(PACKAGE)

SUBDIRS = 	. Pyblio 		\
		scripts		\
		tests		\
		Styles		\
		po		\
		help		\
		data

bin_SCRIPTS = pybliographer

pyb_DATA = pybrc.py

desktopdir = $(datadir)/applications
desktop_in_files = pybliographic.desktop.in
desktop_DATA = $(desktop_in_files:.desktop.in=.desktop)
%.desktop: %.desktop.in Makefile
	$(AM_V_GEN) $(MSGFMT) --desktop --template $< -d $(top_srcdir)/po -o $@

appdatadir = $(datadir)/appdata
appdata_in_files = pybliographic.appdata.xml.in
appdata_DATA = $(appdata_in_files:.xml.in=.xml)
%.xml: %.xml.in Makefile
	$(AM_V_GEN) $(MSGFMT) --xml --template $< -d $(top_srcdir)/po -o $@

EXTRA_DIST = \
 	pybliographer.in 		\
	$(appdata_in_files) \
	$(desktop_in_files) \
	$(pyb_DATA)

CLEANFILES = \
	pybliographer \
	$(desktop_DATA) \
	$(appdata_DATA)

DISTCLEANFILES =

pybliographer: pybliographer.in Makefile
	$(AM_V_GEN)sed \
		-e s!\@bin_dir\@!$(bindir)!               \
		-e s!\@libpyb\@!$(libdir)/$(PACKAGE)!     \
		-e s!\@datapyb\@!$(datadir)/$(PACKAGE)!   \
		-e s!\@package\@!$(PACKAGE)!              \
		-e s!\@version\@!$(VERSION)!              \
		-e s!\@locale_dir\@!$(localedir)!         \
		-e s!\@p_datadir\@!$(datadir)/$(PACKAGE)! \
		-e s!\@python_path\@!$(PYTHON)! \
		< $< > $@
	chmod +x $@

ACLOCAL_AMFLAGS = -I m4 ${ACLOCAL_FLAGS}
