import pygal

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America and Africa'
wm.add('North America', {'ca': 31200922, 'us': 29837298, 'mx': 20123212112})
wm.add('W. Africa', {'gh': 300000, 'na': 20932323})
wm.render_to_file('na_populations.svg')