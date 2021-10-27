
from phonenumbers import geocoder
import os 
import phonenumbers
from phonenumbers import carrier
os.system('cls')

country_name=phonenumbers.parse("+918207214727","CH")
c=geocoder.description_for_number(country_name,"en")
print(c)


surviceprovider=phonenumbers.parse("+918207214727")
print(carrier.name_for_number(surviceprovider,"en"))
