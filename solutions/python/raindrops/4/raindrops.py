def convert(number: int) -> str:
    rain = {3 : "Pling", 5 : "Plang", 7 : "Plong"}
    result = [rain[factor] for factor in rain.keys() if number % factor == 0]
    return str(number) if "".join(result) == "" else "".join(result)
    