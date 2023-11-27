zbozi = [
    {
        "name" : "IPHONE 14",
        "price" : 22169.0,
        "cathegory" : (12, "Mobilní telefony")
    },
    {
        "name" : "Fujifilm XT30",
        "price" : 22269.0,
        "cathegory" : (2, "Fotoaparáty")
    },
    {
        "name" : "Niceboy HIVE Pins Black",
        "price" : 999.0,
        "cathegory" : (4, "Sluchátka")
    }
]

print(sorted(zbozi, key=lambda p: p["price"]))
print(sorted(zbozi, key=lambda n: n["name"], reverse=True))
print(sorted(zbozi, key=lambda c: c["cathegory"]))
