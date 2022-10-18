
class CurencyConverter:


    @staticmethod
    def currency_converter(dollars: float, dollar_price: float) -> float:
        IOF = 0.06  # 6%
        return (dollars * dollar_price) + ((dollars * dollar_price) * IOF)
