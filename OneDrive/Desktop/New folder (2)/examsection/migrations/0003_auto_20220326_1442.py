# Generated by Django 3.2.10 on 2022-03-26 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examsection', '0002_auto_20220211_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remunerationform',
            name='chief_examiner_num',
        ),
        migrations.RemoveField(
            model_name='remunerationform',
            name='chief_examiner_rate',
        ),
        migrations.RemoveField(
            model_name='remunerationform',
            name='lab_examiner_num',
        ),
        migrations.RemoveField(
            model_name='remunerationform',
            name='lab_examiner_rate',
        ),
        migrations.RemoveField(
            model_name='remunerationform',
            name='paper_setting_num',
        ),
        migrations.RemoveField(
            model_name='remunerationform',
            name='paper_setting_rate',
        ),
        migrations.RemoveField(
            model_name='remunerationform',
            name='paper_valuation_num',
        ),
        migrations.RemoveField(
            model_name='remunerationform',
            name='paper_valuation_rate',
        ),
        migrations.RemoveField(
            model_name='remunerationform',
            name='viva_rate',
        ),
        migrations.AddField(
            model_name='remunerationform',
            name='nature_of_work',
            field=models.CharField(choices=[('Question Paper Setting', 'Question Paper Setting'), ('Paper Valuation', 'Paper Valuation'), ('Chief Examiner', 'Chief Examiner'), ('Lab Examiner', 'Lab Examiner'), ('Thesis Viva Voce', 'Thesis Viva Voce')], default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='remunerationform',
            name='number_of_papers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='remunerationform',
            name='rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='remunerationform',
            name='branch',
            field=models.CharField(choices=[('CIV', 'CIV'), ('MECH', 'MECH'), ('EEE', 'EEE'), ('ECE', 'ECE'), ('CSE', 'CSE'), ('AI&ML', 'AI&ML'), ('CAD', 'CAD')], max_length=10),
        ),
    ]
