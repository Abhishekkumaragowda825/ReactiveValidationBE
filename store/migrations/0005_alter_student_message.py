# Generated by Django 3.2.18 on 2023-03-26 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20230326_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='message',
            field=models.CharField(blank=True, default=None, max_length=250),
        ),
    ]
