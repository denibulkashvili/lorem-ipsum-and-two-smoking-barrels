# Generated by Django 2.2.1 on 2019-05-23 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0004_auto_20190523_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='quote_len',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]