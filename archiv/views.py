# generated by appcreator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .filters import (
    AutorListFilter,
    BibliothekListFilter,
    InitiumListFilter,
    LiteraturListFilter,
    ManuscriptListFilter,
    MsDescListFilter,
    MsPartListFilter,
    PlaceListFilter,
    VerfasserListFilter,
    WebLitListFilter,
    WerkInstanzListFilter,
    ZitatListFilter,
    EinbandListFilter,
    SchriftListFilter,
    MsImageListFilter,
    PersonListFilter,
    MsProvListFilter,
)
from .forms import (
    AutorFilterFormHelper,
    AutorForm,
    BibliothekFilterFormHelper,
    BibliothekForm,
    InitiumFilterFormHelper,
    InitiumForm,
    LiteraturFilterFormHelper,
    LiteraturForm,
    ManuscriptFilterFormHelper,
    ManuscriptForm,
    MsDescFilterFormHelper,
    MsDescForm,
    MsPartFilterFormHelper,
    MsPartForm,
    PlaceFilterFormHelper,
    PlaceForm,
    VerfasserFilterFormHelper,
    VerfasserForm,
    WebLitFilterFormHelper,
    WebLitForm,
    WerkInstanzFilterFormHelper,
    WerkInstanzForm,
    ZitatFilterFormHelper,
    ZitatForm,
    EinbandFilterFormHelper,
    EinbandForm,
    SchriftFilterFormHelper,
    SchriftForm,
    MsImageFilterFormHelper,
    MsImageForm,
    PersonFilterFormHelper,
    PersonForm,
    MsProvFilterFormHelper,
    MsProvForm,
)
from .tables import (
    AutorTable,
    BibliothekTable,
    InitiumTable,
    LiteraturTable,
    ManuscriptTable,
    MsDescTable,
    MsPartTable,
    PlaceTable,
    VerfasserTable,
    WebLitTable,
    WerkInstanzTable,
    ZitatTable,
    EinbandTable,
    SchriftTable,
    MsImageTable,
    PersonTable,
    MsProvTable,
)
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
    MsImage,
    Person,
    MsProv,
)
from browsing.browsing_utils import (
    GenericListView,
    BaseCreateView,
    BaseUpdateView,
    BaseDetailView,
)


def manuscript_as_tei_view(request, pk):
    obj = get_object_or_404(Manuscript, pk=pk)
    tei = obj.get_tei()
    return HttpResponse(tei, content_type="application/xml")


class AutorListView(GenericListView):

    model = Autor
    filter_class = AutorListFilter
    formhelper_class = AutorFilterFormHelper
    table_class = AutorTable
    init_columns = [
        "id",
        "name",
        "biogr_daten",
        "jahrhundert",
        "orden",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class AutorDetailView(BaseDetailView):

    model = Autor
    template_name = "archiv/generic_detail.html"


class AutorCreate(BaseCreateView):

    model = Autor
    form_class = AutorForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AutorCreate, self).dispatch(*args, **kwargs)


class AutorUpdate(BaseUpdateView):

    model = Autor
    form_class = AutorForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AutorUpdate, self).dispatch(*args, **kwargs)


class AutorDelete(DeleteView):
    model = Autor
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:autor_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AutorDelete, self).dispatch(*args, **kwargs)


class BibliothekListView(GenericListView):

    model = Bibliothek
    filter_class = BibliothekListFilter
    formhelper_class = BibliothekFilterFormHelper
    table_class = BibliothekTable
    init_columns = ["id", "lib_name", "lib_code", "lib_type"]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class BibliothekDetailView(BaseDetailView):

    model = Bibliothek
    template_name = "archiv/bibliothek_detail.html"


class BibliothekCreate(BaseCreateView):

    model = Bibliothek
    form_class = BibliothekForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BibliothekCreate, self).dispatch(*args, **kwargs)


class BibliothekUpdate(BaseUpdateView):

    model = Bibliothek
    form_class = BibliothekForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BibliothekUpdate, self).dispatch(*args, **kwargs)


class BibliothekDelete(DeleteView):
    model = Bibliothek
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:bibliothek_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BibliothekDelete, self).dispatch(*args, **kwargs)


