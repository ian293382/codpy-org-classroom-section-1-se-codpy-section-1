def fizzBuzz(n: int) -> str:
    if n%15==0:
        return "Fizz" + "Buzz"
    elif n%3==0:
        return "Fizz"
    elif n%5==0:
        return "Buzz"
    else:
        return f"{str(n)}"
 
