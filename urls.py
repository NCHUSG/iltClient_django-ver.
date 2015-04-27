from django.conf.urls import patterns, url
from ilt_client import views
urlpatterns = patterns(
	'',
    url(r'^run/', views.run, name='run'),
    url(r'^failed/', views.getData_failed, name='failed'), 
    
    # If you wan't to watch what data in the session,
    #   just uncomment this url
    url(r'^show/', views.show, name='show'),
)










