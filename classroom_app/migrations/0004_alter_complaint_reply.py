# Generated by Django 4.0.3 on 2022-04-02 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom_app', '0003_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='reply',
            field=models.TextField(blank=True, null=True),
        ),
    ]