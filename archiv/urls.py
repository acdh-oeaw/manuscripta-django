# generated by appcreator
from django.urls import path
from . import views

app_name = "archiv"
urlpatterns = [
    path("autor/", views.AutorListView.as_view(), name="autor_browse"),
    path(
        "autor/detail/<int:pk>",
        views.AutorDetailView.as_view(),
        name="autor_detail",
    ),
    path("autor/create/", views.AutorCreate.as_view(), name="autor_create"),
    path("autor/edit/<int:pk>", views.AutorUpdate.as_view(), name="autor_edit"),
    path(
        "autor/delete/<int:pk>",
        views.AutorDelete.as_view(),
        name="autor_delete",
    ),
    path("bibliothek/", views.BibliothekListView.as_view(), name="bibliothek_browse"),
    path(
        "bibliothek/detail/<int:pk>",
        views.BibliothekDetailView.as_view(),
        name="bibliothek_detail",
    ),
    path(
        "bibliothek/create/",
        views.BibliothekCreate.as_view(),
        name="bibliothek_create",
    ),
    path(
        "bibliothek/edit/<int:pk>",
        views.BibliothekUpdate.as_view(),
        name="bibliothek_edit",
    ),
    path(
        "bibliothek/delete/<int:pk>",
        views.BibliothekDelete.as_view(),
        name="bibliothek_delete",
    ),
    path("initium/", views.InitiumListView.as_view(), name="initium_browse"),
    path(
        "initium/detail/<int:pk>",
        views.InitiumDetailView.as_view(),
        name="initium_detail",
    ),
    path("initium/create/", views.InitiumCreate.as_view(), name="initium_create"),
    path(
        "initium/edit/<int:pk>",
        views.InitiumUpdate.as_view(),
        name="initium_edit",
    ),
    path(
        "initium/delete/<int:pk>",
        views.InitiumDelete.as_view(),
        name="initium_delete",
    ),
    path("literatur/", views.LiteraturListView.as_view(), name="literatur_browse"),
    path(
        "literatur/detail/<int:pk>",
        views.LiteraturDetailView.as_view(),
        name="literatur_detail",
    ),
    path("literatur/create/", views.LiteraturCreate.as_view(), name="literatur_create"),
    path(
        "literatur/edit/<int:pk>",
        views.LiteraturUpdate.as_view(),
        name="literatur_edit",
    ),
    path(
        "literatur/delete/<int:pk>",
        views.LiteraturDelete.as_view(),
        name="literatur_delete",
    ),
    path("manuscript/", views.ManuscriptListView.as_view(), name="manuscript_browse"),
    path(
        "manuscript/detail/<int:pk>",
        views.ManuscriptDetailView.as_view(),
        name="manuscript_detail",
    ),
    path(
        "manuscript/create/",
        views.ManuscriptCreate.as_view(),
        name="manuscript_create",
    ),
    path(
        "manuscript/edit/<int:pk>",
        views.ManuscriptUpdate.as_view(),
        name="manuscript_edit",
    ),
    path(
        "manuscript/delete/<int:pk>",
        views.ManuscriptDelete.as_view(),
        name="manuscript_delete",
    ),
    path("msdesc/", views.MsDescListView.as_view(), name="msdesc_browse"),
    path(
        "msdesc/detail/<int:pk>",
        views.MsDescDetailView.as_view(),
        name="msdesc_detail",
    ),
    path("msdesc/create/", views.MsDescCreate.as_view(), name="msdesc_create"),
    path(
        "msdesc/edit/<int:pk>",
        views.MsDescUpdate.as_view(),
        name="msdesc_edit",
    ),
    path(
        "msdesc/delete/<int:pk>",
        views.MsDescDelete.as_view(),
        name="msdesc_delete",
    ),
    path("mspart/", views.MsPartListView.as_view(), name="mspart_browse"),
    path(
        "mspart/detail/<int:pk>",
        views.MsPartDetailView.as_view(),
        name="mspart_detail",
    ),
    path("mspart/create/", views.MsPartCreate.as_view(), name="mspart_create"),
    path(
        "mspart/edit/<int:pk>",
        views.MsPartUpdate.as_view(),
        name="mspart_edit",
    ),
    path(
        "mspart/delete/<int:pk>",
        views.MsPartDelete.as_view(),
        name="mspart_delete",
    ),
    path("place/", views.PlaceListView.as_view(), name="place_browse"),
    path(
        "place/detail/<int:pk>",
        views.PlaceDetailView.as_view(),
        name="place_detail",
    ),
    path("place/create/", views.PlaceCreate.as_view(), name="place_create"),
    path("place/edit/<int:pk>", views.PlaceUpdate.as_view(), name="place_edit"),
    path(
        "place/delete/<int:pk>",
        views.PlaceDelete.as_view(),
        name="place_delete",
    ),
    path("verfasser/", views.VerfasserListView.as_view(), name="verfasser_browse"),
    path(
        "verfasser/detail/<int:pk>",
        views.VerfasserDetailView.as_view(),
        name="verfasser_detail",
    ),
    path("verfasser/create/", views.VerfasserCreate.as_view(), name="verfasser_create"),
    path(
        "verfasser/edit/<int:pk>",
        views.VerfasserUpdate.as_view(),
        name="verfasser_edit",
    ),
    path(
        "verfasser/delete/<int:pk>",
        views.VerfasserDelete.as_view(),
        name="verfasser_delete",
    ),
    path("weblit/", views.WebLitListView.as_view(), name="weblit_browse"),
    path(
        "weblit/detail/<int:pk>",
        views.WebLitDetailView.as_view(),
        name="weblit_detail",
    ),
    path("weblit/create/", views.WebLitCreate.as_view(), name="weblit_create"),
    path(
        "weblit/edit/<int:pk>",
        views.WebLitUpdate.as_view(),
        name="weblit_edit",
    ),
    path(
        "weblit/delete/<int:pk>",
        views.WebLitDelete.as_view(),
        name="weblit_delete",
    ),
    path(
        "werkinstanz/",
        views.WerkInstanzListView.as_view(),
        name="werkinstanz_browse",
    ),
    path(
        "werkinstanz/detail/<int:pk>",
        views.WerkInstanzDetailView.as_view(),
        name="werkinstanz_detail",
    ),
    path(
        "werkinstanz/create/",
        views.WerkInstanzCreate.as_view(),
        name="werkinstanz_create",
    ),
    path(
        "werkinstanz/edit/<int:pk>",
        views.WerkInstanzUpdate.as_view(),
        name="werkinstanz_edit",
    ),
    path(
        "werkinstanz/delete/<int:pk>",
        views.WerkInstanzDelete.as_view(),
        name="werkinstanz_delete",
    ),
    path("zitat/", views.ZitatListView.as_view(), name="zitat_browse"),
    path(
        "zitat/detail/<int:pk>",
        views.ZitatDetailView.as_view(),
        name="zitat_detail",
    ),
    path("zitat/create/", views.ZitatCreate.as_view(), name="zitat_create"),
    path("zitat/edit/<int:pk>", views.ZitatUpdate.as_view(), name="zitat_edit"),
    path(
        "zitat/delete/<int:pk>",
        views.ZitatDelete.as_view(),
        name="zitat_delete",
    ),
    path("einband/", views.EinbandListView.as_view(), name="einband_browse"),
    path(
        "einband/detail/<int:pk>",
        views.EinbandDetailView.as_view(),
        name="einband_detail",
    ),
    path("einband/create/", views.EinbandCreate.as_view(), name="einband_create"),
    path("einband/edit/<int:pk>", views.EinbandUpdate.as_view(), name="einband_edit"),
    path(
        "einband/delete/<int:pk>",
        views.EinbandDelete.as_view(),
        name="einband_delete",
    ),
    path("schrift/", views.SchriftListView.as_view(), name="schrift_browse"),
    path(
        "schrift/detail/<int:pk>",
        views.SchriftDetailView.as_view(),
        name="schrift_detail",
    ),
    path("schrift/create/", views.SchriftCreate.as_view(), name="schrift_create"),
    path("schrift/edit/<int:pk>", views.SchriftUpdate.as_view(), name="schrift_edit"),
    path(
        "schrift/delete/<int:pk>",
        views.SchriftDelete.as_view(),
        name="schrift_delete",
    ),
]
