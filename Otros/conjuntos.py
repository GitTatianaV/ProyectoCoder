
#mi_conj = {"rojo", "blanco", "azul"}
#mi_conj.add("violeta")
#mi_conj.update(["dorado"])
#print(mi_conj)
#mi_conj.remove("dorado")
#print(mi_conj)

my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.intersection(my_set_2)
print(my_new_set)


my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.difference(my_set_2)
print(my_new_set)
