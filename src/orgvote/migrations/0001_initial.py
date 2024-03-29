# Generated by Django 4.2 on 2023-04-25 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgvote.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgvote.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('choice1', models.CharField(max_length=50)),
                ('choice1_votes', models.IntegerField(default=0)),
                ('choice2', models.CharField(max_length=50)),
                ('choice2_votes', models.IntegerField(default=0)),
                ('choice3', models.CharField(max_length=50)),
                ('choice3_votes', models.IntegerField(default=0)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgvote.organization')),
            ],
        ),
    ]
