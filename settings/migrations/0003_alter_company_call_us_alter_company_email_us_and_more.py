# Generated by Django 4.2.4 on 2023-09-10 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_rename_weitter_link_company_twitter_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='call_us',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='email_us',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.IntegerField(blank=True, max_length=500, null=True),
        ),
    ]
