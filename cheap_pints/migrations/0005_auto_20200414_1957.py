# Generated by Django 2.1.5 on 2020-04-14 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheap_pints', '0004_auto_20200414_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='pintprice',
            name='bar_id',
            field=models.AutoField(primary_key=True, serialize=False, auto_created=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pintprice',
            name='googleId',
            field=models.CharField(max_length=128),
        ),
    ]
