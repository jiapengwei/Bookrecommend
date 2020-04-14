# Generated by Django 2.2.4 on 2020-04-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_book_introduction'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(default='', max_length=50, verbose_name='编码')),
                ('name', models.CharField(default='', max_length=50, verbose_name='书名')),
                ('price', models.CharField(default='', max_length=50, verbose_name='价格')),
                ('cover', models.ImageField(default='img/default.png', upload_to='upload', verbose_name='封面')),
                ('url', models.URLField(blank=True, default='', verbose_name='URL')),
                ('publish', models.CharField(blank=True, default='', max_length=50, verbose_name='出版社')),
                ('rating', models.CharField(default='0', max_length=5, verbose_name='评分')),
            ],
            options={
                'verbose_name': '图书管理',
                'verbose_name_plural': '图书管理',
            },
        ),
        migrations.DeleteModel(
            name='book',
        ),
    ]