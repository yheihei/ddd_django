# Generated by Django 3.0.2 on 2020-09-12 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='書籍名')),
                ('publisher', models.CharField(blank=True, max_length=255, verbose_name='出版社')),
                ('page', models.IntegerField(blank=True, default=0, verbose_name='ページ数')),
            ],
        ),
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, verbose_name='コメント')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impressions', to='cms.Book', verbose_name='書籍')),
            ],
        ),
    ]
