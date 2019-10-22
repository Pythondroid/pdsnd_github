import datetime as dt
import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}


def get_filters():

    """

    Asks user to specify a city, month, and day to analyze.

    Returns:

        (str) city - name of the city to analyze

        (str) month - name of the month to filter by, or "all" to apply no month filter

        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington)

    user_input = input("What city would you like to get statistics for?: ")

    if user_input.lower() in ("chicago", "new york city", "washington"):

        city = user_input

        print("You have selected ", city.title())

    else:

        while user_input.lower() not in ("chicago", "new york city", "washington"):

            print("That is not a correct city. Input 'Chicago', 'New York City'  or 'Washington'")

            user_input = input("What city would you like to get statistics for?: ")

        city = user_input

        print("You have selected ", city.title())

    # Get user input for month (all, january, february, march, april, may, june)

    month_input = input("What month would you like to get statistics for?: ")

    if month_input.title() in ("January", "February", "March", "April", "May", "June", "All"):

        month = month_input

        print("You have selected ", month.title())

    else:

        while month_input.title() not in ("January", "February", "March", "April", "May", "June", "All"):

            print(

                "That is not a correct month. Input: 'January', 'February', 'March', 'April', 'May', 'June', or 'All'")

            month_input = input("What month would you like to get statistics for?: ")

        month = month_input

        print("You have selected ", month.title())

    # Get user input for day of week (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)

    day_input = input("What day would you like to get statistics for?: ")

    if day_input.title() in ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "All"):

        day = day_input

        print("You have selected ", day.title())

    else:

        while day_input.title() not in ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "All"):

            print(

                "That is not a correct day. Input: 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', or 'All'")

            day_input = input("What day would you like to get statistics for?: ")

        day = day_input

        print("You have selected ", day.title())

    print('-'*40)
    city = city.lower()
    month = month.lower()
    day = day.lower()

    return city, month, day


def load_data(city, month, day):

    """

    Loads data for the specified city and filters by month and day if applicable.

    Args:

        (str) city - name of the city to analyze

        (str) month - name of the month to filter by, or "all" to apply no month filter

        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    Returns:

        df - Pandas DataFrame containing city data filtered by month and day

    """

    df = pd.read_csv(CITY_DATA.get(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['months'] = df['Start Time'].dt.month #strftime("%B")
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
        
    if month != 'all':
        month = month.title()
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    #filter by month to create the new dataframe
        df = df[df['months'] == month]
    return df


def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['months'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()

    # Display most commonly used start station

    start_station = df['Start Station'].value_counts()
    index_start_station = start_station.index.tolist()
    print("Most popular start station is ", index_start_station[0], "used ", start_station[0], " times")

    # Display most commonly used end station

    end_station = df['End Station'].value_counts()
    index_end_station = end_station.index.tolist()
    print("Most popular end station is ", index_end_station[0], "used ", end_station[0], " times")

    # Display most frequent combination of start station and end station trip
    start_and_end_station = df.groupby(['Start Station', 'End Station']).size().reset_index(name='Frequency')
    start_and_end_station = start_and_end_station.sort_values(by='Frequency', ascending=False)
    print("The most frequent combination of start station and end station trip is")
    print(start_and_end_station[:1])

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    start_time = time.time()

    # Display total travel time

    print("Total travel time is: ", df['Trip Duration'].sum(), " seconds")

    # Display mean travel time

    print("Average travel time is: ", df['Trip Duration'].mean(), " seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    start_time = time.time()

    # Display counts of user types

    user_count = df['User Type'].value_counts()

    index_user_count = user_count.index.tolist()

    print(index_user_count[0] + 's', user_count[0], index_user_count[1] + 's', user_count[1])

    # Display counts of gender

    try:
        gender_count = df['Gender'].value_counts()

        index_gender_count = gender_count.index.tolist()

        print(index_gender_count[0], gender_count[0], index_gender_count[1], gender_count[1])
    except KeyError:

        print("No gender data available for this city.")

    # Display earliest, most recent, and most common year of birth

    try:
        print("The earliest year of birth is: ", df['Birth Year'].min())
    except KeyError:
        print("Earliest Year of Birth: No birth year data available for this city")

    try:
        print("The most recent year of birth is: ", df['Birth Year'].max())
    except KeyError:
        print(" Most Recent Year of Birth: No birth year data available for this city")

    try:
        date_of_birth_counts = df['Birth Year'].value_counts()

        index_date_of_birth_counts = date_of_birth_counts.index.tolist()

        print('The most common year of birth is ', index_date_of_birth_counts[0])
    except KeyError:
        print("Most Common Year of Birth: No birth year data available for this city")
    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def display_raw_data(df):
    """This function asks the user if he wants to display raw data and then shows him five rows and continues to do so
    until the user says No
    """
    user_input = input("Do you want to view raw data? ")
    num_rows = 0
    if user_input.lower() == "yes":
        num_rows += 5
        print(df.iloc[:num_rows, :])
        user_input = input("Do you want to view raw data? ")
        while user_input.lower() == "yes":
            num_rows += 5
            print(df.iloc[(num_rows - 5):num_rows, :])
            user_input = input("Do you want to view raw data? ")


def main():

    while True:

        city, month, day = get_filters()

        df = load_data(city, month, day)

        time_stats(df)

        station_stats(df)

        trip_duration_stats(df)

        user_stats(df)

        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() != 'yes':

            break


if __name__ == "__main__":

    main()

