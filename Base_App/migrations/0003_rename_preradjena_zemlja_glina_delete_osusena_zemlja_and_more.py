# Generated by Django 5.1.4 on 2024-12-24 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0002_osusena_zemlja_kolicina_vlazna_zemlja_kolicina'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Preradjena_zemlja',
            new_name='Glina',
        ),
        migrations.DeleteModel(
            name='Osusena_zemlja',
        ),
        migrations.DeleteModel(
            name='Sirova_zemlja',
        ),
        migrations.DeleteModel(
            name='Vlazna_Zemlja',
        ),
    ]
