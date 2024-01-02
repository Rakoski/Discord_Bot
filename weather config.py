
from pyowm.owm import OWM
owm = OWM('015f8141edc79dda4164c30a8929fcc6')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('London ,UK')
weather = observation.weather of status 
print(f"{weather.status}, {weather.detailed_status}")
temp_dict_celsius = weather.temperature('celsius')
print(f"{temp_dict_celsius['temp']}°C")
