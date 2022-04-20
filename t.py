from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
PLACE_CITY = 'Lviv'
API_Key = '0650a47706298e4b51b5091d448e4bcf'
owm = OWM(API_Key)

manege = owm.weather_manager()
data = manege.weather_at_place(PLACE_CITY)

weather = data.weather

print(weather.temperature('celsius')