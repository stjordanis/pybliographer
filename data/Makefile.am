SUBDIRS = 	icons	\
		pixmaps	\
		src

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
	$(appdata_in_files) \
	$(desktop_in_files)

CLEANFILES = \
	$(desktop_DATA) \
	$(appdata_DATA)
