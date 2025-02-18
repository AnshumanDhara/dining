# Generated by Django 3.2.9 on 2024-07-02 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('phone_no', models.IntegerField()),
                ('website', models.URLField()),
                ('open_time', models.DateTimeField()),
                ('close_time', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
