# Generated by Django 5.0.6 on 2024-07-04 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasky', '0003_alter_task_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.TimeField(blank=True, null=True),
        ),
    ]