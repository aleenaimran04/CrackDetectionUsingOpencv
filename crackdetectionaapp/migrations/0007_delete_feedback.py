# Generated by Django 4.0.3 on 2022-05-09 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crackdetectionaapp', '0006_feedback_remove_crackdetect_detected_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='feedback',
        ),
    ]
