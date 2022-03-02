# Bài 1

# import json


# j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
# j_str2 = json.dumps(j_str, indent=4, sort_keys=True)
# print(j_str2)


# Bài 2
# import json
# import urllib.request
# from pprint import *


# def read_json_api(URL):
#     DEFAULT_ENCODING = 'utf-8'
#     url_response = urllib.request.urlopen(URL)
    
#     if hasattr(url_response.headers, 'get_content_charset'):
#         encoding = url_response.headers.get_content_charset(DEFAULT_ENCODING)
#     else:
#         encoding = url_response.headers.getparam('charset') or DEFAULT_ENCODING
        
#     data = json.loads(url_response.read().decode(encoding))
#     return data

# if __name__ == '__main__':
#     url = 'http://py4e-data.dr-chuck.net/json?address=Ann+Arbor%2C+MI&key=42'
#     print(read_json_api(url))
#     content = read_json_api(url)
#     count_country = len(content["results"][0]["address_components"])
#     for x in range(0, count_country):
#         print(content["results"][0]["address_components"][x]["long_name"])




import xml.etree.cElementTree as ET


input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)

lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print("Name:", item.find('name').text)
    print("ID:", item.find('id').text)
    print("Atribute:", item.get('x'))