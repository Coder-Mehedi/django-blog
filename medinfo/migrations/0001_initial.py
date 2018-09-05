# Generated by Django 2.1 on 2018-09-05 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('indications', models.CharField(max_length=600)),
                ('adult_dose', models.CharField(max_length=200)),
                ('child_dose', models.CharField(max_length=200)),
                ('renal_dose', models.CharField(max_length=200)),
                ('contraindications', models.CharField(max_length=100)),
                ('side_effects', models.CharField(max_length=800)),
                ('precautions_and_worning', models.CharField(max_length=800)),
                ('pregnancy_category', models.CharField(max_length=800)),
                ('therapeutic_class', models.CharField(max_length=100)),
                ('mode_of_action', models.CharField(max_length=600)),
                ('interaction', models.CharField(max_length=800)),
                ('pack_size_price', models.CharField(max_length=300)),
            ],
        ),
    ]