# generated by appcreator
from django.db.models import Q
from dal import autocomplete
from . models import *


class BibliothekAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Bibliothek.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(lib_code__icontains=self.q)
            )
        return qs


class InitiumAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Initium.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(legacy_pk__icontains=self.q)
            )
        return qs


class ManuscriptAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Manuscript.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(ms_code__icontains=self.q)
            )
        return qs


class MsDescAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = MsDesc.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(legacy_pk__icontains=self.q)
            )
        return qs


class MsPartAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = MsPart.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(legacy_pk__icontains=self.q)
            )
        return qs


class PlaceAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Place.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(name__icontains=self.q)
            )
        return qs


class VerfasserAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Verfasser.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(name__icontains=self.q)
            )
        return qs


