# Generated by Django 3.2.5 on 2023-01-18 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_rename_uerinfo_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
