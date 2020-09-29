# ![pybliographer-logo] Pybliographer

Pybliographer provides a framework for working with bibliographic
databases.

This software is licensed under the [GPLv2][license].

For more information, please consult the documentation at the [website][pybliographer-website].


## Requirements

Before installing pybliographer, please install:

* GNU Recode (v. 3.5)
* python-bibtex (also available at the [website][pybliographer-website])
* Gnome 2.x and gnome-python 2.x


## Installation 

Basically, it should be a matter of:

```
	./configure && make
	su
	make install
```

You can then run several programs :

* pybliographic : the graphical interface
* pybliographer : the text-based interface and scripting language
* pybcheck, pybconvert, pybformat, ... : several useful tools

For more configuration options, have a look at the output of `./configure --help`.


# Troubleshooting

If the configure script reports the following errors:

* *"error in python modules dependencies:  No module named ..."*
 
   This means that a required module is not installed. Unfortunately,
   depending on your distribution, the actual package to install can
   be named differently. Check on the help pages of your distribution.

* *"broken recode version"*

   Your recode package does not behave properly.  Consult
   [recode help][recode-help] for more information.


[license]: COPYING
[pybliographer-website]: https://pybliographer.org/
[recode-help]: http://pybliographer.org/RecodeHelp
[pybliographer-logo]: data/icons/48x48/pybliographic.png
