# Generated by Django 3.2.23 on 2023-11-23 20:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('RecipeId', models.AutoField(primary_key=True, serialize=False)),
                ('RecipeTitle', models.CharField(max_length=100)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('RecipePhoto', models.CharField(max_length=100)),
                ('RecipeIngredients', models.CharField(max_length=300)),
                ('RecipeSteppes', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=100)),
                ('UserEmail', models.CharField(max_length=100)),
            ],
        ),
    ]