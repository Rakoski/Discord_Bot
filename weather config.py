
from pyowm.owm import OWM
owm = OWM('015f8141edc79dda4164c30a8929fcc6')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Paranavaí,BR')  # the observation object is a box containing a weather object
weather = observation.weather    # short version of status (eg. 'Rain')
 # detailed version of status (eg. 'light rain')
print(f"{weather.status}, {weather.detailed_status}")
temp_dict_celsius = weather.temperature('celsius')
print(f"{temp_dict_celsius['temp']}°C")
