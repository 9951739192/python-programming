
# Write a program to display all actors names
#2. Write a program to display all actress names
#3. Who is Darling?
#4. What are the total number of Nandi Awards won by actors?
#5. What is the name of Prince?


movies = {
 'actors': {
     'prabhas': {'knownAs': 'Darling', 'awards': {'nandi': 1, 'cinemaa': 1, 'siima': 1}, 'remuneration': 100,
                 'hits': {'industry': 2, 'super': 3, 'flops': 8}, 'age': 41, 'height': 6.1, 'mStatus': 'single', 'sRate': '35%'},
     'mahesh': {'knownAs': 'Prince', 'awards': {'nandi': 8, 'cinemaa': 3, 'siima': 3}, 'remuneration': 50,
                'hits': {'industry': 2, 'super': 6, 'flops': 11}, 'age': 46, 'height': 6.2, 'mStatus': 'married', 'sRate': '46%'},
     'ramcharan': {'knownAs': 'Mega Power Star', 'awards': {'nandi': 2, 'cinemaa': 1, 'siima': 1},
                   'remuneration': 70, 'hits': {'industry': 3, 'super': 1, 'flops': 5}, 'age': 36, 'height': 5.9, 'mStatus': 'married',
                   'sRate': '50%'},
     'ntr': {'knownAs': 'Jr NTR', 'awards': {'nandi': 2, 'cinemaa': 5, 'siima': 3}, 'remuneration': 70,
             'hits': {'industry': 1, 'super': 7, 'flops': 11}, 'age': 36, 'height': 5.9, 'mStatus': 'married', 'sRate': '40%'},
     'pavan': {'knownAs': 'Power Star', 'awards': {'nandi': 2, 'cinemaa': 2, 'siima': 5}, 'hits': {'industry': 2,
             'super': 7, 'flops': 16}, 'age': 48, 'height': 5.9, 'mStatus': 'married', 'sRate': '37%', 'remuneration': 50},
 },
 'actress': {
     'tamanna': {'knownAs': 'Milky Beauty', 'awards': {'nandi': 0, 'cinemaa': 1, 'siima': 1},
                 'remuneration': 10, 'hits': {'industry': 1, 'super': 7, 'flops': 11}, 'age': 28, 'height': 5.9, 'mStatus': 'single',
                 'sRate': '40%'},
     'rashmika': {'knownAs': 'Butter Milky Beauty', 'awards': {'nandi': 0, 'cinemaa': 0, 'siima': 2},
                  'remuneration': 12, 'hits': {'industry': 0, 'super': 4, 'flops': 2}, 'age': 36, 'height': 5.9, 'mStatus': 'single',
                  'sRate': '30%'},
     'saipallavi': {'knownAs': 'Laughing Queen', 'awards': {'nandi': 0, 'cinemaa': 0, 'siima': 2},
                    'remuneration': 8, 'hits': {'industry': 0, 'super': 3, 'flops': 0}, 'age': 28, 'height': 5.9, 'mStatus': 'single',
                    'sRate': '60%'},
     'samantha': {'knownAs': 'Sam', 'awards': {'nandi': 2, 'cinemaa': 3, 'siima': 5}, 'remuneration': 15,
                  'hits': {'industry': 3, 'super': 7, 'flops': 4}, 'age': 33, 'height': 5.9, 'mStatus': 'married', 'sRate': '70%'},
     'kajal': {'knownAs': 'Kaj', 'awards': {'nandi': 0, 'cinemaa': 2, 'siima': 2}, 'remuneration': 12,
               'hits': {'industry': 1, 'super': 6, 'flops': 8}, 'age': 35, 'height': 5.9, 'mStatus': 'married', 'sRate': '60%'},
 }
}


for actor, details in movies['actors'].items():
    print(f"Name: {actor.capitalize()}")
    print(f"Known As: {details['knownAs']}")
    print(f"Awards: {details['awards']}")
    print(f"Remuneration: {details['remuneration']}")
    print(f"Hits: {details['hits']}")
    print(f"Age: {details['age']}")
    print(f"Height: {details['height']}")
    print(f"Marital Status: {details['mStatus']}")
    print(f"Success Rate: {details['sRate']}")
    print()


#2. Write a program to display all actress names
for actress,details in movies['actress'].items():
    print(f"Name: {actress.capitalize()}")
    print(f"Known As: {details['knownAs']}")
    print(f"Awards: {details['awards']}")

    print(f"Remuneration: {details['remuneration']}")
    print(f"Hits: {details['hits']}")
    print(f"Age: {details['age']}")
    print(f"Height: {details['height']}")
    print(f"Marital Status: {details['mStatus']}")
    print(f"Success Rate: {details['sRate']}")
    print()
    
    
#3. Who is Darling?
darling_name=movies['actors']['prabhas']['knownAs']
print(darling_name)

#4. What are the total number of Nandi Awards won by actors?
total_nandi_awards = sum(actor['awards']['nandi'] for actor in movies['actors'].values())

print(f"Total number of Nandi Awards won by actors: {total_nandi_awards}")

nandi_awards=sum(actor['awards']['nandi'] for actor in movies['actors'].values())
print(nandi_awards)
#5. What is the name of Prince?

prince_name = movies['actors']['mahesh']['knownAs']
print(prince_name)     
