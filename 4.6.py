user_type = input('please enter a 4-digit year: ')                              # str, 1926

file = open('FF_data.txt')                                                      # 'file' object

mktrf_list = []                                                                 # empty list

if not user_type.isdigit() or len(user_type) != 4:                              # bool, True
    print('sorry, must be 4 digits')
    exit()
for items in file:                                                              # str, "19260701    0.09    0.22    0.30   0.009\n"
    items = items.strip()                                                       # str, "19260701    0.09    0.22    0.30   0.009"
    split_items = items.split()                                                 # str, ["19260701", "0.09", "0.22", "0.30", "0.009"]
    years = split_items[0]                                                      # str, 19260701
    year_cut = years[0:4]                                                       # str, 1926
    mkt_rf = float(split_items[1])                                              # float, 0.09
    if year_cut == user_type:                                                   # bool, True
        mktrf_list.append(mkt_rf)                                               # list, [0.97, 0.3, 0.0, 0.72]

if len(mktrf_list) == 0:                                                        # bool, False
    print(f"No values found for year {user_type}")
    exit()

avr_mktrf_list = float(sum(mktrf_list) / len(mktrf_list))                       # float, 0.4975
avr = round(avr_mktrf_list, 2)                                                  # float, 0.5

value = len(mktrf_list)                                                         # int, 4

max = max(mktrf_list)                                                           # int, 0.97
min = min(mktrf_list)                                                           # min, 0.0
print(f"{user_type} (Mkt-RF): {value} values, max {max}, min {min}, avg {avr}")
exit()
