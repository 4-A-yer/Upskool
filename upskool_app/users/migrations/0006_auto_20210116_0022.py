# Generated by Django 3.1.5 on 2021-01-15 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210116_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='type',
        ),
        migrations.CreateModel(
            name='NgoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
            options={
                'db_table': 'ngo_user',
            },
        ),
        migrations.CreateModel(
            name='GovUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
            options={
                'db_table': 'gov_user',
            },
        ),
    ]
