# Generated by Django 4.2 on 2023-05-01 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_newscache_last_fetched'),
    ]

    operations = [
        migrations.CreateModel(
            name='CachedNewsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_fetched', models.DateTimeField()),
                ('news_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.newsitem')),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=255)),
                ('news_items', models.ManyToManyField(through='core.CachedNewsItem', to='core.newsitem')),
            ],
        ),
        migrations.DeleteModel(
            name='NewsCache',
        ),
        migrations.AddField(
            model_name='cachednewsitem',
            name='query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.query'),
        ),
    ]