# Generated by Django 4.2 on 2024-07-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0005_course_owner_lesson_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='owner',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='владелец'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='owner',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='владелец'),
        ),
    ]
