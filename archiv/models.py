# generated by appcreator

from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import DateRangeField

from vocabs.models import SkosConcept

from browsing.browsing_utils import model_to_dict


def set_extra(self, **kwargs):
    self.extra = kwargs
    return self


models.Field.set_extra = set_extra


class Manuscript(models.Model):
    ### Beschreibt ein Manuscript ###
    legacy_id = models.CharField(
        max_length=300, blank=True,
        verbose_name="Legacy ID"
        )
    legacy_pk = models.IntegerField(
        blank=True, null=True,
        verbose_name="Primärschlüssel Alt",
        help_text="Primärschlüssel Alt",
    ).set_extra(
        is_public=False,
        data_lookup="ID",
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="Primärschlüssel Alt: <value>",
    )
    ms_code = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="MS-Code",
        help_text="MS-Code",
    ).set_extra(
        is_public=True,
        data_lookup="ms_code",
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="MS-CODE: <value>",
    )
    ms_code_sort = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="MS-Code (Sortierung)",
        help_text="MS-Code (Sortierung)",
    ).set_extra(
        is_public=True,
        data_lookup="ms_code_sort",
    )
    shelfmark = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Signatur",
        help_text="Signatur",
    ).set_extra(
        is_public=True,
        data_lookup="shelfmark",
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="Signatur: <value>",
    )
    heading = models.TextField(
        blank=True, null=True,
        verbose_name="Heading",
        help_text="Heading",
    ).set_extra(
        is_public=True,
        data_lookup="heading",
        arche_prop="hasAlternativeTitle",
    )
    material = models.ForeignKey(
        SkosConcept,
        related_name='rvn_manuscript_material_skosconcept',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Material",
        help_text="Material",
    ).set_extra(
        is_public=True,
        data_lookup="material",
    )
    num_leaves = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Umfang",
        help_text="Umfang (Anzahl der Blätter)",
    ).set_extra(
        is_public=True,
        data_lookup="num_leaves",
        arche_prop="hasExtent",
        arche_prop_str_template="Number of leaves: <value>",
    )
    dimensions = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Dimensionen",
        help_text="Dimensionen",
    ).set_extra(
        is_public=True,
        data_lookup="dimensions",
        arche_prop="hasExtent",
        arche_prop_str_template="Dimensionen: <value>",
    )
    orig_data_csv = models.TextField(
        blank=True,
        null=True,
        verbose_name="The original data"
        ).set_extra(
            is_public=True
        )

    class Meta:
        
        ordering = [
            'ms_code_sort',
        ]
        verbose_name = "Manuscript"
    
    def __str__(self):
        if self.ms_code:
            return "{}".format(self.ms_code)
        else:
            return "{}".format(self.legacy_id)

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:manuscript_browse')
    
    @classmethod
    def get_source_table(self):
        return "manuscripts"
    
    
    @classmethod
    def get_natural_primary_key(self):
        return "id"
    
    @classmethod
    def get_createview_url(self):
        return reverse('archiv:manuscript_create')

    def get_absolute_url(self):
        return reverse('archiv:manuscript_detail', kwargs={'pk': self.id})

    def get_absolute_url(self):
        return reverse('archiv:manuscript_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:manuscript_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:manuscript_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:manuscript_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:manuscript_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


