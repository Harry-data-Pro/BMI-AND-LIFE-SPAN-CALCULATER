def BMI():
    print("Let's Test Your BMI Score And Your Life Span")

    h = input("Enter Your HEIGHT (e.g. 5'10 for feet+inches or 1.78 for meters) ---> ").strip()


    if "'" in h:
        try:
            feet, inches = map(int, h.replace("'", " ").split())
            height_m = feet * 0.3048 + inches * 0.0254
        except ValueError:
            print("Invalid format. Please enter height like 5'10")
            return
    else:
        try:
            h_float = float(h)
            if h_float > 3.0:
                height_m = h_float / 3.2808399
            else:
                height_m = h_float
        except ValueError:
            print("Invalid numeric input for height.")
            return


    try:
        weight = float(input("Enter Your WEIGHT in KG ---> "))
    except ValueError:
        print("Invalid weight input.")
        return


    bmi = round(weight / height_m**2, 2)
    print(f"Your BMI is ---> {bmi}")

    if bmi < 18.5:
        print('Category: Underweight | Health Risk: Increased risk of malnutrition, osteoporosis, and anemia')
    elif 18.5 <= bmi <= 24.9:
        print('Category: Normal weight | Health Risk: Lowest risk for weight-related diseases')
    elif 25 <= bmi <= 29.9:
        print('Category: Overweight | Health Risk: Increased risk of cardiovascular issues, diabetes')
    elif 30 <= bmi <= 34.9:
        print('Category: Obesity Class I | Health Risk: High risk of heart disease and hypertension')
    elif 35 <= bmi <= 39.9:
        print('Category: Obesity Class II | Health Risk: Very high risk of serious conditions')
    else:
        print('Category: Obesity Class III | Health Risk: Extremely high risk of severe diseases')

    return bmi

def life_span(bmi):
    score=0
    import pandas as pd
    df = pd.read_csv('C:\\python\\codes\\notebook\\cleaned_data.csv')
    user_input=input('Enter if You Want TO Calculate Your Life Span and Time Left (Yes/No)--->').lower()
    if user_input != 'yes':
        print("Okay! Stay healthy and have a great day!")
        return
    if user_input == 'yes':
        country = input("Enter your country: ").strip().title()
        age= int(input('Enter Your Age: ').strip().title())
        smokes = input("Do you smoke? (Yes/No): ").strip().lower()
        if smokes == 'yes':
            slvl=input('Enter Your Consumption lvl (weekly/daily): ').strip().lower()
            if slvl=='weekly':
                score += 2
            elif slvl=='daily':
                score += 5
        alcohol = input("Do you consume alcohol ? (Yes/No): ").strip().lower()
        if alcohol == 'yes':
            alvl=input('Enter Your Consumption lvl (weekly/daily): ').strip().lower()
            if alvl=='weekly':
                score+=1
            elif alvl=='daily':
                score+=3
        fastfood = input("How much fast food do you eat? (no/weekly/daily): ").strip().lower()   
        if fastfood== 'no':
            score+=0
        elif fastfood=='weekly':
            score+= 3
        elif fastfood=='daily':
            score+= 6     
        activity = input("Activity level (Low/Moderate/High): ").strip().lower()
        if activity=='low':
            score+=5
        elif activity=='moderate':
            score+=1
        elif activity=='high':
            score-=3
        disease_dict = {
            'blood pressure': 5,
            'diabetes': 6,
            'heart disease': 8,
            'stroke': 10,
            'cancer': 8,
            'kidney disease': 7,
            'liver disease': 6,
            'cholesterol': 5,
            'influenza': 1,
            'pneumonia': 2,
            'depression': 3,
            'anxiety disorders': 2,
            'substance use disorder': 4,
            'alcohol use disorder': 4,
            'hiv/aids': 10,
            'cirrhosis': 6,
            'multiple sclerosis': 6,
            'rheumatoid arthritis': 4,
            'epilepsy': 3,
            'osteoporosis': 4,
            'severe anemia': 2,
            'tuberculosis': 2,
            'malaria': 3,
            'meningitis': 4,
            'covid-19': 2,
            'hypertensive crisis': 5,
            'chronic migraine': 2,
            'hyperthyroidism': 2,
            'hypothyroidism': 2,
            'brain tumors': 10,
            'bladder cancer': 8,
            'breast cancer': 6,
            'colorectal cancer': 7,
            'prostate cancer': 5,
            'ovarian cancer': 6,
            'cervical cancer': 4,
            'pancreatic cancer': 10,
            'gastric cancer': 8,
            'fatal familial insomnia': 1,
            'rabies': 1,
            'gerstmann-sträussler-scheinker syndrome': 1,
            'bipolar disorder': 9,
            'schizophrenia': 10,
            'drug and alcohol abuse': 9,
            'recurrent depression': 7
        }
        disease=input('Do You have any common disease like blood pressure ,Diabetes etc. if YES then name of the Disease else no -->	').strip().lower()
        if disease != 'no':
            disease = disease.lower()
            for disease_name in disease_dict:
                if disease_name in disease:
                    score += disease_dict[disease_name]



        if country in df['Country Name'].unique():
             avg_life = df[df['Country Name'] == country]['2022'].mean()
        else:
            print("Country not found. Using global average.")
            avg_life = df['2022'].mean()
        if bmi < 18.5:
            score+=2
        elif 18.5 <= bmi <= 24.9:
            score+=0
        elif 25 <= bmi <= 29.9:
            score+=2
        elif 30 <= bmi <= 34.9:
            score+=6
        elif 35 <= bmi <= 39.9:
            score+=9
        elif 40 <= bmi <=99999:
            score+=15            
        else:
            score+=0
    life_expectancy = avg_life - score
    print(f"Estimated Life Expectancy in {country.title()} ---> {round(avg_life,1)} years")
    print(f"Adjusted Life Expectancy based on your lifestyle ---> {round(life_expectancy,1)} years")  
    remaining_life = round(life_expectancy, 1) - age
    if remaining_life < 0:
        print("You've outlived your adjusted life expectancy!")
    else:
        print(f'Your Remaining Life ---> {round(remaining_life, 1)} years')    


bmi_score = BMI()
if bmi_score:
    life_span(bmi_score)