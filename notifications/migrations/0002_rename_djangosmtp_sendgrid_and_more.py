# Generated by Django 5.0.7 on 2024-08-09 18:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("notifications", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="DjangoSMTP",
            new_name="SendGrid",
        ),
        migrations.RenameModel(
            old_name="TwilioSMS",
            new_name="VonageAPI",
        ),
    ]
