# Generated by Django 5.0.2 on 2024-03-10 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_user_sex_user_gender_alter_user_patronymic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.AddField(
            model_name='user',
            name='user_gender',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
