# Generated by Django 4.2.1 on 2023-05-09 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('number_home', models.CharField(max_length=30, verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
                'ordering': ['street'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='my_app.address', verbose_name='Адрес')),
                ('categories', models.ManyToManyField(to='my_app.category', verbose_name='Категории')),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='my_app.town', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Школа',
                'verbose_name_plural': 'Школы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=50, verbose_name='Почта')),
                ('additionally_phone', models.CharField(max_length=12, verbose_name='Дополнительный номер телефона')),
                ('working_mode', models.TextField(verbose_name='Режим работы')),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='school', to='my_app.school')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
