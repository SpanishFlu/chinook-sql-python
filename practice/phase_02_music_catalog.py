PL1 = {"title" : "samir 2amis", "artist" : "abyusif", "genre" : "Rap", "price" : 4.10}
PL2 = {"title" : "getting older", "artist" : "bellie eilish", "genre" : "Pop", "price" : 2.51}
PL3 = {"title" : "u said", "artist" : "Lil Peep", "genre" : "Rap", "price" : 0.56}
PL4 = {"title" : "she's gone", "artist" : "steelheart", "genre" : "Metal", "price" : 14.71}
PL5 = {"title" : "hello", "artist" : "rejjie snow", "genre" : "pop", "price" : 12.74}
Albums = [PL1, PL2, PL3, PL4, PL5]
is_searching = True
for x in Albums:
    print(f"{x['title'].strip().title()} by {x['artist'].strip().title()} — ${x['price']:.2f}")

while is_searching:
    search = input(f"Enter track name or artist name (q to quit)").lower()
    if search == "q":
        break
    found = False
    for x in Albums:
        if search == x["title"].lower() or search == x["artist"].lower():
            found = True
            label = "Premium" if x["price"] >= 18.61 else "Standard"
            print(f"{x['title'].title()} — ${x['price']:.2f} — {label}")

    if not found:
                print(f"Track or Artist not available")
        
    