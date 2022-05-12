# Generated by Django 4.0.4 on 2022-05-11 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='date to start')),
                ('deadline_date', models.DateTimeField(verbose_name='date to finish')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('team', models.SmallIntegerField(choices=[(0, 'CEO'), (1, 'Development'), (2, 'Design'), (3, 'Data')])),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('detail', models.CharField(max_length=500)),
                ('status', models.SmallIntegerField(choices=[(0, 'in progress'), (1, 'done'), (2, 'delayed')], default=0)),
                ('start_date', models.DateTimeField(verbose_name='date to start')),
                ('deadline_date', models.DateTimeField(verbose_name='date to finish')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.user')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.user'),
        ),
    ]