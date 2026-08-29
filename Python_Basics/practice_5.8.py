def sum_of_digits(n):
        if n<10:
            return n
        last_digit=n%10
        remaining=n//10

        return last_digit+sum_of_digits(remaining)
print(sum_of_digits(123))
   


