# generated by appcreator
from django.conf.urls import url
from . import dal_views

app_name = 'archiv'
urlpatterns = [
    url(
        r'^bibliothek-autocomplete/$',
        dal_views.BibliothekAC.as_view(),
        name='bibliothek-autocomplete'
    ),
    url(
        r'^manuscript-autocomplete/$',
        dal_views.ManuscriptAC.as_view(),
        name='manuscript-autocomplete'
    ),
]
