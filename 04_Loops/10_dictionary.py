users = [
  {"id": 1,"total": 250, "coupon": "DISCOUNT10"},
  {"id": 2,"total": 300, "coupon": "DISCOUNT20"},
  {"id": 3,"total": 100, "coupon": "DISCOUNT30"}
]

discounts = {
  "DISCOUNT10": (0.2, 0),
  "DISCOUNT20": (0.5, 0),
  "DISCOUNT30": (0, 10)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid ₹{user["total"]} and got a discount of ₹{discount}")