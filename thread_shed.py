#!/bin/python3

def calculate_sales(daily_sales):

    daily_sales = daily_sales.replace(';','').split('\n')

    sales = {}

    for sale in daily_sales:

        if sale:

            parts = sale.split(',')

            name = parts[0].strip()

            price = float(parts[1].strip().replace('$',''))

            color = parts[2].strip()

            date = parts[3].strip()

            if name in sales:

                sales[name] += price

            else:

                sales[name] = price

    return sum(sales.values())


done
