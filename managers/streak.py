from datetime import datetime, timedelta
from history import get_history_dates,get_day_progress

def get_successful_dates():
    successful_dates = []

    dates = get_history_dates()

    for row in dates:
        date = row[0]

        completed,total,percentage = get_day_progress(date)

        if completed == total and total > 0:
            successful_dates.append(date)

    return successful_dates

def get_current_streak():
    successful_dates = get_successful_dates()

    if not successful_dates:
        return 0

    successful_dates = [datetime.strptime(date, "%Y-%m-%d").date()
                        for date in successful_dates]

    successful_dates.sort(reverse=True)

    today = datetime.now().date()

    most_recent = successful_dates[0]

    if most_recent < today - timedelta(days =1):
        return 0

    streak = 1

    current_date = most_recent

    for date in successful_dates[1:]:
        expected_date = current_date - timedelta(days=1)

        if date == expected_date:
            streak +=1
            current_date = date

        else:
            break

    return streak

def get_longest_streak():
    successful_dates = get_successful_dates()

    if not successful_dates:
        return 0

    successful_dates = [datetime.strptime(date, "%Y-%m-%d").date()
                        for date in successful_dates]

    successful_dates.sort()
    longest = 1
    current =1

    for i in range(1,len(successful_dates)):
        previous_date = successful_dates[i-1]
        current_date = successful_dates[i]

        if current_date == previous_date + timedelta(days=1):
            current +=1

        else:
            current =1

        if current > longest:
            longest = current

    return longest


if __name__ == "__main__":
    print("Successful dates: ", get_successful_dates())

    print("Current streak: ", get_current_streak())

    print("Longetst streak: ", get_longest_streak())

