import ephem

planet_user_name=str(input("Введите название планиты: "))

def planets(planet_name):
	print(ephem.constellation(planet_name))


planets(planet_user_name)