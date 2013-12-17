# BU Django CAS #


The BU Django CAS middleware provides CAS integration for Django projects, allowing application to authetnicate against a CAS server.

**Note:To use this middleware, you must be running django >= 1.5.**

# Instructions #


Add CAS configuration lines to settings.py:


	MIDDLEWARE_CLASSES = (
		...
		'django.contrib.auth.middleware.AuthenticationMiddleware',
		'django_bucas.middleware.CASMiddleware',
		...
	)

	AUTHENTICATION_BACKENDS = (
		...
		'django.contrib.auth.backends.ModelBackend',
		'django_bucas.backends.CASBackend',
		...
	)


You will also need to configure the following CAS specific settings depending on the environment:


	CAS_SERVER_URL = "https://weblogin-devl.bu.edu/cas/"	# Adjust to use correct location per-environment
	CAS_LOGOUT_COMPLETELY = True
	CAS_REDIRECT_URL = "/admin"


Finally, modify urls.py to include URL's for CAS login/logout, i.e.


	urlpatterns = patterns('',
		...
		url(r'^accounts/login/$', 'django_bucas.views.login'),
		url(r'^accounts/logout/$', 'django_bucas.views.logout'),
		...
	)
