# Generated by Django 4.1.3 on 2022-11-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_fc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluno',
            options={'verbose_name': 'Aluno'},
        ),
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(max_length=10),
        ),
    ]
