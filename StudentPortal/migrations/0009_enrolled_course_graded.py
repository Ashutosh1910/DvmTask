# Generated by Django 4.2.10 on 2024-03-02 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentPortal', '0008_alter_enrolled_course_under_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolled_course',
            name='graded',
            field=models.BooleanField(default=False),
        ),
    ]
