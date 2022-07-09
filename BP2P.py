import requests
import json
import codecs
import pandas as pd

url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"

headers = {
    'authority': 'p2p.binance.com',
    'x-trace-id': '72987171-8d38-4c42-88db-b36ddf3d1cfb',
    'c2ctype': 'c2c_merchant',
    'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
    'x-ui-request-trace': '72987171-8d38-4c42-88db-b36ddf3d1cfb',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.110 Safari/537.36',
    'content-type': 'application/json',
    'lang': 'en',
    'fvideo-id': '327a2b7e6415a2e9b075e4a8204293b93f7cc58f',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6Ijg2NCwxNTM2IiwiYXZhaWxhYmxlX3NjcmVlbl9yZXNvbHV0aW9uIjoiODI0LDE1MzYiLCJzeXN0ZW1fdmVyc2lvbiI6IldpbmRvd3MgMTAiLCJicmFuZF9tb2RlbCI6InVua25vd24iLCJzeXN0ZW1fbGFuZyI6ImVuLVVTIiwidGltZXpvbmUiOiJHTVQrMSIsInRpbWV6b25lT2Zmc2V0IjotNjAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTYuMC40NjY0LjExMCBTYWZhcmkvNTM3LjM2IiwibGlzdF9wbHVnaW4iOiJQREYgVmlld2VyLENocm9tZSBQREYgVmlld2VyLENocm9taXVtIFBERiBWaWV3ZXIsTWljcm9zb2Z0IEVkZ2UgUERGIFZpZXdlcixXZWJLaXQgYnVpbHQtaW4gUERGIiwiY2FudmFzX2NvZGUiOiI1ZjhkZDMyNCIsIndlYmdsX3ZlbmRvciI6Ikdvb2dsZSBJbmMuIChJbnRlbCkiLCJ3ZWJnbF9yZW5kZXJlciI6IkFOR0xFIChJbnRlbCwgSW50ZWwoUikgSEQgR3JhcGhpY3MgNTIwIERpcmVjdDNEMTEgdnNfNV8wIHBzXzVfMCwgRDNEMTEtMjcuMjAuMTAwLjg2ODEpIiwiYXVkaW8iOiIxMjQuMDQzNDc1Mjc1MTYwNzQiLCJwbGF0Zm9ybSI6IldpbjMyIiwid2ViX3RpbWV6b25lIjoiRXVyb3BlL1BhcmlzIiwiZGV2aWNlX25hbWUiOiJDaHJvbWUgVjk2LjAuNDY2NC4xMTAgKFdpbmRvd3MpIiwiZmluZ2VycHJpbnQiOiI1ODc0ZmE4Yzg0NjlkMmNmYWE1ODAyMjdmNWIyNGEzNCIsImRldmljZV9pZCI6IiIsInJlbGF0ZWRfZGV2aWNlX2lkcyI6IiJ9',
    'bnc-uuid': '61c41176-5a32-4d4d-a3ee-b081d9d90b3f',
    'clienttype': 'web',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'origin': 'https://p2p.binance.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://p2p.binance.com/en/trade/sell/USDT?fiat=RUB&payment=ALL',
    'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7',
    'cookie': 'cid=Md7yVAAt; bnc-uuid=61c41176-5a32-4d4d-a3ee-b081d9d90b3f; source=organic; campaign=www.google.com; '
              'userPreferredCurrency=USD_USD; fiat-prefer-currency=EUR; showBlockMarket=false; '
              'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217de785cc7bd6-0031a8f0858e91-4303066-1327104'
              '-17de785cc7c7b2%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A'
              '%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5'
              '%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22'
              '%24device_id%22%3A%2217de785cc7bd6-0031a8f0858e91-4303066-1327104-17de785cc7c7b2%22%7D; sys_mob=no; '
              'common_fiat=RUB; BNC_FV_KEY=327a2b7e6415a2e9b075e4a8204293b93f7cc58f; BNC_FV_KEY_EXPIRE=1641650026647; '
              'videoViewed=yes '
}

def get_data(page, rows, asset, fiat, tradeType):
    payload = json.dumps({
        "page": page,
        "rows": rows,
        "payTypes": [],
        "asset": asset,
        "tradeType": tradeType,
        "fiat": fiat,
        "publisherType": None
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(codecs.decode(response.text.encode(), 'utf-8-sig'))
    df = pd.json_normalize(data['data'])
    df1 = df[
        ['advertiser.nickName', 'adv.price', 'adv.maxSingleTransAmount',
         'adv.minSingleTransAmount', 'adv.surplusAmount']]
    return df1
