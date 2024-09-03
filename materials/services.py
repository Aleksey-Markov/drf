import requests
import stripe
from forex_python.converter import CurrencyRates
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(name, description):
    product = stripe.Product.create(name=name, description=description)
    return product


def create_stripe_price(amount):

    return stripe.Price.create(
        unit_amount=int(amount * 100),
        currency="rub",
        product_data={
            "name": "Course Purchase",
        },
    )


def create_stripe_session(price):

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price": price,
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url="http://127.0.0.1:8000/",
    )
    return session.get("id"), session.get("url")


def convert_currencies(rub_price):
    usd_price = 0
    response = requests.get(
        'http://api.currencyapi.com/v3/latest?apikey=cur_live_EIAV8SvKqqFNjLgdSh0OHdtMcMDONzT45RhllViZ&currencies=RUB'
    )
    if response.status_code == 200:
        usd_rate = response.json()['data']['RUB']['value']
        usd_price = rub_price * usd_rate
    return usd_price
