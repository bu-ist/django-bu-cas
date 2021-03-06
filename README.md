===========
BU Django CAS
===========

The BU Django CAS middleware provides CAS integration for Django projects, allowing application to authetnicate against a CAS server.

**Note: If you are using Django>1.5, Please refer to the v2 branch of this repo.**

===========
Instructions
===========

1. Add CAS configuration lines to settings.py:


```
MIDDLEWARE_CLASSES = (
	...
    'django.contrib.auth.middleware.AuthenticationMiddleware', # should already be there
    'django_bucas.middleware.CASMiddleware',
    ...
)
```

```
AUTHENTICATION_BACKENDS = (
	...
    'django.contrib.auth.backends.ModelBackend',
    'django_bucas.backends.CASBackend',
    ...
)
```

```
INSTALLED_APPS = (
	...
	'django_bucas',
	...
)
```

You will also need to configure the following CAS specific settings depending on the environment:

```
CAS_SERVER_URL = "https://weblogin-devl.bu.edu/cas/"	# Adjust to use correct location per-environment
CAS_LOGOUT_COMPLETELY = True
CAS_REDIRECT_URL = "/admin"
```

2. Modify urls.py to include URL's for CAS login/logout, i.e.

```
urlpatterns = patterns('',
	...
	url(r'^accounts/login/$', 'django_bucas.views.login'),
	url(r'^accounts/logout/$', 'django_bucas.views.logout'),
	...
)
```
