# Generated by Django 3.2.10 on 2022-02-11 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examsection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remunerationform',
            name='chief_examiner_num',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='remunerationform',
            name='chief_examiner_rate',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='remunerationform',
            name='da_days',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='remunerationform',
            name='da_rate',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='remunerationform',
            name='lab_examiner_num',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='remunerationform',
            name='lab_examiner_rate',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='remunerationform',
            name='paper_setting_num',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='remunerationform',
            name='paper_setting_rate',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='remunerationform',
            name='paper_valuation_num',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='remunerationform',
            name='paper_valuation_rate',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='remunerationform',
            name='ta_days',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='remunerationform',
            name='ta_rate',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='remunerationform',
            name='viva_rate',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
