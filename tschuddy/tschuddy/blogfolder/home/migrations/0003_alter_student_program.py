# Generated by Django 5.0 on 2024-10-17 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_cohortgroup_students_remove_program_courses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='program',
            field=models.CharField(max_length=50),
        ),
    ]
