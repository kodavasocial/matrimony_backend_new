# Generated by Django 4.2.16 on 2024-12-03 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0009_usersubscription_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscription',
            name='addons',
            field=models.ManyToManyField(null=True, to='subscriptions.addon'),
        ),
    ]
