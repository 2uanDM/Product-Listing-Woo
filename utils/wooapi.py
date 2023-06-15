import requests
from bs4 import BeautifulSoup
import json
from woocommerce import API


class APIKey(object):
    def __init__(self, domain: str, cookies: list) -> None:
        self.domain = domain
        self.cookies = cookies
        self.__revoke_url = ''
        self.__consumer_key = ''
        self.__consumer_secret = ''

    def __str__(self) -> str:
        return f'The consumer key is: {self.__consumer_key}\nThe consumer secrete key is: {self.__consumer_secret}\nRevoke url: {self.__revoke_url}'

    def get_revoke_url(self):
        return self.__revoke_url

    def get_consumer_key(self):
        return self.__consumer_key

    def get_consumer_secret(self):
        return self.__consumer_secret

    def session(self) -> requests.Session:
        session = requests.Session()

        # Convert the cookies JSON into a dictionary
        cookies_dict = {cookie['name']: cookie['value']
                        for cookie in self.cookies}

        # Load the cookies into the session's cookie jar
        session.cookies.update(cookies_dict)

        return session

    def __security_key(self) -> str:
        # Request url
        url = f'https://{self.domain}/wp-admin/admin.php?page=wc-settings&tab=advanced&section=keys&create-key=1'

        # Request headers
        headers = {
            'authority': self.domain,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi,en-US;q=0.9,en;q=0.8,vi-VN;q=0.7',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

        # Request payload
        payload = {}
        try:
            response = self.session().request(
                method='GET',
                url=url,
                headers=headers,
                data=payload
            )
        except Exception as e:
            print(e)
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        script_tag = soup.find('script', {'id': 'wc-api-keys-js-extra'})

        js_code = script_tag.contents[0]
        start_index = js_code.index('{')
        end_index = js_code.rindex('}') + 1
        json_str = js_code[start_index:end_index]

        data = json.loads(json_str)

        return data['update_api_nonce']

    def create(self) -> None:
        # Request url
        url = f'https://{self.domain}/wp-admin/admin-ajax.php'

        # Request headers
        headers = {
            'authority': self.domain,
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'vi,en-US;q=0.9,en;q=0.8,vi-VN;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': f'https://{self.domain}',
            'pragma': 'no-cache',
            'referer': f'https://{self.domain}/wp-admin/admin.php?page=wc-settings&tab=advanced&section=keys&create-key=1',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }

        # Request payload
        payload = f'action=woocommerce_update_api_key&security={self.__security_key()}&key_id=0&description=test&user=5&permissions=read_write'

        try:
            response = self.session().request(
                method='POST',
                url=url,
                headers=headers,
                data=payload
            )
        except Exception as e:
            print(e)
            return

        if response.status_code == 200:
            # Get the attributes
            index = response.text.find('"revoke_url"')
            response_text = response.text[:index-1] + r'}}'
            json_response = json.loads(response_text)
            self.__consumer_key = str(json_response['data']['consumer_key'])
            self.__consumer_secret = str(
                json_response['data']['consumer_secret'])

            start_revoke_url_index = response.text.find('https')
            end_revoke_url_index = response.text.find('>Revoke key')
            response_text = response.text[start_revoke_url_index:end_revoke_url_index-1]
            decoded_url = response_text.replace(
                '\\/', '/').replace('&#038;', '&')
            self.__revoke_url = decoded_url[:-1]

            print('Tạo WooCommerce API key thành công')
        else:
            print('Tạo WooCommerce API key thất bại')

    def delete(self) -> None:
        url = self.__revoke_url
        payload = {}
        headers = {
            'authority': self.domain,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi,en-US;q=0.9,en;q=0.8,vi-VN;q=0.7',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

        try:
            response = self.session().request(
                method='GET',
                url=url,
                headers=headers,
                data=payload
            )
        except Exception as e:
            print(e)
            return

        if response.status_code == 200:
            print('Xóa WooCommerce API key thành công')
        else:
            print('Xóa WooCommerce API key thất bại')

def upload_product(domain: str, cookies: list, data: dict) -> None:
    wcapi_key = APIKey(
        domain=domain,
        cookies=cookies,
        data=data
    )

    # Create a new api key
    try:
        wcapi_key.create()
        print('Tạo API Key thành công')
    except Exception as e:
        print(f'Tạo API Key thất bại: {e}')
        return
        
    # Create woocommerce API object
    wcapi = API(
        url=f'https://{domain}',
        consumer_key=wcapi_key.get_consumer_key(),
        consumer_secret=wcapi_key.get_consumer_secret(),
        wp_api=True,
        version="wc/v3"
    )

    # Upload the product
    print('Đang upload product ...')
    wcapi.post("products", data)
    
    # Remove the API key
    try:
        wcapi_key.delete()
        print('Xóa API Key thành công')
    except Exception as e:
        print(f'Xoá API Key thất bại: {e}')
        return