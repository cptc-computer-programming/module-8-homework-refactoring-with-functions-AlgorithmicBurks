
# -----------------------------
# Global Constants
# -----------------------------
DAYS_IN_WEEK = 7

# Days in each month (no leap year handling)
FEB_DAYS = 28
LONG_MONTH_DAYS = 31  # Jan, Mar, May, Jul, Aug, Oct, Dec
SHORT_MONTH_DAYS = 30 # Apr, Jun, Sep, Nov


def find_date_one_week_later(month, date):
    """Return the month and day one week after the given date."""
    date += DAYS_IN_WEEK

    # February (28 days)
    if month == 2 and date > FEB_DAYS:
        month += 1
        date -= FEB_DAYS

    # Months with 31 days
    elif (month == 1 or month == 3 or month == 5 or
          month == 7 or month == 8 or month == 10 or
          month == 12) and date > LONG_MONTH_DAYS:
        month += 1
        date -= LONG_MONTH_DAYS

    # Months with 30 days
    elif date > SHORT_MONTH_DAYS:
        month += 1
        date -= SHORT_MONTH_DAYS

    # Wrap around past December
    if month > 12:
        month %= 12

    return month, date


def main():
    user_month = int(input("Enter the month (1-12): "))
    user_day = int(input("Enter the day (1-31): "))

    later_month, later_day = find_date_one_week_later(user_month, user_day)

    print(
        "A week after "
        + str(user_month)
        + "/"
        + str(user_day)
        + " is "
        + str(later_month)
        + "/"
        + str(later_day)
    )


if __name__ == "__main__":
    main()
