from django.conf.urls.defaults import *
from django.contrib import databrowse
from django.conf import settings
from openeats.accounts.forms import ProfileForm
import helpers.signals

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^openeats/', include('openeats.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    ('^profiles/edit', 'profiles.views.edit_profile', {'form_class': ProfileForm,}),
    (r'^profiles/', include('profiles.urls')),
    (r'^rosetta/', include('rosetta.urls')),
    (r'^groups/', include('recipe_groups.urls')),
    (r'^recipe/', include('recipe.urls')),
    (r'^ingredient/', include('ingredient.urls')),
    (r'^search/', include('haystack.urls')),

)



if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
        )