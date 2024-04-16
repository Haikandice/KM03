#b = {
    #"car" : "Toyota",
    #"model" :"camry",
    #"imeges" : ['https://cam50-imege','https://cam75-imege'],
    #"price" : 25000000,
    #"is_published" : True
    #}

#a = {
    #"car" : "Toyota",
    #"model" :"camry",
    #"imege" : ['https://cam50-imege'],
    #}
#distionary = словарь dict




c = { "name" : "Erbol","surname":"Askarov"}
#d = c["name"]
#d = c.get("name")
#d = None
c["midlle_name"] = 'Miras'
print(c)


#a = {
    #"car" : "tayota",
    #"model":"camry",
   # "image": ["https://ai2.appinventor.mit.edu/?locale=ru#5974014489067520","https://some-lm"],
   # "price" : 25000000,
    #"is_published" : True
    #}


h= {"name":"Askar", "last_name":"Erlanov"}
for k,v in h.items():
    print("key", k)
    print("value", v)

list_1 = [
    {
        "name" :"Kanat",
        "last_name":"Erbolov",
        "age": 20
    },
    {
        "name": "Miras",
        "last_name": "Miko",
        "age": 15
    },
    {
        "name": "Agibay",
        "last_name": "Zhandosov",
        "age": 45
    }
]
total=0
for n in list_1:
    total += n["age"]

count=len(list_1)
c = total/count
print(c)
