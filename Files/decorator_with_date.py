from datetime import date
today_date = date.today()
independence_day = date(2024, 8, 15)
def deco(price):
    if (today_date==independence_day):
        print("Today best price of samsung mobile is : 9,000 /- only")
    else:
        price()
def price():
    if (today_date != independence_day):
        print("Today best price of samsung mobile is : 10,000 /- only")

deco(price)
