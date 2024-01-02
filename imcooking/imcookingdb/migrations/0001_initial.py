# Generated by Django 3.2.23 on 2024-01-02 12:47

from django.db import migrations, models
import django.db.models.deletion
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
                ('RecipePhoto', models.ImageField(upload_to='recipe_photos/')),
                ('PrepTime', models.IntegerField(null=True)),
                ('CookTime', models.IntegerField(null=True)),
                ('Rating', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=100)),
                ('UserEmail', models.CharField(max_length=100)),
                ('UserEmail2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StepOrder', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=300)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='imcookingdb.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('TypeId', models.IntegerField(null=True)),
                ('Amount', models.FloatField(null=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='imcookingdb.recipe')),
            ],
        ),
    ]
