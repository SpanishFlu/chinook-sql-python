PL1 = {"title" : "samir 2amis", 
       "artist" : "abyusif", 
       "genre" : "Rap", 
       "price" : 4.10}

PL2 = {"title" : "getting older", 
       "artist" : "bellie eilish", 
       "genre" : "Pop", 
       "price" : 2.51}

PL3 = {"title" : "u said", 
       "artist" : "Lil Peep", 
       "genre" : "Rap", 
       "price" : 0.56}

PL4 = {"title" : "she's gone", 
       "artist" : "steelheart", 
       "genre" : "Metal", 
       "price" : 14.71}

PL5 = {"title" : "hello", 
       "artist" : "rejjie snow", 
       "genre" : "pop", 
       "price" : 12.74}
Albums = [PL1, PL2, PL3, PL4, PL5]

def get_label(price):
    return "Premium" if price >= 18.61 else "Standard"

def display_catalog(albums):
     for x in albums:
          print(f"{x['title'].strip().title()} by {x['artist'].strip().title()} — ${x['price']:.2f}")

def search_catalog(albums, search):
    found = False

    for x in Albums:
        if search == x["title"].lower() or search == x["artist"].lower():
            found = True
            label = get_label(x["price"])
            print(f"{x['title'].title()} — ${x['price']:.2f} — {label}")

    if not found:
                print(f"Track or Artist not available")

display_catalog(Albums)

while True:
        search = input(f"Enter track name or artist name (q to quit)").lower().strip()
        if search == "q":
             break
        search_catalog(Albums, search)
