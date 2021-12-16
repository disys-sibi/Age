data = [{"id":1000,"Name":"John Smith","DOB":"01/01/2000","Gender":"Male","Age":20,"Zip code":12345,"Amount":"1500.20"},
        {"id":2000,"Name":"Jim McDonald","DOB":"02/02/2020","Gender":"Male","Age":25,"Zip code":67890,"Amount":"1500.20"},
        {"id":20,"Name":"Jim McDonald","DOB":"01/01/1999","Gender":"Male","Age":25,"Zip code":13579,"Amount":"1500.20"}]

for i in data:
    if (i["Name"]=="John Smith"):
        print("John Smith is present")
    if (i["Zip code"]==12345):
        print("Zip code right")
    if (i["Age"]==20):
        print("Age accepted")