class InitiumListView(GenericListView):

    model = Initium
    filter_class = InitiumListFilter
    formhelper_class = InitiumFilterFormHelper
    table_class = InitiumTable
    init_columns = [
        "id",
        "manuscript",
        "werk",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class InitiumDetailView(BaseDetailView):

    model = Initium
    template_name = "archiv/generic_detail.html"


class InitiumCreate(BaseCreateView):

    model = Initium
    form_class = InitiumForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InitiumCreate, self).dispatch(*args, **kwargs)


class InitiumUpdate(BaseUpdateView):

    model = Initium
    form_class = InitiumForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InitiumUpdate, self).dispatch(*args, **kwargs)


class InitiumDelete(DeleteView):
    model = Initium
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:initium_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InitiumDelete, self).dispatch(*args, **kwargs)


class LiteraturListView(GenericListView):

    model = Literatur
    filter_class = LiteraturListFilter
    formhelper_class = LiteraturFilterFormHelper
    table_class = LiteraturTable
    init_columns = [
        "id",
        "vollzitat",
        "cit_short",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class LiteraturDetailView(BaseDetailView):

    model = Literatur
    template_name = "archiv/generic_detail.html"


class LiteraturCreate(BaseCreateView):

    model = Literatur
    form_class = LiteraturForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LiteraturCreate, self).dispatch(*args, **kwargs)


class LiteraturUpdate(BaseUpdateView):

    model = Literatur
    form_class = LiteraturForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LiteraturUpdate, self).dispatch(*args, **kwargs)


class LiteraturDelete(DeleteView):
    model = Literatur
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:literatur_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LiteraturDelete, self).dispatch(*args, **kwargs)


class ManuscriptListView(GenericListView):

    model = Manuscript
    filter_class = ManuscriptListFilter
    formhelper_class = ManuscriptFilterFormHelper
    table_class = ManuscriptTable
    init_columns = [
        "id",
        "shelfmark",
        "ms_code",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class ManuscriptDetailView(BaseDetailView):

    model = Manuscript
    template_name = "archiv/manuscript_detail.html"


class ManuscriptCreate(BaseCreateView):

    model = Manuscript
    form_class = ManuscriptForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ManuscriptCreate, self).dispatch(*args, **kwargs)


class ManuscriptUpdate(BaseUpdateView):

    model = Manuscript
    form_class = ManuscriptForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ManuscriptUpdate, self).dispatch(*args, **kwargs)


class ManuscriptDelete(DeleteView):
    model = Manuscript
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:manuscript_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ManuscriptDelete, self).dispatch(*args, **kwargs)


class MsDescListView(GenericListView):

    model = MsDesc
    filter_class = MsDescListFilter
    formhelper_class = MsDescFilterFormHelper
    table_class = MsDescTable
    init_columns = [
        "id",
        "legacy_pk",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class MsDescDetailView(BaseDetailView):

    model = MsDesc
    template_name = "archiv/generic_detail.html"


class MsDescCreate(BaseCreateView):

    model = MsDesc
    form_class = MsDescForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MsDescCreate, self).dispatch(*args, **kwargs)


class MsDescUpdate(BaseUpdateView):

    model = MsDesc
    form_class = MsDescForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MsDescUpdate, self).dispatch(*args, **kwargs)


class MsDescDelete(DeleteView):
    model = MsDesc
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:msdesc_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MsDescDelete, self).dispatch(*args, **kwargs)


class MsPartListView(GenericListView):

    model = MsPart
    filter_class = MsPartListFilter
    formhelper_class = MsPartFilterFormHelper
    table_class = MsPartTable
    init_columns = [
        "id",
        "part_of_manuscript",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class MsPartDetailView(BaseDetailView):

    model = MsPart
    template_name = "archiv/generic_detail.html"


class MsPartCreate(BaseCreateView):

    model = MsPart
    form_class = MsPartForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MsPartCreate, self).dispatch(*args, **kwargs)


class MsPartUpdate(BaseUpdateView):

    model = MsPart
    form_class = MsPartForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MsPartUpdate, self).dispatch(*args, **kwargs)


class MsPartDelete(DeleteView):
    model = MsPart
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:mspart_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MsPartDelete, self).dispatch(*args, **kwargs)


