try:
  ans = 5 / 2
except ZeroDivisionError:
  print("Nolga bo'lish mumkin emas.")
else:
   print(f"Hech qanday xatolik vujudga kelmadi. Natija :", ans)
finally:
   print('Dastur yakunlandi.')
