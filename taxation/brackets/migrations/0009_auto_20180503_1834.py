# Generated by Django 2.1.dev20180424160604 on 2018-05-03 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brackets', '0008_auto_20180502_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='fed_bracket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fed_bracket', to='brackets.Federal'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='state_bracket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='state_bracket', to='brackets.State'),
        ),
    ]
