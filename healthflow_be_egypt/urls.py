"""URL namespace for the optional Egypt localization module.

The module currently exposes no standalone HTTP endpoints. Providing an empty
URL configuration keeps it compatible with openIMIS module discovery, which
registers each configured module under its own URL prefix.
"""

from django.urls import path


urlpatterns = []
