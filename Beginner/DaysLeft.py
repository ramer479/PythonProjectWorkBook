

if __name__ == "__main__":
    age = int(input("Current age: "))
    max_age = 75
    rest_age_yr = max_age-age
    rest_age_mnth = rest_age_yr * 12
    rest_age_week = rest_age_yr * 52
    rest_age_day = rest_age_yr * 365
    message = f"You have {rest_age_mnth} months, {rest_age_week} weeks and {rest_age_day} days to live"
    print(message)