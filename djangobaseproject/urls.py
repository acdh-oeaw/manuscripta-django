from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from vocabs import api_views


router = routers.DefaultRouter()
router.register(r"metadata", api_views.MetadataViewSet)
router.register(r"skoslabels", api_views.SkosLabelViewSet)
router.register(r"skosnamespaces", api_views.SkosNamespaceViewSet)
router.register(r"skosconceptschemes", api_views.SkosConceptSchemeViewSet)
router.register(r"skoscollections", api_views.SkosCollectionViewSet)
router.register(r"skosconcepts", api_views.SkosConceptViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
    path("browsing/", include("browsing.urls", namespace="browsing")),
    path("archiv/", include("archiv.urls", namespace="archiv")),
    path("archiv-ac/", include("archiv.dal_urls", namespace="archiv-ac")),
    path("vocabs/", include("vocabs.urls", namespace="vocabs")),
    path("vocabs-ac/", include("vocabs.dal_urls", namespace="vocabs-ac")),
    path("", include("webpage.urls", namespace="webpage")),
]
