# Generated by Django 4.2.10 on 2024-03-02 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProfPortal', '0001_initial'),
        ('StudentPortal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_eval',
            name='of_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProfPortal.evaluation'),
        ),
    ]
