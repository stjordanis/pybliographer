gladedir = $(datadir)/$(PACKAGE)/Pyblio/GnomeUI/glade
appicondir = $(datadir)/$(PACKAGE)/pixmaps

glade_DATA = 					\
	fields.ui				\
	pyblio.ui 				\
	search.ui 				\
	sort.ui 				\
	format.ui				\
	medline.glade 				\
	config.ui				\
	openurl.ui

EXTRA_DIST = $(glade_DATA) pyblio.ui.in

pyblio.ui: pyblio.ui.in Makefile
	sed -e 's^\@icondir\@^$(appicondir)^g' 		\
	< $(srcdir)/pyblio.ui.in > pyblio.ui.tmp 	\
	&& mv pyblio.ui.tmp pyblio.ui

DISTCLEANFILES = pyblio.ui
