# Generated by Django 2.1.3 on 2019-01-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_update_notes_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=30)),
            ],
        ),
    ]