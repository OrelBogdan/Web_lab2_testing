# Generated by Django 5.0.2 on 2024-03-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=128, null=True),
        ),
    ]