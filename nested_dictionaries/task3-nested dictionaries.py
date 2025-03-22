import requests

baseurl="https://randomuser.me/api/?results=500"

response_3=requests.get(baseurl)

data=response_3.json()

print(data)

profile_of_male = []
profile_of_female= []
date_of_birth=[]
full_name=[]
    
    
for item in data['results']:
        
        """
        created an empty list for male and female gender,date_of_birth and full_name

        for loops to iterate through the result list 

        Extracts gender, birth date, and full name for each user
        """
    
        if item['gender']=='male':
            profile_of_male.append('male')
        elif item['gender']=='female':
            profile_of_female.append('female')
            
        if   item['dob']:
            birth_date = item['dob']['date']
            date_of_birth.append(birth_date)
        if item['name']:
            first_name= item['name']['first']
            last_name=item['name']['last']
            full_name.append(f'my fulname is {first_name} {last_name}')
            
            
print( profile_of_male)
print(profile_of_female)
print(date_of_birth)
print(full_name)

print(len(profile_of_female))
print(len(profile_of_male))