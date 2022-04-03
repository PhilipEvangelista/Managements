# Generated by Django 4.0.3 on 2022-03-28 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_history_select'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bitcoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('current_price', models.FloatField(default=0)),
                ('currency', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='history',
            name='payment',
            field=models.FloatField(default=0),
        ),
    ]