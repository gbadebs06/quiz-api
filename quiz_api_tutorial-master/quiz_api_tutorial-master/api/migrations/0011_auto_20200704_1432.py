# Generated by Django 3.0.8 on 2020-07-04 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_option_correct_opt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='correct_opt',
            new_name='is_correct',
        ),
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='api.Subject'),
        ),
    ]
