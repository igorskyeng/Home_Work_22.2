# Generated by Django 5.0.4 on 2024-04-28 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_delete_material'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Блог', 'verbose_name_plural': 'Блоги'},
        ),
    ]
