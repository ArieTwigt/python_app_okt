from custom_modules.calculation_functions import calc_interest, calc_interest_inflation


if __name__ == '__main__':
    my_result_2 = calc_interest_inflation(100, 0.05, 5)
    print("="*10)
    print(my_result_2)
    pass