# 1. TAREA: imprime "Hola, mundo"
name = "Hola, mundo"
print(name.title())

# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Luisa!"
print("Hola,", name)	# con una coma
print("Hola," + name)	# con un +

# 3. imprimir "Hola 42!" con el número en una variable
name = 13
print("¡Hola", name, "!")	# con una coma
print("¡Hola" + name + "!" )	  # con una +	-- este debería arrojar un error! (porque el numero no fue convertido a cadena)
print("¡Hola" + str(name) + "!" )

# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
food_fav_1 = "sushi"
food_fav_2 = "pizza"
print(f"Amo comer {food_fav_1} y {food_fav_2}")
print("Amo comer {} y {}" .format(food_fav_1, food_fav_2))