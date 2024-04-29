

def filt_condition(klines: list):
    if len(klines) < 3:
        return False

    data_0 = klines[0]  # 当前k
    data_1 = klines[1]  # 上一根k
    data_2 = klines[2]  # 上上一根k

    if float(data_1["rate"]) < 0.0 and float(data_0["rate"]) > 0.0:
        if float(data_1["close"]) > float(data_1["open"]):  # 收阳线
            if float(data_1["close"]) > float(data_2["open"]):   # 吞没形态
                return True
    return False


