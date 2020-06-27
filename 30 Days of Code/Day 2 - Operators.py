if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())

    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    print(str(round(meal_cost + tip + tax)))
