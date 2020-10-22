# generated by appcreator
import django_filters
from django import forms

from dal import autocomplete

from vocabs.filters import generous_concept_filter
from vocabs.models import SkosConcept
from . models import (
    Manuscript
)


class ManuscriptListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Manuscript._meta.get_field('legacy_id').help_text,
        label=Manuscript._meta.get_field('legacy_id').verbose_name
    )
    ms_code = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Manuscript._meta.get_field('ms_code').help_text,
        label=Manuscript._meta.get_field('ms_code').verbose_name
    )
    ms_code_sort = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Manuscript._meta.get_field('ms_code_sort').help_text,
        label=Manuscript._meta.get_field('ms_code_sort').verbose_name
    )
    shelfmark = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Manuscript._meta.get_field('shelfmark').help_text,
        label=Manuscript._meta.get_field('shelfmark').verbose_name
    )
    heading = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Manuscript._meta.get_field('heading').help_text,
        label=Manuscript._meta.get_field('heading').verbose_name
    )
    material = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__name="material"
        ),
        help_text=Manuscript._meta.get_field('material').help_text,
        label=Manuscript._meta.get_field('material').verbose_name,
        method=generous_concept_filter,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/material",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
                },
        )
    )
    num_leaves = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Manuscript._meta.get_field('num_leaves').help_text,
        label=Manuscript._meta.get_field('num_leaves').verbose_name
    )
    dimensions = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Manuscript._meta.get_field('dimensions').help_text,
        label=Manuscript._meta.get_field('dimensions').verbose_name
    )

    class Meta:
        model = Manuscript
        fields = [
            'id',
            'legacy_id',
            'legacy_pk',
            'ms_code',
            'ms_code_sort',
            'shelfmark',
            'heading',
            'material',
            'num_leaves',
            'dimensions',
            ]


