import requests

# headers = {
#     'accept': '*/*',
#     'accept-encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#     'Connection	': 'keep-alive',
#     'cookies': 'CXID=0DDCDF3AB524336D02F12EE46CD334E4; SUID=D4C85D7C3965860A5AA39D940000145A; IPLOC=CN2102; SUV=1531959792494460; sct=5; SNUID=B829F6A09C99EE1D34CBD8E59CC58ED4; ld=wyllllllll2bFdo5lllllVH5TZGlllllnLLdflllllwlllll9Zlll5@@@@@@@@@@; LSTMV=347%2C155; LCLKINT=4472; ABTEST=0|1531961096|v1; weixinIndexVisited=1; ppinf=5|1532852075|1534061675|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTclOUYlQjMlRTUlQTQlQjR8Y3J0OjEwOjE1MzI4NTIwNzV8cmVmbmljazoxODolRTclOUYlQjMlRTUlQTQlQjR8dXNlcmlkOjQ0Om85dDJsdUI5VE85TE1CemdVRDd5dC10RjI4MzBAd2VpeGluLnNvaHUuY29tfA; pprdig=Lk7HiV8rT2LS8uZh0riBcnZ8cokN-aN-Yv5OjbnX3qmZS4SYIg7PnnZqXWsxfPwNF1M-YxeT9PZQxGVw7qc6d15IjwIg_2E9537JOqzdHQL34_9ntlXJ_gYE7RCQ-Nt_piMGk9cvi5Ll9oRWWsdK2dUqWTbDnESGbkA07hWhO9E; sgid=06-34211517-AVtdd2sgghdVYlHDIz6Ug1U; ppmdig=1533384102000000c6517d180472f221cca4816ae5f92d73; JSESSIONID=aaaVHAXKqrFvbeiJfMHsw',
#     'Host': 'weixin.sogou.com',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
#     'X-Requested-With': 'XMLHttpRequest'
# }
headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection	': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'cookies': 'CXID=0DDCDF3AB524336D02F12EE46CD334E4; SUID=D4C85D7C3965860A5AA39D940000145A; '
               'IPLOC=CN2102; SUV=1531959792494460; '
               'sct=5; SNUID=8E67BCEBD1D5A2CE38998221D186284B; '
               'ld=wyllllllll2bFdo5lllllVH5TZGlllllnLLdflllllwlllll9Zlll5@@@@@@@@@@; '
               'LSTMV=347%2C155; LCLKINT=4472; ABTEST=0|1531961096|v1; weixinIndexVisited=1; '
               'JSESSIONID=aaa4Ta7_4rS8e9Jqz3Hsw; '
               'ppinf=5|1532852075|1534061675|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTclOUYlQjMlRTUlQ'
               'TQlQjR8Y3J0OjEwOjE1MzI4NTIwNzV8cmVmbmljazoxODolRTclOUYlQjMlRTUlQTQlQjR8dXNlcmlkOjQ0Om85dDJsdUI5VE8'
               '5TE1CemdVRDd5dC10RjI4MzBAd2VpeGluLnNvaHUuY29tfA; '
               'pprdig=Lk7HiV8rT2LS8uZh0riBcnZ8cokN-aN-Yv5OjbnX3qmZS4SYIg7PnnZqXWsxfPwNF1M-YxeT9PZQxGVw7qc6d15IjwIg'
               '_2E9537JOqzdHQL34_9ntlXJ_gYE7RCQ-Nt_piMGk9cvi5Ll9oRWWsdK2dUqWTbDnESGbkA07hWhO9E; '
               'sgid=06-34211517-AVtdd2sgghdVYlHDIz6Ug1U; ppmdig=153286085500000088c26503f3219f8b3403a4a6915fc676',
    'Host': 'weixin.sogou.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}

response = requests.get('http://weixin.sogou.com/weixin?query=RNG&type=2&page=11&ie=utf8', headers=headers)
print(response.text)
