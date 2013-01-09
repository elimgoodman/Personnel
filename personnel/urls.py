from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'people.views.people'),
    url(r'^people/$', 'people.views.manage_people'),
    url(r'^people/edit/$', 'people.views.edit_person'),
    url(r'^people/(\w+)/$', 'people.views.view_person'),
    url(r'^people/(\w+)/update_info$', 'people.views.update_info'),
    url(r'^people/(\w+)/journal$', 'people.views.journal'),
    url(r'^people/(\w+)/journal/add$', 'people.views.add_entry'),
    # url(r'^personnel/', include('personnel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
