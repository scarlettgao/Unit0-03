# Created by: Scarlett Gao
# Created on: 14-Sep-2017
# Created for: ICS3U
# Daily assignment - Unit0-03
# This program displays Hello World program, but in GUI

import ui

def hello_world_touch_up_inside(sender):
	  #print('Hello,World!')
	  view['hello_world_label'].Text=("Hello,World!")
	  
view = ui.load_view()
view.present('sheet')
