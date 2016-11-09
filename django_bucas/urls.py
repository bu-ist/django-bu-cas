from django.conf.urls import include, url
from django_bucas.views import login, logout

class CASUrls(object):

	"""
	Enable the use of {% url "login" %} and {% url "logout" %}
	"""

	@property
	def urls(self):
		return include([
		    url(r'^login/$', login, name="login"),
		    url(r'^logout/$', logout, name="logout"),
		], namespace="cas")
 
urls = CASUrls().urls