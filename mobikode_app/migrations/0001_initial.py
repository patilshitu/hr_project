# Generated by Django 4.2.1 on 2023-06-02 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Skill', models.CharField(max_length=100)),
                ('Experience', models.CharField(max_length=100)),
                ('Relevant_Experience', models.CharField(max_length=100)),
                ('Company', models.CharField(max_length=100)),
                ('Availability', models.CharField(max_length=100)),
                ('Offer', models.CharField(max_length=100)),
                ('CTC', models.CharField(max_length=100)),
                ('ECTC', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Contact', models.CharField(max_length=100, unique=True)),
                ('Mail_id', models.EmailField(max_length=254, unique=True)),
                ('Reason_for_job_change', models.CharField(max_length=100)),
                ('Resume', models.FileField(blank=True, upload_to='')),
                ('PassPort', models.CharField(choices=[('Yes', '✅'), ('No', '❌')], max_length=50)),
                ('status', models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Reject', 'Reject'), ('Screen Reject ', 'Screen Reject'), ('Shortlisted', 'Shortlisted'), ('Hold', 'Hold')], max_length=50)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]