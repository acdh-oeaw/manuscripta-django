# generated by appcreator
import django_filters
from django import forms

from dal import autocomplete

from vocabs.filters import generous_concept_filter
from vocabs.models import SkosConcept
from .models import (
    Autor,
    Bibliothek,
    Initium,
    Literatur,
    Manuscript,
    MsDesc,
    MsPart,
    Place,
    Verfasser,
    WebLit,
    WerkInstanz,
    Zitat,
)


class AutorListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Autor._meta.get_field("legacy_id").help_text,
        label=Autor._meta.get_field("legacy_id").verbose_name,
    )
    name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Autor._meta.get_field("name").help_text,
        label=Autor._meta.get_field("name").verbose_name,
    )
    name_gnd = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Autor._meta.get_field("name_gnd").help_text,
        label=Autor._meta.get_field("name_gnd").verbose_name,
    )
    gnd_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Autor._meta.get_field("gnd_id").help_text,
        label=Autor._meta.get_field("gnd_id").verbose_name,
    )
    biogr_daten = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Autor._meta.get_field("biogr_daten").help_text,
        label=Autor._meta.get_field("biogr_daten").verbose_name,
    )

    class Meta:
        model = Autor
        fields = [
            "id",
            "legacy_id",
            "name",
            "name_gnd",
            "gnd_id",
            "biogr_daten",
        ]


class BibliothekListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Bibliothek._meta.get_field("legacy_id").help_text,
        label=Bibliothek._meta.get_field("legacy_id").verbose_name,
    )
    lib_code = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Bibliothek._meta.get_field("lib_code").help_text,
        label=Bibliothek._meta.get_field("lib_code").verbose_name,
    )
    lib_name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Bibliothek._meta.get_field("lib_name").help_text,
        label=Bibliothek._meta.get_field("lib_name").verbose_name,
    )
    lib_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(collection__name="lib_type"),
        help_text=Bibliothek._meta.get_field("lib_type").help_text,
        label=Bibliothek._meta.get_field("lib_type").verbose_name,
        method=generous_concept_filter,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/lib_type",
            attrs={
                "data-placeholder": "Autocomplete ...",
                "data-minimum-input-length": 2,
            },
        ),
    )
    short_name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Bibliothek._meta.get_field("short_name").help_text,
        label=Bibliothek._meta.get_field("short_name").verbose_name,
    )
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Bibliothek._meta.get_field("location").help_text,
        label=Bibliothek._meta.get_field("location").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:place-autocomplete",
        ),
    )
    address = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Bibliothek._meta.get_field("address").help_text,
        label=Bibliothek._meta.get_field("address").verbose_name,
    )

    class Meta:
        model = Bibliothek
        fields = [
            "id",
            "legacy_id",
            "lib_code",
            "lib_name",
            "lib_type",
            "short_name",
            "location",
            "address",
        ]


class InitiumListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Initium._meta.get_field("legacy_id").help_text,
        label=Initium._meta.get_field("legacy_id").verbose_name,
    )
    manuscript = django_filters.ModelMultipleChoiceFilter(
        queryset=Manuscript.objects.all(),
        help_text=Initium._meta.get_field("manuscript").help_text,
        label=Initium._meta.get_field("manuscript").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:manuscript-autocomplete",
        ),
    )
    initium = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Initium._meta.get_field("initium").help_text,
        label=Initium._meta.get_field("initium").verbose_name,
    )
    explicit = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Initium._meta.get_field("explicit").help_text,
        label=Initium._meta.get_field("explicit").verbose_name,
    )
    fol = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Initium._meta.get_field("fol").help_text,
        label=Initium._meta.get_field("fol").verbose_name,
    )
    fol_sort = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Initium._meta.get_field("fol_sort").help_text,
        label=Initium._meta.get_field("fol_sort").verbose_name,
    )
    fol_end = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Initium._meta.get_field("fol_end").help_text,
        label=Initium._meta.get_field("fol_end").verbose_name,
    )
    signtaur_fol = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Initium._meta.get_field("signtaur_fol").help_text,
        label=Initium._meta.get_field("signtaur_fol").verbose_name,
    )
    titel_vorspann = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Initium._meta.get_field("titel_vorspann").help_text,
        label=Initium._meta.get_field("titel_vorspann").verbose_name,
    )
    titel = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Initium._meta.get_field("titel").help_text,
        label=Initium._meta.get_field("titel").verbose_name,
    )
    sprache = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(collection__name="sprache"),
        help_text=Initium._meta.get_field("sprache").help_text,
        label=Initium._meta.get_field("sprache").verbose_name,
        method=generous_concept_filter,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/sprache",
            attrs={
                "data-placeholder": "Autocomplete ...",
                "data-minimum-input-length": 2,
            },
        ),
    )
    werk = django_filters.ModelMultipleChoiceFilter(
        queryset=WerkInstanz.objects.all(),
        help_text=Initium._meta.get_field("werk").help_text,
        label=Initium._meta.get_field("werk").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:werkinstanz-autocomplete",
        ),
    )

    class Meta:
        model = Initium
        fields = [
            "id",
            "legacy_id",
            "legacy_pk",
            "manuscript",
            "initium",
            "explicit",
            "fol",
            "fol_sort",
            "fol_end",
            "signtaur_fol",
            "titel_vorspann",
            "titel",
            "sprache",
            "werk",
        ]


class LiteraturListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Literatur._meta.get_field("legacy_id").help_text,
        label=Literatur._meta.get_field("legacy_id").verbose_name,
    )
    kurz_zitat = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Literatur._meta.get_field("kurz_zitat").help_text,
        label=Literatur._meta.get_field("kurz_zitat").verbose_name,
    )
    autor_nachname = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Literatur._meta.get_field("autor_nachname").help_text,
        label=Literatur._meta.get_field("autor_nachname").verbose_name,
    )
    nr = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Literatur._meta.get_field("nr").help_text,
        label=Literatur._meta.get_field("nr").verbose_name,
    )
    kz = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Literatur._meta.get_field("kz").help_text,
        label=Literatur._meta.get_field("kz").verbose_name,
    )
    vollzitat = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Literatur._meta.get_field("vollzitat").help_text,
        label=Literatur._meta.get_field("vollzitat").verbose_name,
    )
    anmerkung = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Literatur._meta.get_field("anmerkung").help_text,
        label=Literatur._meta.get_field("anmerkung").verbose_name,
    )

    class Meta:
        model = Literatur
        fields = [
            "id",
            "legacy_id",
            "legacy_pk",
            "kurz_zitat",
            "autor_nachname",
            "jahr",
            "nr",
            "kz",
            "vollzitat",
            "anmerkung",
        ]


class ManuscriptListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Manuscript._meta.get_field("legacy_id").help_text,
        label=Manuscript._meta.get_field("legacy_id").verbose_name,
    )
    lib_code = django_filters.ModelMultipleChoiceFilter(
        queryset=Bibliothek.objects.all(),
        help_text=Manuscript._meta.get_field("lib_code").help_text,
        label=Manuscript._meta.get_field("lib_code").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:bibliothek-autocomplete",
        ),
    )
    ms_code = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Manuscript._meta.get_field("ms_code").help_text,
        label=Manuscript._meta.get_field("ms_code").verbose_name,
    )
    ms_code_sort = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Manuscript._meta.get_field("ms_code_sort").help_text,
        label=Manuscript._meta.get_field("ms_code_sort").verbose_name,
    )
    shelfmark = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Manuscript._meta.get_field("shelfmark").help_text,
        label=Manuscript._meta.get_field("shelfmark").verbose_name,
    )
    heading = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Manuscript._meta.get_field("heading").help_text,
        label=Manuscript._meta.get_field("heading").verbose_name,
    )
    material = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(collection__name="material"),
        help_text=Manuscript._meta.get_field("material").help_text,
        label=Manuscript._meta.get_field("material").verbose_name,
        method=generous_concept_filter,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/material",
            attrs={
                "data-placeholder": "Autocomplete ...",
                "data-minimum-input-length": 2,
            },
        ),
    )
    num_leaves = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Manuscript._meta.get_field("num_leaves").help_text,
        label=Manuscript._meta.get_field("num_leaves").verbose_name,
    )
    dimensions = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Manuscript._meta.get_field("dimensions").help_text,
        label=Manuscript._meta.get_field("dimensions").verbose_name,
    )
    origin_date = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Manuscript._meta.get_field("origin_date").help_text,
        label=Manuscript._meta.get_field("origin_date").verbose_name,
    )
    prov = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Manuscript._meta.get_field("prov").help_text,
        label=Manuscript._meta.get_field("prov").verbose_name,
    )
    fragm = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Manuscript._meta.get_field("fragm").help_text,
        label=Manuscript._meta.get_field("fragm").verbose_name,
    )
    remarks = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Manuscript._meta.get_field("remarks").help_text,
        label=Manuscript._meta.get_field("remarks").verbose_name,
    )
    geschichte = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Manuscript._meta.get_field("geschichte").help_text,
        label=Manuscript._meta.get_field("geschichte").verbose_name,
    )

    class Meta:
        model = Manuscript
        fields = [
            "id",
            "legacy_id",
            "legacy_pk",
            "lib_code",
            "ms_code",
            "ms_code_sort",
            "shelfmark",
            "heading",
            "material",
            "num_leaves",
            "dimensions",
            "origin_date",
            "prov",
            "fragm",
            "hscensus",
            "remarks",
            "geschichte",
        ]


class MsDescListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=MsDesc._meta.get_field("legacy_id").help_text,
        label=MsDesc._meta.get_field("legacy_id").verbose_name,
    )
    manuscript = django_filters.ModelMultipleChoiceFilter(
        queryset=Manuscript.objects.all(),
        help_text=MsDesc._meta.get_field("manuscript").help_text,
        label=MsDesc._meta.get_field("manuscript").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:manuscript-autocomplete",
        ),
    )
    bibliography = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=MsDesc._meta.get_field("bibliography").help_text,
        label=MsDesc._meta.get_field("bibliography").verbose_name,
    )
    phys_desc = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=MsDesc._meta.get_field("phys_desc").help_text,
        label=MsDesc._meta.get_field("phys_desc").verbose_name,
    )
    content = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=MsDesc._meta.get_field("content").help_text,
        label=MsDesc._meta.get_field("content").verbose_name,
    )
    verfasser = django_filters.ModelMultipleChoiceFilter(
        queryset=Verfasser.objects.all(),
        help_text=MsDesc._meta.get_field("verfasser").help_text,
        label=MsDesc._meta.get_field("verfasser").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:verfasser-autocomplete",
        ),
    )

    class Meta:
        model = MsDesc
        fields = [
            "id",
            "legacy_id",
            "legacy_pk",
            "manuscript",
            "bibliography",
            "phys_desc",
            "content",
            "verfasser",
            "created",
        ]


class MsPartListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=MsPart._meta.get_field("legacy_id").help_text,
        label=MsPart._meta.get_field("legacy_id").verbose_name,
    )
    part_of_manuscript = django_filters.ModelMultipleChoiceFilter(
        queryset=Manuscript.objects.all(),
        help_text=MsPart._meta.get_field("part_of_manuscript").help_text,
        label=MsPart._meta.get_field("part_of_manuscript").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:manuscript-autocomplete",
        ),
    )
    range = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=MsPart._meta.get_field("range").help_text,
        label=MsPart._meta.get_field("range").verbose_name,
    )
    date_str = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=MsPart._meta.get_field("date_str").help_text,
        label=MsPart._meta.get_field("date_str").verbose_name,
    )
    origin_date = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=MsPart._meta.get_field("origin_date").help_text,
        label=MsPart._meta.get_field("origin_date").verbose_name,
    )

    class Meta:
        model = MsPart
        fields = [
            "id",
            "legacy_id",
            "legacy_pk",
            "part_of_manuscript",
            "range",
            "date_str",
            "origin_date",
            "date_begin",
            "date_end",
        ]


class PlaceListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Place._meta.get_field("legacy_id").help_text,
        label=Place._meta.get_field("legacy_id").verbose_name,
    )
    name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Place._meta.get_field("name").help_text,
        label=Place._meta.get_field("name").verbose_name,
    )

    class Meta:
        model = Place
        fields = [
            "id",
            "legacy_id",
            "name",
        ]


class VerfasserListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Verfasser._meta.get_field("legacy_id").help_text,
        label=Verfasser._meta.get_field("legacy_id").verbose_name,
    )
    name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Verfasser._meta.get_field("name").help_text,
        label=Verfasser._meta.get_field("name").verbose_name,
    )

    class Meta:
        model = Verfasser
        fields = [
            "id",
            "legacy_id",
            "name",
        ]


class WebLitListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=WebLit._meta.get_field("legacy_id").help_text,
        label=WebLit._meta.get_field("legacy_id").verbose_name,
    )
    url = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=WebLit._meta.get_field("url").help_text,
        label=WebLit._meta.get_field("url").verbose_name,
    )
    beschriftung = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=WebLit._meta.get_field("beschriftung").help_text,
        label=WebLit._meta.get_field("beschriftung").verbose_name,
    )
    literatur = django_filters.ModelMultipleChoiceFilter(
        queryset=Literatur.objects.all(),
        help_text=WebLit._meta.get_field("literatur").help_text,
        label=WebLit._meta.get_field("literatur").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:literatur-autocomplete",
        ),
    )

    class Meta:
        model = WebLit
        fields = [
            "id",
            "legacy_id",
            "legacy_pk",
            "url",
            "beschriftung",
            "literatur",
        ]


class WerkInstanzListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=WerkInstanz._meta.get_field("legacy_id").help_text,
        label=WerkInstanz._meta.get_field("legacy_id").verbose_name,
    )
    werk_titel = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=WerkInstanz._meta.get_field("werk_titel").help_text,
        label=WerkInstanz._meta.get_field("werk_titel").verbose_name,
    )
    werk_titel_alt = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=WerkInstanz._meta.get_field("werk_titel_alt").help_text,
        label=WerkInstanz._meta.get_field("werk_titel_alt").verbose_name,
    )
    textzeuge_kommentar = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=WerkInstanz._meta.get_field("textzeuge_kommentar").help_text,
        label=WerkInstanz._meta.get_field("textzeuge_kommentar").verbose_name,
    )
    sprache = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(collection__name="sprache"),
        help_text=WerkInstanz._meta.get_field("sprache").help_text,
        label=WerkInstanz._meta.get_field("sprache").verbose_name,
        method=generous_concept_filter,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/sprache",
            attrs={
                "data-placeholder": "Autocomplete ...",
                "data-minimum-input-length": 2,
            },
        ),
    )
    fol_start = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=WerkInstanz._meta.get_field("fol_start").help_text,
        label=WerkInstanz._meta.get_field("fol_start").verbose_name,
    )
    fol_end = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=WerkInstanz._meta.get_field("fol_end").help_text,
        label=WerkInstanz._meta.get_field("fol_end").verbose_name,
    )
    fol_sort = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=WerkInstanz._meta.get_field("fol_sort").help_text,
        label=WerkInstanz._meta.get_field("fol_sort").verbose_name,
    )
    manuscript = django_filters.ModelMultipleChoiceFilter(
        queryset=Manuscript.objects.all(),
        help_text=WerkInstanz._meta.get_field("manuscript").help_text,
        label=WerkInstanz._meta.get_field("manuscript").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:manuscript-autocomplete",
        ),
    )
    autor = django_filters.ModelMultipleChoiceFilter(
        queryset=Autor.objects.all(),
        help_text=WerkInstanz._meta.get_field("autor").help_text,
        label=WerkInstanz._meta.get_field("autor").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:autor-autocomplete",
        ),
    )

    class Meta:
        model = WerkInstanz
        fields = [
            "id",
            "legacy_id",
            "legacy_pk",
            "werk_titel",
            "werk_titel_alt",
            "textzeuge_kommentar",
            "sprache",
            "fol_start",
            "fol_end",
            "fol_sort",
            "manuscript",
            "autor",
        ]


class ZitatListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Zitat._meta.get_field("legacy_id").help_text,
        label=Zitat._meta.get_field("legacy_id").verbose_name,
    )
    literatur = django_filters.ModelMultipleChoiceFilter(
        queryset=Literatur.objects.all(),
        help_text=Zitat._meta.get_field("literatur").help_text,
        label=Zitat._meta.get_field("literatur").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:literatur-autocomplete",
        ),
    )
    manuscript = django_filters.ModelMultipleChoiceFilter(
        queryset=Manuscript.objects.all(),
        help_text=Zitat._meta.get_field("manuscript").help_text,
        label=Zitat._meta.get_field("manuscript").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:manuscript-autocomplete",
        ),
    )
    kz_ms = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Zitat._meta.get_field("kz_ms").help_text,
        label=Zitat._meta.get_field("kz_ms").verbose_name,
    )
    signatur = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Zitat._meta.get_field("signatur").help_text,
        label=Zitat._meta.get_field("signatur").verbose_name,
    )

    class Meta:
        model = Zitat
        fields = [
            "id",
            "legacy_id",
            "legacy_pk",
            "literatur",
            "manuscript",
            "kz_ms",
            "signatur",
        ]
