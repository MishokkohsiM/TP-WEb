# Generated by Django 2.2 on 2019-04-15 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_remove_tag_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='question',
            field=models.ManyToManyField(related_name='tags', related_query_name='tag', to='questions.Question'),
        ),
    ]