class PlaceListView(GenericListView):

    model = Place
    filter_class = PlaceListFilter
    formhelper_class = PlaceFilterFormHelper
    table_class = PlaceTable
    init_columns = [
        "id",
        "name",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class PlaceDetailView(BaseDetailView):

    model = Place
    template_name = "archiv/generic_detail.html"


class PlaceCreate(BaseCreateView):

    model = Place
    form_class = PlaceForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceCreate, self).dispatch(*args, **kwargs)


class PlaceUpdate(BaseUpdateView):

    model = Place
    form_class = PlaceForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceUpdate, self).dispatch(*args, **kwargs)


class PlaceDelete(DeleteView):
    model = Place
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:place_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceDelete, self).dispatch(*args, **kwargs)


class VerfasserListView(GenericListView):

    model = Verfasser
    filter_class = VerfasserListFilter
    formhelper_class = VerfasserFilterFormHelper
    table_class = VerfasserTable
    init_columns = [
        "id",
        "name",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class VerfasserDetailView(BaseDetailView):

    model = Verfasser
    template_name = "archiv/generic_detail.html"


class VerfasserCreate(BaseCreateView):

    model = Verfasser
    form_class = VerfasserForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(VerfasserCreate, self).dispatch(*args, **kwargs)


class VerfasserUpdate(BaseUpdateView):

    model = Verfasser
    form_class = VerfasserForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(VerfasserUpdate, self).dispatch(*args, **kwargs)


class VerfasserDelete(DeleteView):
    model = Verfasser
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:verfasser_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(VerfasserDelete, self).dispatch(*args, **kwargs)


class WebLitListView(GenericListView):

    model = WebLit
    filter_class = WebLitListFilter
    formhelper_class = WebLitFilterFormHelper
    table_class = WebLitTable
    init_columns = [
        "id",
        "url",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class WebLitDetailView(BaseDetailView):

    model = WebLit
    template_name = "archiv/generic_detail.html"


class WebLitCreate(BaseCreateView):

    model = WebLit
    form_class = WebLitForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WebLitCreate, self).dispatch(*args, **kwargs)


class WebLitUpdate(BaseUpdateView):

    model = WebLit
    form_class = WebLitForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WebLitUpdate, self).dispatch(*args, **kwargs)


class WebLitDelete(DeleteView):
    model = WebLit
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:weblit_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WebLitDelete, self).dispatch(*args, **kwargs)


class WerkInstanzListView(GenericListView):

    model = WerkInstanz
    filter_class = WerkInstanzListFilter
    formhelper_class = WerkInstanzFilterFormHelper
    table_class = WerkInstanzTable
    init_columns = [
        "id",
        "werk_titel",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class WerkInstanzDetailView(BaseDetailView):

    model = WerkInstanz
    template_name = "archiv/generic_detail.html"


class WerkInstanzCreate(BaseCreateView):

    model = WerkInstanz
    form_class = WerkInstanzForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WerkInstanzCreate, self).dispatch(*args, **kwargs)


class WerkInstanzUpdate(BaseUpdateView):

    model = WerkInstanz
    form_class = WerkInstanzForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WerkInstanzUpdate, self).dispatch(*args, **kwargs)


class WerkInstanzDelete(DeleteView):
    model = WerkInstanz
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:werkinstanz_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WerkInstanzDelete, self).dispatch(*args, **kwargs)


class ZitatListView(GenericListView):

    model = Zitat
    filter_class = ZitatListFilter
    formhelper_class = ZitatFilterFormHelper
    table_class = ZitatTable
    init_columns = [
        "id",
        "literatur",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class ZitatDetailView(BaseDetailView):

    model = Zitat
    template_name = "archiv/generic_detail.html"


class ZitatCreate(BaseCreateView):

    model = Zitat
    form_class = ZitatForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ZitatCreate, self).dispatch(*args, **kwargs)


class ZitatUpdate(BaseUpdateView):

    model = Zitat
    form_class = ZitatForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ZitatUpdate, self).dispatch(*args, **kwargs)


class ZitatDelete(DeleteView):
    model = Zitat
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:zitat_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ZitatDelete, self).dispatch(*args, **kwargs)


