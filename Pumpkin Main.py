def main():
	# World Reset
	clear()
	# Global variables
	water_limit = 0.75

	while True:
		# Water check for all tiles
		if get_water() < water_limit:
			use_item(Items.Water_Tank)

		# Sunflower Section
		if is_sunflower_column():
			sunflower_plant()

		# Pumpkin Section
		else:
			pumpkin_plant()

		# Movement Loop
		if is_top():
			move(East)
		move(North)

# Plants sunflowers in first column
def is_sunflower_column():
	if get_pos_x() == 0:
		return True
def sunflower_plant():
	if get_ground_type() != Grounds.Soil:
		while get_ground_type() != Grounds.Soil:
			till()
			move(North)

	if get_entity_type() != Entities.Sunflower:
		while get_entity_type() != Entities.Sunflower:
			trade(Items.Sunflower_Seed)
			plant(Entities.Sunflower)

	if can_harvest() == True and get_entity_type() == Entities.Sunflower:
		row_count = get_world_size()
		while row_count > 0:	
			sunflower_petal_list = []
			sunflower_y_location = []	
			for i in range(get_world_size()):
				if get_entity_type() == Entities.Sunflower:
					sunflower_petal_list.append(measure())
					sunflower_y_location.append(i)
				move(North)

			max_petal = 0
			max_petal_location = 0
			index = 0
			for n in range(len(sunflower_petal_list)):
				if sunflower_petal_list[n] > max_petal:
					max_petal = sunflower_petal_list[n]
					max_petal_location = sunflower_y_location[n]
					index = n

			while get_pos_y() != max_petal_location:
				move(North)

			harvest()
			sunflower_petal_list.pop(index)
			row_count -= 1	

			while not is_bottom():
				move(South)
	
		if get_entity_type() != Entities.Sunflower:
			trade(Items.Sunflower_Seed)
			plant(Entities.Sunflower)	

# Plants pumpkins in any column
def pumpkin_plant():
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Pumpkin:
		trade(Items.Pumpkin_Seed)
		plant(Entities.Pumpkin)
	if can_harvest():
		harvest()
		trade(Items.Pumpkin_Seed)
		plant(Entities.Pumpkin)

# Utility Functions
def is_even(i):
	return i % 2 == 0
def is_top():
	if get_pos_y() == get_world_size() - 1:
		return True
def is_bottom():
	if get_pos_y() == 0:
		return True
	
main()