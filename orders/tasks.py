from celery import shared_task
from django.db import transaction
from .models import Order

@shared_task(bind=True)
def process_order(self, order_id):
    from .models import Product, OrderItem

    try:
        with transaction.atomic():
            order = Order.objects.select_for_update().get(id=order_id)
            if order.status != 'pending':
                return

            total = 0
            for item in order.items.select_related('product'):
                product = item.product

                if product.stock < item.quantity:
                    order.status = 'failed'
                    order.save()
                    return

                product.stock -= item.quantity
                product.save()
                total += product.price * item.quantity

            order.status = 'confirmed'
            order.save()

    except Exception as e:
        self.retry(exc=e)
