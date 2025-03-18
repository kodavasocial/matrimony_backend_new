# Generated by Django 4.2.16 on 2025-03-04 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0012_usersubscription_calls_usersubscription_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscription',
            name='mode',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usersubscription',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subscriptions.subscription'),
        ),
    ]
