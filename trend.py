#show the top 5 days when changes in a trend happen
import csv
csv_file='/home/poppie/Documents/my-todo/GBPJPY=X.csv'

def analyze_csv(csv_file):
    data = []

    # Read the CSV file and store the data in a list
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row

        for row in csv_reader:
            try:
                date = row[0]
                open_value = float(row[1])
                close_value = float(row[2])
                high_value = float(row[3])
                low_value = float(row[4])

                data.append({
                    'date': date,
                    'open': open_value,
                    'close': close_value,
                    'high': high_value,
                    'low': low_value
                })
            except ValueError:
                print(f"Skipping invalid data in row: {row}")

    # Find the top 5 dates with major trend changes
    trend_changes = []
    window_size = 15 * 252  # 15 years assuming 252 trading days per year

    for i in range(window_size, len(data)):
        current = data[i]
        previous = data[i - window_size]

        if (current['close'] > previous['close'] and
            all(data[j]['close'] < current['close'] for j in range(i - window_size + 1, i))) or \
           (current['close'] < previous['close'] and
            all(data[j]['close'] > current['close'] for j in range(i - window_size + 1, i))):
            trend_changes.append(i)

    top_5_dates = sorted(trend_changes, key=lambda x: data[x]['close'], reverse=True)[:5]
    top_dates = [data[i]['date'] for i in top_5_dates]

    return top_dates

# Usage example
csv_file = '/home/poppie/Documents/my-todo/GBPJPY=X.csv'
top_dates = analyze_csv(csv_file)

print("Top 5 Dates with Major Trend Changes:")
for date in top_dates:
    print(date)
