import json
from urllib.parse import unquote_plus
response_text = '{'success':true,'data':{'user_id':5,'description':'test','permissions':'read_write','consumer_key':'ck_9bb3410113f2024182396ad1c976ba4092c8d247','consumer_secret':'cs_a6cf473c9b8829490cd02ca132f8a5b0e31e03a7','truncated_key':'2c8d247','message':'API Key generated successfully. Make sure to copy your new keys now as the secret key will be hidden once you leave this page.','revoke_url':'<a style=\'color: #a00; text-decoration: none;\' href=\'https:\/\/silegend.com\/wp-admin\/admin.php?page=wc-settings&#038;tab=advanced&#038;section=keys&#038;revoke-key=11&#038;_wpnonce=609a5f7d81\'>Revoke key<\/a>'}}'


# Create a new variable as the raw string literal of response_text

start_revoke_url_index = response_text.find('https')
end_revoke_url_index = response_text.find('>Revoke key')

response_text = response_text[start_revoke_url_index:end_revoke_url_index-1]

decoded_url = response_text.replace('\\/', '/').replace('&#038;', '&')

print(decoded_url)
