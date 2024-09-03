# Utility Functions
def is_even(i):
	return i % 2 == 0
def is_top():
	if get_pos_y() == get_world_size() - 1:
		return True
def is_bottom():
	if get_pos_y() == 0:
		return True
	
# Main Loop Bare Bones
def main():
	# World Reset
	clear()
	# Global variables
	water_limit = 0.75

	while True:
		# Water check for all tiles
		if get_water() < water_limit:
			use_item(Items.Water_Tank)

        # Add crop plant functions here

		# Movement Loop
		if is_top():
			move(East)
		move(North)

# Plants sunflowers in second to last column
def is_sunflower_section():
	return get_pos_x() == get_world_size() - 2	
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

# Plants trees and grass in alternating chess board pattern
def trees_and_grass_section():
	if can_harvest():
		harvest()
	if is_even(get_pos_x()) and is_even(get_pos_y()):
		plant(Entities.Tree)
	elif not is_even(get_pos_x()) and not is_even(get_pos_y()):
		plant(Entities.Tree)

# Plants pumpkins in the bottom left 4 by 4 grid
def is_pumpkin_section():
	if get_pos_x() < 4 and get_pos_y() < 4:
		return True
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

# Plants carrots in the far right column
def is_carrot_section():
	return get_pos_x() == get_world_size() - 1		
def carrot_plant():
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Carrots:
		trade(Items.Carrot_Seed)
		plant(Entities.Carrots)
	if can_harvest():
		harvest()
		trade(Items.Carrot_Seed)
		plant(Entities.Carrots)
