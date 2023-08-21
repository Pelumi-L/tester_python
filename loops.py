# prime = []
# for num in range(1, 21):
#     if num > 1:
#       print(num)
#       for i in range(2, num):
#          if (num % i) == 0:
#             print(f"this is {num}")
#             break
#         #  else:
#         #     print(f"this is the result {num}")
#       else:
#          prime.append(num)
#          print(prime)
#assignment use class & function to get the same result 

class Prime:
   def __init__(self):
      self.prime_numbers = []

   def prime(self, num):
      if num > 1:
         for i in range(2, num):
            if (num % i) == 0:
               return False
         return True
      return False
   
   def get_primes(self, start, end):
      for num in range(start, end + 1):
         if self.prime(num):
            self.prime_numbers.append(num)
      return self.prime_numbers
prime_collate = Prime()
primes = prime_collate.get_primes(1, 20)
print(primes)
      