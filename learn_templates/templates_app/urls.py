from templates_app import views
from django.urls import path, re_path, include

# TEMPLATE TAGGING: Django will automatically look for this variable
# 'app_name', which we set as the actual app_name.
# This allows us to use the template tagging...

app_name = 'templates_app'

urlpatterns = [
    # 'relative' link...
    re_path(r'^relative/$', views.relative, name='relative'),
    # 'other' link...
    re_path(r'other/$', views.other, name='other'),
]

# Here we are defnining the URL paths for the different html pages
# within our tamplates_app. We tell the URL which view to point to!

# See relative_url_templates.html for detail on relative URLs execution!
