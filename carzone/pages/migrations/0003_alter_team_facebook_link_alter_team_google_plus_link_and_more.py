# Generated by Django 4.2.6 on 2023-10-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_rename_teams_team"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team", name="facebook_link", field=models.URLField(default=""),
        ),
        migrations.AlterField(
            model_name="team",
            name="google_plus_link",
            field=models.URLField(default=""),
        ),
        migrations.AlterField(
            model_name="team", name="twitter_link", field=models.URLField(default=""),
        ),
    ]
