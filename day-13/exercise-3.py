data = ("Tom Hardy", "English", 42)

def process_data(name, nationality, age):
    return {"name": name, "nationality": nationality, "age": age}


print(process_data(*data))