class EinbandListView(GenericListView):

    model = Einband
    filter_class = EinbandListFilter
    formhelper_class = EinbandFilterFormHelper
    table_class = EinbandTable
    init_columns = [
        "id",
        "legacy_pk",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class EinbandDetailView(BaseDetailView):

    model = Einband
    template_name = "archiv/generic_detail.html"


class EinbandCreate(BaseCreateView):

    model = Einband
    form_class = EinbandForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EinbandCreate, self).dispatch(*args, **kwargs)


class EinbandUpdate(BaseUpdateView):

    model = Einband
    form_class = EinbandForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EinbandUpdate, self).dispatch(*args, **kwargs)


class EinbandDelete(DeleteView):
    model = Einband
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:einband_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EinbandDelete, self).dispatch(*args, **kwargs)


class SchriftListView(GenericListView):

    model = Schrift
    filter_class = SchriftListFilter
    formhelper_class = SchriftFilterFormHelper
    table_class = SchriftTable
    init_columns = [
        "id",
        "schriftart",
        "schr_hohe",
        "schr_breite",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class SchriftDetailView(BaseDetailView):

    model = Schrift
    template_name = "archiv/generic_detail.html"


class SchriftCreate(BaseCreateView):

    model = Schrift
    form_class = SchriftForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SchriftCreate, self).dispatch(*args, **kwargs)


class SchriftUpdate(BaseUpdateView):

    model = Schrift
    form_class = SchriftForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SchriftUpdate, self).dispatch(*args, **kwargs)


class SchriftDelete(DeleteView):
    model = Schrift
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:schrift_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SchriftDelete, self).dispatch(*args, **kwargs)


class MsImageListView(GenericListView):

    model = MsImage
    filter_class = MsImageListFilter
    formhelper_class = MsImageFilterFormHelper
    table_class = MsImageTable
    init_columns = [
        "id",
        "filename",
        "manuscript",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class MsImageDetailView(BaseDetailView):

    model = MsImage
    template_name = "archiv/generic_detail.html"


class MsImageCreate(BaseCreateView):

    model = MsImage
    form_class = MsImageForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MsImageCreate, self).dispatch(*args, **kwargs)


class MsImageUpdate(BaseUpdateView):

    model = MsImage
    form_class = MsImageForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MsImageUpdate, self).dispatch(*args, **kwargs)


class MsImageDelete(DeleteView):
    model = MsImage
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:msimage_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MsImageDelete, self).dispatch(*args, **kwargs)


class PersonListView(GenericListView):

    model = Person
    filter_class = PersonListFilter
    formhelper_class = PersonFilterFormHelper
    table_class = PersonTable
    init_columns = [
        "id",
        "name",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class PersonDetailView(BaseDetailView):

    model = Person
    template_name = "archiv/generic_detail.html"


class PersonCreate(BaseCreateView):

    model = Person
    form_class = PersonForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonCreate, self).dispatch(*args, **kwargs)


class PersonUpdate(BaseUpdateView):

    model = Person
    form_class = PersonForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonUpdate, self).dispatch(*args, **kwargs)


class PersonDelete(DeleteView):
    model = Person
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:person_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonDelete, self).dispatch(*args, **kwargs)


class MsProvListView(GenericListView):

    model = MsProv
    filter_class = MsProvListFilter
    formhelper_class = MsProvFilterFormHelper
    table_class = MsProvTable
    init_columns = [
        "id",
        "manuscript",
        "previous_owner",
    ]
    enable_merge = True
    template_name = "archiv/generic_list.html"


class MsProvDetailView(BaseDetailView):

    model = MsProv
    template_name = "archiv/generic_detail.html"


class MsProvCreate(BaseCreateView):

    model = MsProv
    form_class = MsProvForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MsProvCreate, self).dispatch(*args, **kwargs)


class MsProvUpdate(BaseUpdateView):

    model = MsProv
    form_class = MsProvForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MsProvUpdate, self).dispatch(*args, **kwargs)


class MsProvDelete(DeleteView):
    model = MsProv
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:msprov_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MsProvDelete, self).dispatch(*args, **kwargs)
