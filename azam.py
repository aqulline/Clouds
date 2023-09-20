from azampay import Azampay

import invdata

azampay = Azampay(app_name='Shoppy', client_id='f26d6f7e-d679-45d1-9333-0e8545313ba9', client_secret=invdata.secret,
                  x_api_key='<x_api_key>', sandbox=True)

checkout_response = azampay.mobile_checkout(amount="100", mobile='255715700411', external_id='9060', provider='Tigo')
