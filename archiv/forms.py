# generated by appcreator
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_bootstrap5.bootstrap5 import BS5Accordion
from crispy_forms.bootstrap import AccordionGroup

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
    Einband,
    Schrift,
)


class AutorFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AutorFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Filter",
                    "name",
                    "biogr_daten",
                    "orden",
                    "jahrhundert",
                    css_id="more",
                ),
                AccordionGroup(
                    "weitere Filter",
                    "name_gnd",
                    "id",
                    "gnd_id",
                    "legacy_id",
                    css_id="admin_search",
                ),
            ),
        )


class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AutorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class BibliothekFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(BibliothekFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Filter",
                    "lib_code",
                    "lib_name",
                    "lib_type",
                    "short_name",
                    "location",
                    "address",
                    css_id="more",
                ),
                AccordionGroup("weitere Filter", "legacy_id", css_id="admin_search"),
            ),
        )


class BibliothekForm(forms.ModelForm):
    lib_type = forms.ModelChoiceField(
        required=False,
        label="Art der Bibliothek",
        queryset=SkosConcept.objects.filter(collection__name="lib_type"),
    )

    class Meta:
        model = Bibliothek
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BibliothekForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class InitiumFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(InitiumFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Filter",
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
                    css_id="more",
                ),
                AccordionGroup("weitere Filter", "legacy_id", css_id="admin_search"),
            ),
        )


class InitiumForm(forms.ModelForm):
    sprache = forms.ModelChoiceField(
        required=False,
        label="Sprache",
        queryset=SkosConcept.objects.filter(collection__name="sprache"),
    )

    class Meta:
        model = Initium
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(InitiumForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class LiteraturFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(LiteraturFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Filter",
                    "legacy_pk",
                    "kurz_zitat",
                    "autor_nachname",
                    "jahr",
                    "nr",
                    "kz",
                    "vollzitat",
                    "anmerkung",
                    css_id="more",
                ),
                AccordionGroup("weitere Filter", "legacy_id", css_id="admin_search"),
            ),
        )


class LiteraturForm(forms.ModelForm):

    class Meta:
        model = Literatur
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(LiteraturForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class ManuscriptFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ManuscriptFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Filter",
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
                    css_id="more",
                ),
                AccordionGroup("weitere Filter", "legacy_id", css_id="admin_search"),
            ),
        )


class ManuscriptForm(forms.ModelForm):
    material = forms.ModelChoiceField(
        required=False,
        label="Material",
        queryset=SkosConcept.objects.filter(collection__name="material"),
    )

    class Meta:
        model = Manuscript
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ManuscriptForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class MsDescFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(MsDescFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Filter",
                    "legacy_pk",
                    "manuscript",
                    "bibliography",
                    "phys_desc",
                    "content",
                    "verfasser",
                    "created",
                    css_id="more",
                ),
                AccordionGroup("weitere Filter", "legacy_id", css_id="admin_search"),
            ),
        )


class MsDescForm(forms.ModelForm):

    class Meta:
        model = MsDesc
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(MsDescForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class MsPartFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(MsPartFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Filter",
                    "legacy_pk",
                    "part_of_manuscript",
                    "range",
                    "date_str",
                    "origin_date",
                    "date_begin",
                    "date_end",
                    css_id="more",
                ),
                AccordionGroup("weitere Filter", "legacy_id", css_id="admin_search"),
            ),
        )


class MsPartForm(forms.ModelForm):

    class Meta:
        model = MsPart
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(MsPartForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class PlaceFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PlaceFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup("Filter", "name", css_id="more"),
                AccordionGroup("weitere Filter", "legacy_id", css_id="admin_search"),
            ),
        )


class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class VerfasserFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(VerfasserFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup("Filter", "name", css_id="more"),
                AccordionGroup("weitere Filter", "legacy_id", css_id="admin_search"),
            ),
        )


class VerfasserForm(forms.ModelForm):

    class Meta:
        model = Verfasser
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(VerfasserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class WebLitFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(WebLitFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Filter",
                    "legacy_pk",
                    "url",
                    "beschriftung",
                    "literatur",
                    css_id="more",
                ),
                AccordionGroup("weitere Filter", "legacy_id", css_id="admin_search"),
            ),
        )


class WebLitForm(forms.ModelForm):

    class Meta:
        model = WebLit
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(WebLitForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class WerkInstanzFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(WerkInstanzFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Filter",
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
                    css_id="more",
                ),
                AccordionGroup("weitere Filter", "legacy_id", css_id="admin_search"),
            ),
        )


class WerkInstanzForm(forms.ModelForm):
    sprache = forms.ModelChoiceField(
        required=False,
        label="Sprache",
        queryset=SkosConcept.objects.filter(collection__name="sprache"),
    )

    class Meta:
        model = WerkInstanz
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(WerkInstanzForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class ZitatFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ZitatFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Filter",
                    "legacy_pk",
                    "literatur",
                    "manuscript",
                    "kz_ms",
                    "signatur",
                    css_id="more",
                ),
                AccordionGroup("weitere Filter", "legacy_id", css_id="admin_search"),
            ),
        )


class ZitatForm(forms.ModelForm):

    class Meta:
        model = Zitat
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ZitatForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class EinbandFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(EinbandFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Filter",
                    "legacy_pk",
                    "manuscript",
                    "verfasser",
                    css_id="more",
                ),
                AccordionGroup("weitere Filter", "legacy_id", css_id="admin_search"),
            ),
        )


class EinbandForm(forms.ModelForm):

    class Meta:
        model = Einband
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EinbandForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class SchriftFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(SchriftFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Filter",
                    "legacy_pk",
                    "manuscript",
                    "verfasser",
                    css_id="more",
                ),
                AccordionGroup("weitere Filter", "legacy_id", css_id="admin_search"),
            ),
        )


class SchriftForm(forms.ModelForm):

    class Meta:
        model = Schrift
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SchriftForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )
