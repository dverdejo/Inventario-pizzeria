toppings = ['muzzarella', 'napolitana', 'jamon', 'fugazzeta', 'roquefort', 'anchoas', 'calabresa']

precio = [500, 550, 650, 550, 550, 790, 650]

num_pizzas = len(toppings)

print("¡Bienvenid@!. Contamos con una variedad de " + str(num_pizzas) + " gustos de pizza.")

pizzas = list(zip(precio, toppings))
pizzas.sort()

print(pizzas)

print("Las pizzas más baratas son: " + str(pizzas[:4]))
print("Las pizzas más caras son: " + str(pizzas[4:]))
print("Las pizzas más baratas son: " + str(pizzas[0]))
print("Las pizzas más baratas son: " + str(pizzas[-1]))

gustos = precio.count(550)

print("Por el precio de $550 tiene para elegir una variedad de ", gustos, " gustos.")
