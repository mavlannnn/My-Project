# Generated by Django 4.2.10 on 2024-02-27 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wristwatch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=100)),
                ('available_items', models.ManyToManyField(to='wristwatch.watch')),
                ('sales_history', models.ManyToManyField(to='wristwatch.order')),
            ],
        ),
    ]
