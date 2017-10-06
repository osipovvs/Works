def get_days_to_new_year():
    from datetime import date

    today = date.today()
    new_year = date(today.year + 1, 1, 1)

    return (new_year - today).days
