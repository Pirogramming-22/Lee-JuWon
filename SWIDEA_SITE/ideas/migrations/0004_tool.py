# Generated by Django 5.0.6 on 2025-01-15 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_alter_idea_description_alter_idea_dev_tool_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('explain', models.TextField()),
            ],
        ),
    ]
