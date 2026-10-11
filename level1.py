prices = [100,102,99,105,110]
cash = 1000
shares = 0
values = []

print(prices,cash,shares,values)

shares = cash//prices[0]
cash = cash - shares*prices[0]


for price in prices:
    value = cash + shares*price
    values.append(value)