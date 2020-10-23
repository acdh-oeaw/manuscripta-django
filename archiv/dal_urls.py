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
        r'^initium-autocomplete/$',
        dal_views.InitiumAC.as_view(),
        name='initium-autocomplete'
    ),
    url(
        r'^manuscript-autocomplete/$',
        dal_views.ManuscriptAC.as_view(),
        name='manuscript-autocomplete'
    ),
    url(
        r'^msdesc-autocomplete/$',
        dal_views.MsDescAC.as_view(),
        name='msdesc-autocomplete'
    ),
    url(
        r'^mspart-autocomplete/$',
        dal_views.MsPartAC.as_view(),
        name='mspart-autocomplete'
    ),
    url(
        r'^place-autocomplete/$',
        dal_views.PlaceAC.as_view(),
        name='place-autocomplete'
    ),
    url(
        r'^verfasser-autocomplete/$',
        dal_views.VerfasserAC.as_view(),
        name='verfasser-autocomplete'
    ),
]
