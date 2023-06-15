from utils.wooapi import APIKey
from woocommerce import API

wcapi_key = APIKey(
    domain='silegend.com',
    cookies=[
        {
            "domain": "silegend.com",
            "hostOnly": True,
            "httpOnly": False,
            "name": "wordpress_test_cookie",
            "path": "/",
            "sameSite": None,
            "secure": True,
            "session": True,
            "storeId": None,
            "value": "WP%20Cookie%20check"
        },
        {
            "domain": "silegend.com",
            "expirationDate": 1718300231.961251,
            "hostOnly": True,
            "httpOnly": False,
            "name": "wp-settings-time-5",
            "path": "/",
            "sameSite": None,
            "secure": True,
            "session": False,
            "storeId": None,
            "value": "1686764231"
        },
        {
            "domain": "silegend.com",
            "hostOnly": True,
            "httpOnly": False,
            "name": "tk_ai",
            "path": "/",
            "sameSite": None,
            "secure": False,
            "session": True,
            "storeId": None,
            "value": "woo%3ATexhoAaP4f0LVgtS%2BoQmIANV"
        },
        {
            "domain": "silegend.com",
            "hostOnly": True,
            "httpOnly": True,
            "name": "wordpress_sec_091348d5935107ab5f95c23ec9437605",
            "path": "/wp-admin",
            "sameSite": None,
            "secure": True,
            "session": True,
            "storeId": None,
            "value": "teamkhacanh%7C1686937030%7CBaQM4DKjQFOcCexQQBX5xa3WFKA8Jl1zDvkFZeDwqzR%7C7590361b35e9d2bc7f89ccc84744fedd0fab81ec15f63b95a4fbd7cf7788f334"
        },
        {
            "domain": "silegend.com",
            "expirationDate": 1718300231.96123,
            "hostOnly": True,
            "httpOnly": False,
            "name": "wp-settings-5",
            "path": "/",
            "sameSite": None,
            "secure": True,
            "session": False,
            "storeId": None,
            "value": "libraryContent%3Dbrowse"
        },
        {
            "domain": "silegend.com",
            "hostOnly": True,
            "httpOnly": True,
            "name": "wordpress_logged_in_091348d5935107ab5f95c23ec9437605",
            "path": "/",
            "sameSite": None,
            "secure": True,
            "session": True,
            "storeId": None,
            "value": "teamkhacanh%7C1686937030%7CBaQM4DKjQFOcCexQQBX5xa3WFKA8Jl1zDvkFZeDwqzR%7Cb62e28504320e114ab67de33e13796bcc9478c4375c2d99b0d9ac9806ef1aeb8"
        }
    ]
)

# Create a new api key
wcapi_key.create()

wcapi = API(
    url="https://silegend.com",
    consumer_key=wcapi_key.get_consumer_key(),
    consumer_secret=wcapi_key.get_consumer_secret(),
    wp_api=True,
    version="wc/v3"
)

data = {
    "type": "simple",
    "sku": "tumbler-20230614-001",
    "name": "Blossom 40 oz Stainless Steel Tumbler",
    "status": "publish",
    "featured": False,
    "catalog_visibility": "visible",
    "short_description": "",
    "description": "<p>SUITABLE FOR COLD DRINKS: This insulated mug uses stainless steel to provide a keep-cold effect without sweating.</p><p>LEAK-PROOF LID: The double-threaded designed portable insulated cup comes with a handle and is made for lefties and righties and prevents leaks. The cup is dishwasher safe.</p><p>VERSATILE TUMBLER WITH HANDLE: The large durable handle provides a comfortable grip and the cup fits beautifully in a car cup holder making it ideal for travel.</p><p>Product Information:</p><p>Style: Straight cup</p><p>Liner material: 304 Stainless Steel</p><p>Shell material: 201 Stainless Steel</p><p>Thermal insulation performance: 12-24 hours</p><p>Material: Inner 304 Outer 201</p><p>Style: Sport</p><p>Function: Thermal Insulation</p><p>Size: 26×9.8×7.5cm</p><p>Colors: Green Gray Brown Light Blue Black White Light Pink Hot Pink</p><p>Capacity: 1200ML</p><p>Packing list: Water cup X1PCS</p><p>2 Version for you to choose from.</p><p>This 40oz stainless steel tumbler comes with a handle lid and straw. Its large capacity makes it a match for beer, water or any other cold beverage. The powder-coated tumbler is ideal for outdoor camping and is vacuum-insulated ensuring that your drink stays at a stable temperature for longer.</p><p>Production may take longer than expected as we sell out almost daily. But you can expect the best price here with just a little bit longer wait! We love and thank you guys for your support!</p>",
    "tax_status": "taxable",
    "stock_status": "instock",
    "backorders": "no",
    "sold_individually": False,
    "regular_price": "21.99",
    "categories": [
        {
            "id": 20,
            "name": "Home & Garden"
        },
        {
            "id": 30,
            "name": "Kitchen & Dining"
        },
        {
            "id": 40,
            "name": "Tableware"
        },
        {
            "id": 50,
            "name": "Drinkware"
        },
        {
            "id": 60,
            "name": "Tumblers"
        }
    ],
    "tags": [
        {
            "name": "40 ounce tumbler"
        },
        {
            "name": "40oz Quencher"
        },
        {
            "name": "40oz tumbler"
        },
        {
            "name": "Adventure Quencher"
        },
        {
            "name": "floral tumbler"
        },
        {
            "name": "Handle Tumbler"
        },
        {
            "name": "large cup"
        },
        {
            "name": "large tumbler"
        },
        {
            "name": "Quencher"
        },
        {
            "name": "tumbler 40oz"
        },
        {
            "name": "tumbler with handle"
        }
    ],
    "meta_data": [
        {
            "key": "fifu_list_url",
            "value": "https://cdn.shopify.com/s/files/1/0074/8198/3035/files/1-Blossom_2000x.jpg?v=1685611908|https://cdn.shopify.com/s/files/1/0074/8198/3035/files/2000x2000_2000x.jpg?v=1686736146"
        }
    ]
}

# Up the product
wcapi.post("products", data)

wcapi_key.delete()
