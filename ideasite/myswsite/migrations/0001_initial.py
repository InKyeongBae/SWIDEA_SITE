# Generated by Django 2.2.9 on 2021-01-13 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevTool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('kind', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('content', models.TextField(blank=True, null=True)),
                ('interest', models.IntegerField(default=0)),
                ('devtool', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='idea', to='myswsite.DevTool')),
            ],
        ),
    ]
