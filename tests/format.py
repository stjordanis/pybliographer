import sys
from Pyblio import Fields, Autoload
from Pyblio.Open import bibopen
from Pyblio.Style import Utils


db   = bibopen (sys.argv [2])
keys = db.keys ()
keys.sort ()
url = Fields.URL (sys.argv [3])

Utils.generate (url, Autoload.get_by_name ('output', sys.argv [4]).data,
                db, keys, sys.stdout)

