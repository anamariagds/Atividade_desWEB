# Generated by Django 4.1.3 on 2022-11-22 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_fc', '0002_alter_aluno_options_alter_aluno_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(max_length=20),
        ),
    ]