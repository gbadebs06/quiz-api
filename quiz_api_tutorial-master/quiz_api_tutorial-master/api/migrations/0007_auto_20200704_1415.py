# Generated by Django 3.0.8 on 2020-07-04 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200704_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correct_opt',
        ),
        migrations.RemoveField(
            model_name='question',
            name='opt1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='opt2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='opt3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='opt4',
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=80)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Question')),
            ],
        ),
    ]