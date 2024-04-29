from execl import get_bk_source_data
from request import get_bks_klines, gte_bks_stock_list, get_stocks_list
from strategy import filt_condition


def working():
    filt_list = []
    bk_source = get_bk_source_data()
    print(bk_source)
    id = bk_source[0]["id"]
    bk_list = get_bks_klines(id, "101")
    print(bk_list)
    bks_stock_list = gte_bks_stock_list(id)
    print(bks_stock_list)
    stock_id = bks_stock_list[0]["f12"]
    stock_list = get_stocks_list(stock_id, "101")
    print(stock_list)
    res = filt_condition(bk_list)



if __name__ == '__main__':
    working()

