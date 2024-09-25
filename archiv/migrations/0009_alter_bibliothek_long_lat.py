# Generated by Django 5.1.1 on 2024-09-25 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archiv", "0008_bibliothek_hbhistbb_bibliothek_hmml_img_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bibliothek",
            name="long_lat",
            field=models.CharField(
                blank=True,
                help_text="(Long,Lat)",
                max_length=250,
                null=True,
                verbose_name="Koordinaten",
            ),
        ),
    ]
