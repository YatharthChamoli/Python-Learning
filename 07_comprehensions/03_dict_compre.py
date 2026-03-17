tea_prices_inr = {
  "Masala Chai": 20,
  "Green Tea": 15,
  "Lemon Tea": 18,
}

tea_prices_USD = {tea:price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_USD)