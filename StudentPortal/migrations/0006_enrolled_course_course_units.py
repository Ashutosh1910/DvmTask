# Generated by Django 4.2.10 on 2024-03-02 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentPortal', '0005_rename_under_courses_enrolled_course_under_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolled_course',
            name='course_units',
            field=models.PositiveIntegerField(default=0),
        ),
    ]