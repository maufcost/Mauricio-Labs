# Generated by Django 2.2 on 2019-05-25 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190525_0232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choices',
        ),
        migrations.AddField(
            model_name='question',
            name='choice1',
            field=models.CharField(default='choiceA', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='choice2',
            field=models.CharField(default='choiceB', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='choice3',
            field=models.CharField(default='choiceC', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='choice4',
            field=models.CharField(default='choiceD', max_length=100),
        ),
    ]
