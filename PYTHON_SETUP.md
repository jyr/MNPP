Setuptools
---

/Applications/MNPP/Library/python26/bin/python setup.py install --prefix=/Applications/MNPP/Library/python26/

Uwsgi
---

/Applications/MNPP/Library/python26/bin/python setup.py install --prefix=/Applications/MNPP/Library/uwsgi/

MySQLdb
---

Edit line 26 in setup_posix.py with mysql_config.path = "/Applications/MNPP/Library/mysql/bin/mysql_config"

/Applications/MNPP/Library/python26/bin/python setup.py build
/Applications/MNPP/Library/python26/bin/python setup.py install --prefix=/Applications/MNPP/Library/python26/

Web.py
---

/Applications/MNPP/Library/python26/bin/python setup.py install --prefix=/Applications/MNPP/Library/python26