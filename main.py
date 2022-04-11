income = int(input())
if income <= 15527:
  calculated_tax = 0
  print('{0} {income} {1} {calculated_tax} {2}'.format('The tax for', 'is 0%. That is', 'dollars!', income = income, calculated_tax = calculated_tax))
elif 15528 <= income <= 42707:
  calculated_tax = income * 15 // 100
  print('{0} {income} {1} {calculated_tax} {2}'.format('The tax for', 'is 15%. That is', 'dollars!', income = income, calculated_tax = calculated_tax))
elif 42708 < income < 132406:
  calculated_tax = income * 25 // 100
  print('{0} {income} {1} {calculated_tax} {2}'.format('The tax for', 'is 25%. That is', 'dollars!', income = income, calculated_tax = calculated_tax))
elif 132407 < income:
  calculated_tax = income * 28 // 100
  print('{0} {income} {1} {calculated_tax} {2}'.format('The tax for', 'is 28%. That is', 'dollars!', income = income, calculated_tax = calculated_tax))
