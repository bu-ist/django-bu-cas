from django.conf.urls import url
from django_bucas.views import login, logout

class CASApp(object):

	@property
	def urls(self):
		return [
		    url(r'^login/$', login, name="login"),
		    url(r'^logout/$', logout, name="logout"),
		], 'cas', ""

sites = CASApp()