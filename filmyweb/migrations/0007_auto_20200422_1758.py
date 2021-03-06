# Generated by Django 3.0.5 on 2020-04-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0006_auto_20200422_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Horror'), (4, 'Drama'), (0, 'Inne'), (5, 'Thiler'), (2, 'Komedia'), (3, 'Sci-fi')], default=0),
        ),
        migrations.CreateModel(
            name='Aktor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=32)),
                ('nazwisko', models.CharField(max_length=32)),
                ('filmy', models.ManyToManyField(to='filmyweb.Film')),
            ],
        ),
    ]
