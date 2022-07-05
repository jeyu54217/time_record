# Generated by Django 4.0.5 on 2022-07-05 01:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Act_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_main', models.CharField(max_length=225)),
                ('act_sub', models.CharField(max_length=225)),
                ('act_dtl', models.CharField(blank=True, default='', max_length=225, null=True)),
                ('act_note', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Date_record',
            fields=[
                ('id', models.BigAutoField(default=0, primary_key=True, serialize=False)),
                ('dt_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Time_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tm_start_time', models.TimeField()),
                ('tm_end_time', models.TimeField()),
                ('tm_duration_hr', models.DurationField()),
                ('act_act', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.act_record')),
                ('dt_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.date_record')),
            ],
        ),
        migrations.CreateModel(
            name='Calories_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cal_morning', models.IntegerField(blank=True, null=True)),
                ('cal_noon', models.IntegerField(blank=True, null=True)),
                ('cal_night', models.IntegerField(blank=True, null=True)),
                ('cal_goal', models.IntegerField(blank=True, null=True)),
                ('cal_deficit', models.IntegerField(blank=True, null=True)),
                ('dt_date', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core_app.date_record')),
            ],
        ),
        migrations.AddField(
            model_name='act_record',
            name='dt_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.date_record'),
        ),
    ]
