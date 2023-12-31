# Generated by Django 4.2.4 on 2023-08-24 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('img', models.ImageField(upload_to='static/img/')),
                ('seller', models.CharField(max_length=255)),
                ('name', models.TextField()),
                ('stars', models.IntegerField()),
                ('price', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField()),
                ('new', models.BooleanField()),
                ('added', models.BooleanField()),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_header_h2', models.CharField(max_length=255)),
                ('page_header_p', models.TextField()),
                ('hero_button_text', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='static/img/')),
                ('hero_h4', models.TextField()),
                ('hero_h2', models.TextField()),
                ('hero_h1', models.TextField()),
                ('hero_p', models.TextField()),
                ('hero_button_text', models.CharField(max_length=255)),
                ('feature1_img', models.ImageField(upload_to='static/img/')),
                ('feature2_img', models.ImageField(upload_to='static/img/')),
                ('feature3_img', models.ImageField(upload_to='static/img/')),
                ('feature4_img', models.ImageField(upload_to='static/img/')),
                ('feature5_img', models.ImageField(upload_to='static/img/')),
                ('feature6_img', models.ImageField(upload_to='static/img/')),
                ('feature1_text', models.CharField(max_length=255)),
                ('feature2_text', models.CharField(max_length=255)),
                ('feature3_text', models.CharField(max_length=255)),
                ('feature4_text', models.CharField(max_length=255)),
                ('feature5_text', models.CharField(max_length=255)),
                ('feature6_text', models.CharField(max_length=255)),
                ('banner_h4', models.CharField(max_length=255)),
                ('banner_h2', models.TextField()),
                ('banner_button_text', models.CharField(max_length=255)),
                ('sm_banner1_h4', models.CharField(max_length=255)),
                ('sm_banner1_h2', models.TextField()),
                ('sm_banner1_span', models.TextField()),
                ('sm_banner1_button_text', models.CharField(max_length=255)),
                ('sm_banner2_h4', models.CharField(max_length=255)),
                ('sm_banner2_h2', models.TextField()),
                ('sm_banner2_span', models.TextField()),
                ('sm_banner2_button_text', models.CharField(max_length=255)),
                ('vsm_banner1_h4', models.CharField(max_length=255)),
                ('vsm_banner1_h2', models.TextField()),
                ('vsm_banner2_h4', models.CharField(max_length=255)),
                ('vsm_banner2_h2', models.TextField()),
                ('vsm_banner3_h4', models.CharField(max_length=255)),
                ('vsm_banner3_h2', models.TextField()),
                ('contact_label', models.CharField(max_length=255)),
                ('address_label', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('phone_label', models.CharField(max_length=255)),
                ('phone', models.TextField()),
                ('hours_label', models.CharField(max_length=255)),
                ('hours', models.TextField()),
                ('facebook', models.TextField()),
                ('twitter', models.TextField()),
                ('instagram', models.TextField()),
                ('pinterest', models.TextField()),
                ('youtube', models.TextField()),
                ('about_label', models.CharField(max_length=255)),
                ('about_us_label', models.CharField(max_length=255)),
                ('about_us', models.TextField()),
                ('delivery_information_label', models.CharField(max_length=255)),
                ('delivery_information', models.TextField()),
                ('privacy_policy_label', models.CharField(max_length=255)),
                ('privacy_policy', models.TextField()),
                ('terms_conditions_label', models.CharField(max_length=255)),
                ('terms_conditions', models.TextField()),
                ('contact_us_label', models.CharField(max_length=255)),
                ('contact_us', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='static/img/')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='static/img/')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='static/img/')),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='ecom.product')),
            ],
        ),
    ]
