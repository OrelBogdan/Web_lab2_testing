# Generated by Django 5.0.2 on 2024-03-08 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_patronymic_alter_user_surname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
