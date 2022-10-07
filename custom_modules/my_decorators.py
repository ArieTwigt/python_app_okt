# define the decorator
def inflation_adjusted(func):
    

    def wrapper(amount, rate, years):
        result = func(amount,  rate / 2, years)
        return result

    return wrapper


# decorator for showing the intermediate values
def print_interest(func):

    def wrapper(amount, rate, years):
        for year in range(years + 1):
            result = func(amount, rate, year)
            print(result)
        return result
    
    return wrapper


