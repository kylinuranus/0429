def filt_condition(klines: list):
    if len(klines) < 3:
        return False

    data_0 = klines[0]  # 当前k
    data_1 = klines[1]  # 上一根k
    data_2 = klines[2]  # 上上一根k

    if float(data_1["close"]) > float(data_1["open"]):  # 收阳线
        if float(data_1["close"]) > float(data_2["open"]):  # 吞没形态
            return True
    return False


def filt_condition2(klines: list):
    if len(klines) < 3:
        return False

    data_1 = klines[1]  # 上一根k
    data_2 = klines[2]  # 上上一根k

    if float(data_1["close"]) > float(data_1["open"]) and float(data_1["close"]) > float(data_2["open"]) and float(
            data_1["close"]) > float(data_2["close"]):  # 收阳线
        return True
    return False


def match_price(week_data, day_data):
    day_close = float(day_data["close"])
    day_low = float(day_data["low"])
    week_open = float(week_data["open"])
    if day_close >= week_open:
        if (day_close - week_open) <= (week_open / 100):
            return True
        if (day_low - week_open) <= (week_open / 100):
            return True
    return False


def match_price2(week_data, day_data):
    day_close = float(day_data["close"])
    day_low = float(day_data["low"])
    week_open = float(week_data["open"])
    if day_close >= week_open:
        if (day_close - week_open) <= (week_open / 100):
            return True
    return False


def match_price3(week_data, day_data):
    day_close = float(day_data["close"])
    day_low = float(day_data["low"])
    week_open = float(week_data["open"])
    if day_low >= week_open:
        if (day_low - week_open) <= (week_open / 200):
            return True
    return False
