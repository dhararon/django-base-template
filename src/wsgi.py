# Standard Library
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")
os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")

# Third Party Stuff
from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
