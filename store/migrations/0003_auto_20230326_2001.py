# Generated by Django 3.2.18 on 2023-03-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20230302_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='description',
        ),
        migrations.AddField(
            model_name='student',
            name='lname',
            field=models.CharField(default='Unknow', max_length=150),
        ),
        migrations.AddField(
            model_name='student',
            name='message',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(default='Unknow', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
