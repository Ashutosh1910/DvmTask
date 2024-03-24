# Generated by Django 4.2.10 on 2024-03-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfPortal', '0009_course_course_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='attached_file',
            field=models.FileField(blank=True, null=True, upload_to='announcement_files/'),
        ),
        migrations.AlterField(
            model_name='study_material',
            name='material',
            field=models.FileField(blank=True, null=True, upload_to='study_material_files/'),
        ),
    ]