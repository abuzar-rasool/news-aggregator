# Generated by Django 4.2 on 2023-05-01 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_cachednewsitem_query_delete_newscache_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
