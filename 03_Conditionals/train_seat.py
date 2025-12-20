# You're building a ticket info system for a railway app.
# Based on seat type, show its features.
# Task:
# • Input: "sleeper", "AC", "general", "luxury"
# • Match using match-case
# • Unknown → show: "Invalid seat type"

seat_type = input("Enter seat type (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper: Non-AC, sleeping beds available.")
    case "AC":
        print("AC: Air-conditioned, comfortable seating.")
    case "general":
        print("General: Basic seating, no air conditioning.")
    case "luxury":
        print("Luxury: Premium seating with extra amenities.")
    case _:
        print("Invalid seat type.")