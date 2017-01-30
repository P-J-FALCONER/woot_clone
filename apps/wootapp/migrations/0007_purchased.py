from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0004_auto_20170129_1515'),
        ('wootapp', '0006_auto_20170130_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchased',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_purchased', to='wootapp.Items')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_purchased', to='loginapp.Users')),
            ],
        ),
    ]
