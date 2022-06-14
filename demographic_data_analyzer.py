import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.groupby('sex').age.mean()['Male'],1)

    # What is the percentage of people who have a Bachelor's degree?
    education_count = df.groupby('education').education.count()
    education_total = education_count.sum()
    percentage_bachelors = round(
        ((education_count['Bachelors']) / education_total) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`

    higher_education = df.loc[df['education'].isin(["Bachelors", "Masters", "Doctorate"])] # People having advavnced degree
    num_higher_education = higher_education.size
    num_rich_advanced_degree = higher_education.loc[higher_education['salary'] == ">50K"].size # rich people with advanced ddegree
  
    lower_education = df.loc[~df['education'].isin(["Bachelors", "Masters", "Doctorate"])] # People not having advanced degree
    num_lower_education = lower_education.size
    num_rich_lower_degree = lower_education.loc[lower_education['salary'] == ">50K"].size # rich people without advanced degree

    

    #percentage with salary >50K

    higher_education_rich = round(100*(num_rich_advanced_degree/num_higher_education) , 1)
    lower_education_rich = round(100*(num_rich_lower_degree/num_lower_education) ,1)

    min_work_hours = df["hours-per-week"].min(axis=0) 

    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours] # number of workers that work equal to minimum wirk hours

    rich_percentage = round(100*num_min_workers.loc[num_min_workers["salary"] == ">50K"].size / num_min_workers.size,1)

    # What country has the highest percentage of people that earn >50K?
    highest_country = (df[["salary","native-country"]].groupby('native-country').apply(lambda x: x.loc[x['salary'] == '>50K'].size/x.size * 100))
    highest_earning_country = highest_country.idxmax()
    highest_earning_country_percentage = round(highest_country.max(),1)
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = top_IN_occupation = df.loc[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].value_counts().idxmax()


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:",
              highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
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
