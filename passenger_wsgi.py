import os
import sys
import BaseWeb.wsgi
sys.path.insert(0, os.path.dirname(__file__))
application = BaseWeb.wsgi.application
