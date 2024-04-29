import json
import re
import requests


# cycle  日101 周102 月103
def get_bks_klines(id, cycle):
    params = {
        "secid": "90." + id,
        "fields1": "f1,f2,f3,f4,f5",
        "fields2":
            "f51,f52,f53,f54,f55,f59",  # 分别对应time，open,close,high,low,涨幅
        "lmt": "5",  # 条数
        "klt": cycle,
        "fqt": "1",
        "end": "30000101",
        "ut": "fa5fd1943c7b386f172d6893dbfba10b",
    }

    url = "http://12.push2his.eastmoney.com/api/qt/stock/kline/get"
    data = request(url, params=params)
    list_data = data["data"]["klines"]
    arr = get_klines_arr(list_data, 0, 1, 2, 3, 4, 5)
    arr.reverse()
    return arr


# 根据板块id获取板块的股票
def gte_bks_stock_list(id):
    params = {
        "pn": 1,
        "pz": 100,
        "np": 1,
        "fs": "b:" + id + "+f:!50",
        "fields": "f12,f14",
    }
    url = "http://93.push2.eastmoney.com/api/qt/clist/get"
    data = request(url, params=params)
    bk_stock_list = data["data"]["diff"]
    return bk_stock_list


# 格局id获取股票k
# klt  日101 周102 月103
def get_stocks_list(id: str, cycle):
    secid = "0."
    if id.startswith("0"):
        secid = "0."
    elif id.startswith("6") and id.startswith("688") == False:
        secid = "1."
    else:
        return []

    params = {
        "secid": secid + id,
        "fields1": "f1,f2,f3,f4,f5",
        "fields2":
            "f51,f52,f53,f54,f55,f59",  # 分别对应time，open,close,high,low,涨幅
        "lmt": "5",  # 条数,默认取5条
        "klt": cycle,
        "fqt": "1",
        "end": "30000101",
        "ut": "fa5fd1943c7b386f172d6893dbfba10b",
    }

    url = "https://push2his.eastmoney.com/api/qt/stock/kline/get"
    data = request(url, params=params)
    list_data = data["data"]["klines"]
    arr = get_klines_arr(list_data, 0, 1, 2, 3, 4, 5)
    arr.reverse()
    return arr


def get_klines_arr(klines: list, date: int, open: int, close: int, high: int,
                   low: int, change: int):
    arr = []
    for s in klines:
        l = s.split(",")
        m = {
            "date": l[date],
            "high": l[high],
            "open": l[open],
            "low": l[low],
            "close": l[close],
            "rate": l[change],
        }
        arr.append(m)
    return arr


def loads_jsonp(_jsonp):
    try:
        return json.loads(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
    except:
        raise ValueError('Invalid Input')


def request(url, params=None):
    r = requests.get(url, params=params)
    r.close()
    json1 = loads_jsonp(r.text)
    json_str = json.dumps(json1)
    data = json.loads(json_str)
    return data
