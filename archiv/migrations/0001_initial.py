# Generated by Django 3.1.1 on 2020-10-24 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vocabs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "legacy_id",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Legacy ID"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Name",
                        max_length=250,
                        verbose_name="Name",
                    ),
                ),
                (
                    "name_gnd",
                    models.CharField(
                        blank=True,
                        help_text="Name (GND)",
                        max_length=250,
                        verbose_name="Name (GND)",
                    ),
                ),
                (
                    "gnd_id",
                    models.CharField(
                        blank=True,
                        help_text="GND-ID",
                        max_length=250,
                        verbose_name="GND-ID",
                    ),
                ),
                (
                    "biogr_daten",
                    models.TextField(
                        blank=True,
                        help_text="Kurbiographie",
                        null=True,
                        verbose_name="Kurzbio",
                    ),
                ),
                (
                    "orig_data_csv",
                    models.TextField(
                        blank=True, null=True, verbose_name="The original data"
                    ),
                ),
            ],
            options={
                "verbose_name": "Autor",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Bibliothek",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "legacy_id",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Legacy ID"
                    ),
                ),
                (
                    "lib_code",
                    models.CharField(
                        blank=True,
                        help_text="Bibliothekscode",
                        max_length=250,
                        verbose_name="Bibliothekscode",
                    ),
                ),
                (
                    "lib_name",
                    models.CharField(
                        blank=True,
                        help_text="Name",
                        max_length=250,
                        verbose_name="Name",
                    ),
                ),
                (
                    "short_name",
                    models.CharField(
                        blank=True,
                        help_text="Name (Abkürzung)",
                        max_length=250,
                        verbose_name="Name (Abkürzung)",
                    ),
                ),
                (
                    "address",
                    models.TextField(
                        blank=True,
                        help_text="Adresse",
                        null=True,
                        verbose_name="Adresse",
                    ),
                ),
                (
                    "orig_data_csv",
                    models.TextField(
                        blank=True, null=True, verbose_name="The original data"
                    ),
                ),
                (
                    "lib_type",
                    models.ForeignKey(
                        blank=True,
                        help_text="Art der Bibliothek",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rvn_bibliothek_lib_type_skosconcept",
                        to="vocabs.skosconcept",
                        verbose_name="Art der Bibliothek",
                    ),
                ),
            ],
            options={
                "verbose_name": "Bibliothek",
                "ordering": ["lib_name"],
            },
        ),
        migrations.CreateModel(
            name="Manuscript",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "legacy_id",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Legacy ID"
                    ),
                ),
                (
                    "legacy_pk",
                    models.IntegerField(
                        blank=True,
                        help_text="Primärschlüssel Alt",
                        null=True,
                        verbose_name="Primärschlüssel Alt",
                    ),
                ),
                (
                    "ms_code",
                    models.CharField(
                        blank=True,
                        help_text="MS-Code",
                        max_length=250,
                        verbose_name="MS-Code",
                    ),
                ),
                (
                    "ms_code_sort",
                    models.CharField(
                        blank=True,
                        help_text="MS-Code (Sortierung)",
                        max_length=250,
                        verbose_name="MS-Code (Sortierung)",
                    ),
                ),
                (
                    "shelfmark",
                    models.CharField(
                        blank=True,
                        help_text="Signatur",
                        max_length=250,
                        verbose_name="Signatur",
                    ),
                ),
                (
                    "heading",
                    models.TextField(
                        blank=True,
                        help_text="Heading",
                        null=True,
                        verbose_name="Heading",
                    ),
                ),
                (
                    "num_leaves",
                    models.CharField(
                        blank=True,
                        help_text="Umfang (Anzahl der Blätter)",
                        max_length=250,
                        verbose_name="Umfang",
                    ),
                ),
                (
                    "dimensions",
                    models.CharField(
                        blank=True,
                        help_text="Dimensionen",
                        max_length=250,
                        verbose_name="Dimensionen",
                    ),
                ),
                (
                    "origin_date",
                    models.CharField(
                        blank=True,
                        help_text="Entstehungsdatum",
                        max_length=250,
                        verbose_name="Entstehungsdatum",
                    ),
                ),
                (
                    "prov",
                    models.TextField(
                        blank=True,
                        help_text="Provenienz",
                        null=True,
                        verbose_name="Provenienz",
                    ),
                ),
                (
                    "fragm",
                    models.CharField(
                        blank=True,
                        help_text="Fragm",
                        max_length=250,
                        verbose_name="Fragm",
                    ),
                ),
                (
                    "hscensus",
                    models.IntegerField(
                        blank=True,
                        help_text="hscensus",
                        null=True,
                        verbose_name="hscensus",
                    ),
                ),
                (
                    "remarks",
                    models.TextField(
                        blank=True,
                        help_text="Anmerkungen",
                        null=True,
                        verbose_name="Anmerkungen",
                    ),
                ),
                (
                    "geschichte",
                    models.TextField(
                        blank=True,
                        help_text="Geschichte",
                        null=True,
                        verbose_name="Geschichte",
                    ),
                ),
                (
                    "orig_data_csv",
                    models.TextField(
                        blank=True, null=True, verbose_name="The original data"
                    ),
                ),
                (
                    "lib_code",
                    models.ForeignKey(
                        blank=True,
                        help_text="Bibliothek",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rvn_manuscript_lib_code_bibliothek",
                        to="archiv.bibliothek",
                        verbose_name="Bibliothek",
                    ),
                ),
                (
                    "material",
                    models.ForeignKey(
                        blank=True,
                        help_text="Material",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rvn_manuscript_material_skosconcept",
                        to="vocabs.skosconcept",
                        verbose_name="Material",
                    ),
                ),
            ],
            options={
                "verbose_name": "Manuscript",
                "ordering": ["ms_code_sort"],
            },
        ),
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "legacy_id",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Legacy ID"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Ortsname",
                        max_length=250,
                        verbose_name="Ortsname",
                    ),
                ),
                (
                    "orig_data_csv",
                    models.TextField(
                        blank=True, null=True, verbose_name="The original data"
                    ),
                ),
            ],
            options={
                "verbose_name": "Place",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Verfasser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "legacy_id",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Legacy ID"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Name",
                        max_length=250,
                        verbose_name="Name",
                    ),
                ),
                (
                    "orig_data_csv",
                    models.TextField(
                        blank=True, null=True, verbose_name="The original data"
                    ),
                ),
            ],
            options={
                "verbose_name": "Verfasser",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="WerkInstanz",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "legacy_id",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Legacy ID"
                    ),
                ),
                (
                    "legacy_pk",
                    models.IntegerField(
                        blank=True,
                        help_text="Primärschlüssel Alt",
                        null=True,
                        verbose_name="Primärschlüssel Alt",
                    ),
                ),
                (
                    "werk_titel",
                    models.TextField(
                        blank=True,
                        help_text="Titel des Werkes",
                        null=True,
                        verbose_name="Titel des Werkes",
                    ),
                ),
                (
                    "werk_titel_alt",
                    models.TextField(
                        blank=True,
                        help_text="Alternativer Werktitel",
                        null=True,
                        verbose_name="Alternativer Werktitel",
                    ),
                ),
                (
                    "textzeuge_kommentar",
                    models.TextField(
                        blank=True,
                        help_text="Kommentar zum Textzeugen",
                        null=True,
                        verbose_name="Kommentar zum Textzeugen",
                    ),
                ),
                (
                    "fol_start",
                    models.CharField(
                        blank=True,
                        help_text="Folio Beginn",
                        max_length=250,
                        verbose_name="Folio Beginn",
                    ),
                ),
                (
                    "fol_end",
                    models.CharField(
                        blank=True,
                        help_text="Folio Ende",
                        max_length=250,
                        verbose_name="Folio Ende",
                    ),
                ),
                (
                    "fol_sort",
                    models.CharField(
                        blank=True,
                        help_text="Folio (Sortierung)",
                        max_length=250,
                        verbose_name="Folio (Sortierung)",
                    ),
                ),
                (
                    "orig_data_csv",
                    models.TextField(
                        blank=True, null=True, verbose_name="The original data"
                    ),
                ),
                (
                    "autor",
                    models.ForeignKey(
                        blank=True,
                        help_text="Autor",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rvn_werkinstanz_autor_autor",
                        to="archiv.autor",
                        verbose_name="Autor",
                    ),
                ),
                (
                    "manuscript",
                    models.ForeignKey(
                        blank=True,
                        help_text="Manuscript",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rvn_werkinstanz_manuscript_manuscript",
                        to="archiv.manuscript",
                        verbose_name="Manuscript",
                    ),
                ),
                (
                    "sprache",
                    models.ForeignKey(
                        blank=True,
                        help_text="Sprache",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rvn_werkinstanz_sprache_skosconcept",
                        to="vocabs.skosconcept",
                        verbose_name="Sprache",
                    ),
                ),
            ],
            options={
                "verbose_name": "Instanz eines Werkes",
                "ordering": ["legacy_pk"],
            },
        ),
        migrations.CreateModel(
            name="MsPart",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "legacy_id",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Legacy ID"
                    ),
                ),
                (
                    "legacy_pk",
                    models.IntegerField(
                        blank=True,
                        help_text="Primärschlüssel Alt",
                        null=True,
                        verbose_name="Primärschlüssel Alt",
                    ),
                ),
                (
                    "range",
                    models.CharField(
                        blank=True,
                        help_text="von-bis",
                        max_length=250,
                        verbose_name="von-bis",
                    ),
                ),
                (
                    "date_str",
                    models.CharField(
                        blank=True,
                        help_text="Datum (str)",
                        max_length=250,
                        verbose_name="Datum (str)",
                    ),
                ),
                (
                    "origin_date",
                    models.CharField(
                        blank=True,
                        help_text="Datum (orig)",
                        max_length=250,
                        verbose_name="Datum (orig)",
                    ),
                ),
                (
                    "date_begin",
                    models.DateField(
                        blank=True,
                        help_text="Datum (start, norm)",
                        null=True,
                        verbose_name="Datum (start, norm)",
                    ),
                ),
                (
                    "date_end",
                    models.DateField(
                        blank=True,
                        help_text="Datum (end, norm)",
                        null=True,
                        verbose_name="Datum (end, norm)",
                    ),
                ),
                (
                    "orig_data_csv",
                    models.TextField(
                        blank=True, null=True, verbose_name="The original data"
                    ),
                ),
                (
                    "part_of_manuscript",
                    models.ForeignKey(
                        blank=True,
                        help_text="Teil von Handschrift",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rvn_mspart_part_of_manuscript_manuscript",
                        to="archiv.manuscript",
                        verbose_name="Teil von Handschrift",
                    ),
                ),
            ],
            options={
                "verbose_name": "MsPart",
                "ordering": ["legacy_pk"],
            },
        ),
        migrations.CreateModel(
            name="MsDesc",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "legacy_id",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Legacy ID"
                    ),
                ),
                (
                    "legacy_pk",
                    models.IntegerField(
                        blank=True,
                        help_text="Primärschlüssel Alt",
                        null=True,
                        verbose_name="Primärschlüssel Alt",
                    ),
                ),
                (
                    "bibliography",
                    models.TextField(
                        blank=True,
                        help_text="Bibliographie",
                        null=True,
                        verbose_name="Bibliographie",
                    ),
                ),
                (
                    "phys_desc",
                    models.TextField(
                        blank=True,
                        help_text="phys_desc",
                        null=True,
                        verbose_name="phys_desc",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        blank=True,
                        help_text="content",
                        null=True,
                        verbose_name="content",
                    ),
                ),
                (
                    "created",
                    models.DateField(
                        blank=True,
                        help_text="Erstellungsdatum",
                        null=True,
                        verbose_name="Erstellungsdatum",
                    ),
                ),
                (
                    "orig_data_csv",
                    models.TextField(
                        blank=True, null=True, verbose_name="The original data"
                    ),
                ),
                (
                    "manuscript",
                    models.ForeignKey(
                        blank=True,
                        help_text="Manuscript",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rvn_msdesc_manuscript_manuscript",
                        to="archiv.manuscript",
                        verbose_name="Manuscript",
                    ),
                ),
                (
                    "verfasser",
                    models.ForeignKey(
                        blank=True,
                        help_text="Verfasser*In",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rvn_msdesc_verfasser_verfasser",
                        to="archiv.verfasser",
                        verbose_name="Verfasser*In",
                    ),
                ),
            ],
            options={
                "verbose_name": "Manuscript Description",
                "ordering": ["legacy_pk"],
            },
        ),
        migrations.CreateModel(
            name="Initium",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "legacy_id",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Legacy ID"
                    ),
                ),
                (
                    "legacy_pk",
                    models.IntegerField(
                        blank=True,
                        help_text="Primärschlüssel Alt",
                        null=True,
                        verbose_name="Primärschlüssel Alt",
                    ),
                ),
                (
                    "initium",
                    models.TextField(
                        blank=True,
                        help_text="Initium",
                        null=True,
                        verbose_name="Inititum",
                    ),
                ),
                (
                    "explicit",
                    models.TextField(
                        blank=True,
                        help_text="Explicit",
                        null=True,
                        verbose_name="Explicit",
                    ),
                ),
                (
                    "fol",
                    models.CharField(
                        blank=True,
                        help_text="Folio",
                        max_length=250,
                        verbose_name="Folio",
                    ),
                ),
                (
                    "fol_sort",
                    models.CharField(
                        blank=True,
                        help_text="Folio (sort)",
                        max_length=250,
                        verbose_name="Folio (sort)",
                    ),
                ),
                (
                    "fol_end",
                    models.CharField(
                        blank=True,
                        help_text="Folio (end)",
                        max_length=250,
                        verbose_name="Folio (end)",
                    ),
                ),
                (
                    "orig_data_csv",
                    models.TextField(
                        blank=True, null=True, verbose_name="The original data"
                    ),
                ),
                (
                    "manuscript",
                    models.ForeignKey(
                        blank=True,
                        help_text="Manuscript",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rvn_initium_manuscript_manuscript",
                        to="archiv.manuscript",
                        verbose_name="Manuscript",
                    ),
                ),
            ],
            options={
                "verbose_name": "Initium",
                "ordering": ["legacy_pk"],
            },
        ),
        migrations.AddField(
            model_name="bibliothek",
            name="location",
            field=models.ForeignKey(
                blank=True,
                help_text="Ort",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="rvn_bibliothek_location_place",
                to="archiv.place",
                verbose_name="Ort",
            ),
        ),
    ]
