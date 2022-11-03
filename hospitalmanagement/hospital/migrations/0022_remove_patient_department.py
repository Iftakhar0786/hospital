

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0021_patient_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='department',
        ),
    ]
