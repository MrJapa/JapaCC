# Generated by Django 4.2.9 on 2024-03-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Japa', '0023_rename_iscourier_nybestilling_courier_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nybestilling',
            name='KundeNavn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]