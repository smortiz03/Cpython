countries=[
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": [
            "Swedish"
        ],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    },
    {
        "name": "Albania",
        "capital": "Tirana",
        "languages": [
            "Albanian"
        ],
        "population": 2886026,
        "flag": "https://restcountries.eu/data/alb.svg",
        "currency": "Albanian lek"
    }
    
]

'''

#¿Cuál es el número total de idiomas en los datos?
suma=0
print(type(countries))
#print(len(countries))
for c in countries:
    for key,value in c.items():
        if key=='languages':
            suma=(len(value))+suma
            #print(type(len(value)))
print("total de idiomas",suma)        
  '''  
#Encuentre los diez idiomas más hablados a partir de los datos
#Encuentra los 10 países más poblados del mundo.
