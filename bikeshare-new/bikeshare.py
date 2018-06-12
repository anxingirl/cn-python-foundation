import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
   
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago','new york city','washington']
    city = ""
    while(city not in cities):
        city = input("Pls input the city name you want to explore.Choose from 'chicago,new york city,washington':\n").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january','february','march','april','may','june']
    month = ""
    while(month not in months):
        month = input("Pls input the month name you want to exlore. Choose from 'all','january','february','march','april','may','june':\n").lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day = ""
    while(day not in days):
        day = input("Pls input the week day you want to explore. Choose from 'all','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday':\n").title()
    print('-'*40)
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
    city = "_".join(city.split(" "))
    df = pd.read_csv(city+'.csv')
    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%d %H:%M:%S')
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
    months = ['january','february','march','april','may','june']
    if(month != 'all'):
        df = df[df['month'] == months.index(month)+1]
    print(df.iloc[1])
    print(day)
    if(day != 'all'):
        df = df[df['weekday'] == day]  
    print(df.iloc[1])
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    #print(df['month'].value_counts())
    months = ['january','february','march','april','may','june']
    freq_month = months[df['month'].mode()[0]-1]
    print("The most common month is {}".format(freq_month))
    # TO DO: display the most common day of week
    print("The most common day of week is {}".format(df['weekday'].mode()[0]))
    # TO DO: display the most common start hour
    print("The most common start hour is {}".format(df['Start Time'].dt.hour.mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is {}".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most commonly used start station is {}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    max_trip = df.groupby(['Start Station','End Station']).size().reset_index().max()
    print("Most frequent combination of start station and end station trip is from '{}' to '{}'".format(max_trip['Start Station'], max_trip['End Station']))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    print("Total travel time:{}".format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("Total travel time:{}".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
   
    # TO DO: Display counts of user types
    print(df.groupby("User Type").size())
    
    if('Gender' in df.columns.tolist()):
    # TO DO: Display counts of gender
        print(df.groupby('Gender').size()) 

    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df.columns.tolist()):
        print("The earliest year of birth:{}".format(df["Birth Year"].min()))
        print("The recent year of birth;{}".format(df['Birth Year'].max()))
        print("The most common year of birth:{}".format(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

