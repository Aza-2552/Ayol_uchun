# apps/payments/crud.py
from django.db import transaction
from django.shortcuts import get_object_or_404
from apps.payments.models import UserCard, Order, Transaction, Providers, ProviderCredentials


# -------------------- USER CARD --------------------
def create_user_card(user, card_token, provider, **extra_fields):
    return UserCard.objects.create(
        user=user,
        card_token=card_token,
        provider=provider,
        **extra_fields
    )


def get_user_card(card_id):
    return get_object_or_404(UserCard, id=card_id)


def delete_user_card(card_id):
    card = get_object_or_404(UserCard, id=card_id)
    card.delete()
    return True


# -------------------- ORDER --------------------
def create_order(user, course=None, webinar=None, amount=0, provider=None):
    with transaction.atomic():
        order = Order.objects.create(
            user=user,
            course=course,
            webinar=webinar,
            amount=amount,
        )
        transaction_obj = Transaction.objects.create(
            order=order,
            provider=provider,
            amount=amount,
        )
    return order, transaction_obj


def get_order(order_id):
    return get_object_or_404(Order, id=order_id)


def update_order_status(order_id, status, is_paid=False):
    order = get_object_or_404(Order, id=order_id)
    order.status = status
    order.is_paid = is_paid
    order.save(update_fields=["status", "is_paid"])
    return order


# -------------------- TRANSACTION --------------------
def create_transaction(order, provider, amount, status="PENDING", card=None):
    return Transaction.objects.create(
        order=order,
        provider=provider,
        amount=amount,
        status=status,
        card=card,
    )


def get_transaction(transaction_id):
    return get_object_or_404(Transaction, id=transaction_id)


def cancel_transaction(transaction_id, reason="User Cancelled"):
    tx = get_object_or_404(Transaction, id=transaction_id)
    tx.cancel_transaction(reason)
    return tx


def complete_transaction(transaction_id, provider, transaction_remote_id, card=None):
    tx = get_object_or_404(Transaction, id=transaction_id)
    tx.apply_transaction(provider=provider, transaction_id=transaction_remote_id, card=card)
    return tx


# -------------------- PROVIDERS --------------------
def get_provider_by_key(key):
    return Providers.objects.filter(key=key).last()


def create_provider(name, key):
    return Providers.objects.create(name=name, key=key)


# -------------------- PROVIDER CREDENTIALS --------------------
def add_provider_credential(provider, key, value, description=None):
    return ProviderCredentials.objects.create(
        provider=provider,
        key=key,
        value=value,
        key_description=description,
    )


def get_provider_credentials(provider):
    return ProviderCredentials.objects.filter(provider=provider, is_active=True)
