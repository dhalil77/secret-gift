# Generated by Django 4.2.7 on 2023-11-22 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='R_user',
            fields=[
                ('r_user_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('r_user_nom', models.CharField(max_length=255)),
                ('r_user_prenom', models.CharField(max_length=255)),
                ('r_user_voeux', models.CharField(max_length=500)),
                ('r_user_jouer', models.BooleanField(default=False)),
                ('r_user_created_at', models.DateTimeField(auto_now_add=True)),
                ('r_user_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='R_user_secret',
            fields=[
                ('r_user_secret_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('r_user_secret_nom', models.CharField(max_length=255)),
                ('r_user_secret_prenom', models.CharField(max_length=255)),
                ('r_user_secret_choisie', models.BooleanField(default=False)),
                ('r_user_secret_created_at', models.DateTimeField(auto_now_add=True)),
                ('r_user_secret_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tj_user_preson_secret',
            fields=[
                ('tj_user_preson_secret_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('r_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.r_user')),
                ('r_user_secret_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.r_user_secret')),
            ],
        ),
    ]