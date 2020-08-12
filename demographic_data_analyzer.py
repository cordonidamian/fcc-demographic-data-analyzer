import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race = df.groupby(["race"])['native-country'].count()
    race_count = race.sort_values(ascending=False)

    # What is the average age of men?
    avg_age_men = df.groupby(["sex"])['age'].mean()
    avg_age_men = avg_age_men['Male']
    average_age_men = round(avg_age_men,1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelor = df[df['education'] == 'Bachelors']
    bachelor_percentage = (len(bachelor) * 100) / len(df)
    bachelor_percentage = round(bachelor_percentage,1)
    percentage_bachelors = bachelor_percentage

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    education_higher = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    total_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count().max()
    tolal_plus_50K = education_higher[education_higher['salary'] == '>50K'].count().max()
    tolal_plus_50K = (tolal_plus_50K * 100) / total_education
    higher_education = round(tolal_plus_50K,1)

    education_lower = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    total_education_lower = education_lower.count().max()
    not_higher = education_lower[education_lower['salary'] == '>50K'].count().max()
    not_higher = (not_higher * 100) / total_education_lower
    lower_education = round(not_higher, 1)

    # percentage with salary >50K
    higher_education_rich = higher_education
    lower_education_rich = lower_education

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_hours_per_week = df['hours-per-week'].min()
    min_work_hours = min_hours_per_week

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    more_50_K = df[df['hours-per-week'] == 1]
    more_50_K = more_50_K[more_50_K['salary'] == '>50K']
    more_50_K = more_50_K.count().max()
    total_one_per_week = df[df['hours-per-week'] == 1].count().max()
    more_50_K = (more_50_K * 100) / total_one_per_week

    num_min_workers = round(more_50_K)

    more_50_K = df[df['hours-per-week'] == 1]
    more_50_K = more_50_K[more_50_K['salary'] == '>50K']
    more_50_K = more_50_K.count().max()
    total_one_per_week = df[df['hours-per-week'] == 1].count().max()
    more_50_K = (more_50_K * 100) / total_one_per_week

    rich_percentage = round(more_50_K)

    # What country has the highest percentage of people that earn >50K?
    all = df[['salary', 'native-country']]
    entire = all.groupby(['native-country']).count()
    plus50K = all[all['salary']=='>50K']
    plus50K = plus50K.groupby(['native-country']).count()
    plus50K = (plus50K*100) / entire
    plus50K.sort_values(by=['salary'], inplace=True, ascending=False)
    final = pd.Series(plus50K['salary'])
    
    highest_earning_country = final.index[0]
    highest_earning_country_percentage = round(final.values[0],1)

    # Identify the most popular occupation for those who earn >50K in India.
    prof = df[df['salary'] == '>50K'] [['occupation', 'native-country', 'salary']]
    prof = prof[prof['native-country'] == 'India']
    
    prof = prof.describe()
    
    top_IN_occupation = prof.loc['top', 'occupation']

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
