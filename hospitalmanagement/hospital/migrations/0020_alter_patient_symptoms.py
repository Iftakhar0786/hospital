# Generated by Django 4.1 on 2022-10-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_alter_patient_symptoms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='symptoms',
            field=models.CharField(max_length=100),
        ),
    ]
