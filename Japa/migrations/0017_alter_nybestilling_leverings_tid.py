# Generated by Django 4.2.10 on 2024-03-03 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Japa', '0016_nybestilling_accepteret'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nybestilling',
            name='Leverings_tid',
            field=models.TextField(),
        ),
    ]