dictionar={"cheia1":1, "cheia2":2, 3:"valoare3", "cheia2":2}
#print(type(dictionar))
#print(dictionar.keys())
#print(dictionar["cheia1"])
#print(dictionar.get('cheie11', "nu exista valoare"))
dictionar.update({"cheia11":"valoare", "cheia12":12})
#dictionar.popitem()
dictionar['cheia11']="alfabet"
print(dictionar)

