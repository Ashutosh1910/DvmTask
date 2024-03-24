# Generated by Django 4.2.10 on 2024-03-02 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProfPortal', '0001_initial'),
        ('StudentPortal', '0003_rename_of_course_course_eval_of_eval'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_profile',
            name='under_courses',
        ),
        migrations.AddField(
            model_name='enrolled_course',
            name='under_courses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProfPortal.course'),
        ),
    ]
