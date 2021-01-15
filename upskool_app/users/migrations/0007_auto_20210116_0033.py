# Generated by Django 3.1.5 on 2021-01-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210116_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ngouser',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='type',
            field=models.CharField(choices=[('Gov', 'Government'), ('NGO', 'NGO')], default='Gov', max_length=16),
        ),
        migrations.DeleteModel(
            name='GovUser',
        ),
        migrations.DeleteModel(
            name='NgoUser',
        ),
    ]