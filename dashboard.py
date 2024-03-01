import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv('day_bike.csv')

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Define Streamlit App
st.title('Bike Rental Analysis (2011-2012)')

# Sidebar with options
st.sidebar.title('Analysis Options')
selected_analysis = st.sidebar.selectbox('Select Analysis', ['Monthly Trend', 'Weather Impact', 'Daily Pattern'])

# Main Content
if selected_analysis == 'Monthly Trend':
    st.header('Monthly Trend of Bike Rentals')
    st.write('Here is the monthly trend of bike rentals over the two-year period (2011-2012):')
    monthly_rentals = df.groupby(['year', 'month'])['total_count'].sum().reset_index()
    monthly_rentals['date'] = pd.to_datetime(monthly_rentals[['year', 'month']].assign(day=1))
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_rentals['date'], monthly_rentals['total_count'], marker='o', linestyle='-')
    plt.title('Monthly Trend of Bike Rentals (2011-2012)')
    plt.xlabel('Date')
    plt.ylabel('Total Bike Rentals')
    plt.grid(True)
    st.pyplot(plt)

    # Explanation for Question 1
    with st.expander("See explanation"):
        st.write("Conclusion for Question 1:")
        st.write("- The monthly trend of bike rentals over the two-year period (2011-2012) indicates fluctuating patterns.")
        st.write("- Rentals gradually increase from January to May, peaking steadily until October.")
        st.write("- Subsequently, there is a decline in rental counts until January of the following year, followed by a rise similar to the previous year.")
        st.write("- Peak rental months are observed from May to October, with a subsequent decline.")

elif selected_analysis == 'Weather Impact':
    st.header('Impact of Weather Condition on Bike Rentals')
    st.write('Here is the impact of weather condition on bike rentals over the two-year period (2011-2012):')
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='weather', y='total_count')
    plt.title('Impact of Weather Condition on Bike Rentals (2011-2012)')
    plt.xlabel('Weather Condition')
    plt.ylabel('Total Bike Rentals')
    plt.grid(True)
    st.pyplot(plt)

    # Explanation for Question 2
    with st.expander("See explanation"):
        st.write("Conclusion for Question 2:")
        st.write("- Weather conditions significantly impact bike rentals over the two-year period (2011-2012).")
        st.write("- Clear weather conditions tend to result in higher average rental counts compared to misty or rainy conditions.")
        st.write("- Favorable weather conditions, such as clear skies, create a more conducive environment for outdoor activities like biking.")
        st.write("- Good weather tends to increase interest in biking, leading to higher rental counts.")

else:
    st.header('Daily Bike Rental Pattern on Weekdays vs. Weekends')
    st.write('Here is the daily bike rental pattern on weekdays versus weekends over the two-year period (2011-2012):')
    df['weekday'] = df['date'].dt.day_name()
    daily_rentals = df.groupby('weekday')['total_count'].mean()
    weekdays_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    plt.figure(figsize=(10, 6))
    plt.plot(daily_rentals.loc[weekdays_order[:-2]], label='Weekdays', marker='o')
    plt.plot(daily_rentals.loc[['Saturday', 'Sunday']], label='Weekends', marker='o')
    plt.title('Daily Bike Rental Pattern on Weekdays vs. Weekends (2011-2012)')
    plt.xlabel('Day of the Week')
    plt.ylabel('Average Bike Rentals')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

    # Explanation for Question 3
    with st.expander("See explanation"):
        st.write("Conclusion for Question 3:")
        st.write("- The daily bike rental pattern on weekdays versus weekends over the two-year period (2011-2012) shows distinct differences.")
        st.write("- Weekdays, encompassing Monday through Friday, experience higher average bike rental counts compared to weekends (Saturday and Sunday).")
        st.write("- The two consecutive days with the lowest average bike rentals are observed on Sunday and Monday, contrary to the expected pattern of lower rentals on weekends (Saturday and Sunday).")
