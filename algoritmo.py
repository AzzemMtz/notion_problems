from decimal import Decimal
from math import ceil

class Algoritmo:

    @staticmethod
    def valid_parentheses(parens:str):
        """Write a function that takes a string of parentheses, 
        and determines if the order of the parentheses is valid"""
        open_parens = parens.count("(")
        close_parens = parens.count(")")
        return parens.startswith("(") and parens.endswith(")") and open_parens == close_parens

    @staticmethod
    def format_duration(seconds:int):
        """The function must accept a non-negative integer. 
            If it is zero, it just returns "now". 
            Otherwise, the duration is expressed as a combination of 
            years, days, hours, minutes and seconds."""
        if (seconds < 0): return None
        if (seconds == 0): return "now"
        min,sec = divmod(seconds,60)
        hrs,min = divmod(min,60)
        day,hrs = divmod(hrs,24)
        year,day = divmod(day,365)
        lst_str = [duration for duration in [
            f"{year} years" if year > 1 else f"{year} year" if year == 1 else "",
            f"{day} days" if day > 1 else f"{day} day" if day == 1 else "",
            f"{hrs} hours" if hrs > 1 else f"{hrs} hour" if hrs == 1 else "",
            f"{min} minutes" if min >1 else f"{min} minute" if min == 1 else "",
            f"{sec} seconds" if sec > 1 else f"{sec} second" if sec == 1 else ""
        ] if duration]
        return f"{', '.join(lst_str[:-1])}" + f" and {lst_str[-1]}" if len(lst_str) > 1 else f"{lst_str[-1]}" 

    @staticmethod
    def movie(card:int, ticket:Decimal, perc:Decimal):
        A = lambda n: ticket * n
        B = lambda n: card + ticket * perc * (perc ** n - 1)/(perc - 1)
        a, b = 0, card
        n = 1
        while a < ceil(b):
            a,b = A(n),B(n)
            n += 1
        return n - 1


