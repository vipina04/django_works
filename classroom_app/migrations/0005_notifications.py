# Generated by Django 4.0.3 on 2022-04-02 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom_app', '0004_alter_complaint_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('subject', models.CharField(max_length=100)),
                ('notification', models.TextField()),
            ],
        ),
    ]