# Generated by Django 3.2 on 2022-04-07 07:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=20, null=True)),
                ('market_value', models.DecimalField(decimal_places=3, default=0, max_digits=19)),
                ('change_percentage', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('initial_deposit_cost', models.DecimalField(decimal_places=3, default=0, max_digits=19)),
                ('is_public', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ActiveHoldings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_price_for_security', models.DecimalField(decimal_places=3, default=0, max_digits=19)),
                ('security_qty', models.PositiveBigIntegerField(default=0)),
                ('dividend_amount_received_total', models.DecimalField(decimal_places=3, default=0, max_digits=19)),
                ('yeild_on_cost', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('yeild', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('total_investment', models.DecimalField(decimal_places=3, default=0, max_digits=19)),
                ('current_value', models.DecimalField(decimal_places=3, default=0, max_digits=19)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holdings', to='portfolio_app.portfolio')),
                ('securities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_app.security')),
            ],
        ),
    ]