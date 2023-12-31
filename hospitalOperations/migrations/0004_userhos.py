# Generated by Django 4.2.2 on 2023-10-01 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_rename_last_loginend_userdetails_last_logined'),
        ('hospitalOperations', '0003_delete_userhos'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserHos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messageRequested', models.CharField(max_length=2000)),
                ('RequestApproved', models.BooleanField()),
                ('hos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalOperations.hospitallogin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.userlogin')),
            ],
        ),
    ]
