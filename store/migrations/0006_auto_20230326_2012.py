# Generated by Django 3.2.18 on 2023-03-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_student_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(default='Unknown', max_length=150),
        ),
        migrations.AlterField(
            model_name='student',
            name='message',
            field=models.CharField(blank=True, default='Unknown', max_length=250),
        ),
    ]
