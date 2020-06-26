def odd_values_string(str):
  result = " "
  for i in range(len(str)):
    if i % 2 == 0:
     result = result + str[i]
  return result
print(odd_values_string("kishore"))
print(odd_values_string("charan"))