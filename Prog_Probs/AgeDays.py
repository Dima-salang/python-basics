def calculate_days(days_alive):
    years = 0
    months = 0
    days = 0
    while days_alive != 0:
        if days_alive % 365 == 0:
            years += 1
            days_alive -= 365
        elif days_alive % 30 == 0:
            months += 1
            days_alive -= 30
        else:
            days += 1
            days_alive -= 1

    return f"You have been alive for {years} years, {months} months, and {days} days"


print(calculate_days(100000))

