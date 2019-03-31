# Generated by Django 2.1.7 on 2019-03-29 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='수정 일시')),
                ('deleted_at', models.DateTimeField(help_text='삭제 일시', null=True)),
                ('name', models.CharField(max_length=40, verbose_name='이름')),
                ('email', models.CharField(max_length=128, unique=True, verbose_name='이메일')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
