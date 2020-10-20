# Creating number plates using python

# to import different states names.
import random

import string

# dictionary to print the name of the state from the given short form of states.
names = {'AN':'Andaman and Nicobar Islands', 'AP':'Andhra Pradesh', 'AR':'Arunachal Pradesh', 'AS':'Assam', 'BR':'Bihar',
         'CG':'Chhattisgarh', 'CH':'Chandigarh', 'DD':'Dadra and Nagar Haveli and Daman and Diu', 'DL':'Delhi', 'GA':'Goa',
         'GJ':'Gujarat', 'HP':'Himachal Pradesh', 'HR':'Haryana', 'JH':'Jharkhand', 'JK':'Jammu and Kashmir', 'KA':'Karnataka',
         'KL':'Kerala', 'LA':'Ladakh', 'LD':'Lakshadweep', 'MH':'Maharashtra', 'ML':'Meghalaya', 'MN':'Manipur',
         'MP':'Madhya Pradesh', 'MZ':'Mizoram', 'NL':'Nagaland', 'OD':'Odisha', 'PB':'Punjab', 'PY':'Puducherry',
         'RJ':'Rajasthan', 'SK':'Sikkim', 'TN':'Tamil Nadu', 'TR':'Tripura', 'TS':'Telangana', 'UK':'Uttarakhand',
         'UP':'Uttar Pradesh', 'WB':'West Bengal'}

# list representing states.
states = ['AN', 'AP', 'AR', 'AS', 'BR', 'CG', 'CH', 'DD', 'DL', 'GA', 'GJ', 'HP', 'HR', 'JH', 'JK', 'KA', 'KL', 'LA', 'LD',
          'MH', 'ML', 'MN', 'MP', 'MZ', 'NL', 'OD', 'PB', 'PY', 'RJ', 'SK', 'TN', 'TR', 'TS', 'TK', 'UP', 'WB']

# to print random state from the given choice using random.choice() function.
states_name = random.choice(states)

# to print city number of number plate using random.randint() function.
city_number = random.randint(1, 20)

first_letter = random.choice(string.ascii_uppercase)

second_letter = random.choice(string.ascii_uppercase)

# to print vehicle number using random.randint() function.
vehicle_number = random.randint(1, 9999)

# to print the number plate of the vehicle.
print("{}-{:>02}-{}{}-{:>04}".format(states_name, city_number, first_letter, second_letter, vehicle_number))