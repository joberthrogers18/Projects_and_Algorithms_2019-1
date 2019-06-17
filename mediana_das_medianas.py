var = [2, 5, 9, 19, 24, 54, 5, 87, 9, 10, 44, 32,
       18, 13, 2, 4, 23, 26, 16, 19, 25, 39, 47, 56, 71, 20, 29, 33, 85, 111, 93,69,99, 53]

aux = []

teste_median = []


def def_gap():
   while (len(var) != 0):
      if len(var) > 5:
         teste_median.append(var[0:5])
         del var[0:5]
      else:
         teste_median.append(var[0:len(var)])
         del var[0:len(var)]

   for i in teste_median:
      i.sort()


def find_median():
   global aux
   global var

   aux = []

   print(teste_median)

   for i in teste_median:
      if len(i) % 2 == 0:
         aux.append(i[(len(i) // 2) - 1])
      elif len(i) % 2 != 0:
         aux.append(i[len(i) // 2])

   var = aux
   aux = []


if __name__ == "__main__":

   print(var)

   while(len(var) > 5):
      teste_median = []
      def_gap()
      find_median()

   teste_median = [var]
   find_median()
   print("-------------")
   print("the median of median is : %d" % (var[0]))
