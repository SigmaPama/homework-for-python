from smartphone import Smartphone

catalog = [
Smartphone("samsung", "GalaxyA", "+795465445"),
Smartphone("Iphone", "16", "+79537753573"),
Smartphone("Iphone", "Xs", "+79213231213"),
Smartphone("Xiomy", "trollo", "+7951951519"),
Smartphone("Pocco", "chikenmacnuggets", "+79170971919")
]

for smartphone in catalog:
    print(f"{smartphone.type} - {smartphone.model}. {smartphone.number}")