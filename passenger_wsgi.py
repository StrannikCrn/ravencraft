import os, sys
sys.path.insert(0,'home2/c/c1mg/RavencraftRepo/Lib/site-packages/')
sys.path.insert(0,'home2/c/c1mg/RavencraftRepo/Lib/site-packages/django')
sys.path.insert(0,'home2/c/c1mg/RavencraftRepo/Lib/')
sys.path.append('home2/c/c1mg/RavencraftRepo')

os.environ['DJANGO_SETTINGS_MODULE'] = 'Ravencraft.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()