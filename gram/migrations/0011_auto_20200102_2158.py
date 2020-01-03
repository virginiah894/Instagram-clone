# Generated by Django 3.0.1 on 2020-01-02 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0010_post_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gram.Author'),
        ),
    ]