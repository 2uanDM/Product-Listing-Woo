import requests
from bs4 import BeautifulSoup
import json
import urllib.parse


class API_key(object):
    def __init__(self, url: str, cookies: list) -> None:
        self.url = url
        self.cookies = cookies
        self.__revoke_url = ''
        self.__consumer_key = ''
        self.__consumer_secret = ''

    def __str__(self) -> str:
        return f'The consumer key is: {self.__consumer_key}\nThe consumer secrete key is: {self.__consumer_secret}\nRevoke url: {self.__revoke_url}'

    def __session(self) -> requests.Session:
        session = requests.Session()

        # Convert the cookies JSON into a dictionary
        cookies_dict = {cookie['name']: cookie['value']
                        for cookie in self.cookies}

        # Load the cookies into the session's cookie jar
        session.cookies.update(cookies_dict)

        return session

    def __security_key(self) -> str:
        # Request url
        url = f'https://{self.url}/wp-admin/admin.php?page=wc-settings&tab=advanced&section=keys&create-key=1'

        # Request headers
        headers = {
            'authority': self.url,
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
            response = self.__session().request(
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
        url = f'https://{self.url}/wp-admin/admin-ajax.php'

        # Request headers
        headers = {
            'authority': self.url,
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'vi,en-US;q=0.9,en;q=0.8,vi-VN;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': f'https://{self.url}',
            'pragma': 'no-cache',
            'referer': f'https://{self.url}/wp-admin/admin.php?page=wc-settings&tab=advanced&section=keys&create-key=1',
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
            response = self.__session().request(
                method='POST',
                url=url,
                headers=headers,
                data=payload
            )
        except Exception as e:
            print(e)
            return

        # Get the attributes
        index = response.text.find('"revoke_url"')
        response_text = response.text[:index-1] + r'}}'
        json_response = json.loads(response_text)
        self.__consumer_key = str(json_response['data']['consumer_key'])
        self.__consumer_secret = str(json_response['data']['consumer_secret'])

        start_revoke_url_index = response.text.find('https')
        end_revoke_url_index = response.text.find('>Revoke key')
        response_text = response.text[start_revoke_url_index:end_revoke_url_index-1]
        decoded_url = response_text.replace('\\/', '/').replace('&#038;', '&')
        self.__revoke_url = decoded_url[:-1]

        print('Tạo WooCommerce API key thành công')

    def delete(self) -> None:
        url = self.__revoke_url
        payload = {}
        headers = {
            'authority': self.url,
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
            response = self.__session().request(
                method='GET',
                url=url,
                headers=headers,
                data=payload
            )
        except Exception as e:
            print(e)
            return

        print('Xóa WooCommerce API key thành công')
