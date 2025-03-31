"""
coderbyte challenge for printing the count of how many keys with 'age' are greater than or equal to 50.
"""
import requests

def count_age_above_50():
    response = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
    data = response.json()['data']
    
    # Split the string into items
    items = data.split(', ')
    
    count = 0
    for item in items:
        if item.startswith(' age='):
            age = int(item.split('=')[1])
            if age >= 50:
                count += 1
                
    print(count)

count_age_above_50()