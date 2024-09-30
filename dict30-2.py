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

#12. What are actress names who did not win at least one Nandi Award?
#13. What are the total number of SIIMA awards won by all artists?
#14. What is the artist name who has more success rate?
#16. What is the actress name who is married?
#18. Who is the Youngest artist?
#19. Who are unmarried actress?
#20. Who is smallest actress?
#21. Who is the Youngest artist?
#12. What are actress names who did not win at least one Nandi Award?
least_nandi_award=0
least_actor=None
for actress,details in movies['actress'].items():
  nandi=details['awards']['nandi']
  if least_nandi_award==nandi:
      least_actor=actress
      
      print(f"the least actress:{least_actor} with {least_nandi_award}")


#13. What are the total number of SIIMA awards won by all artists?
of_awards=0
for award in movies['actors'].values():
    of_awards+=award['awards']['siima']
    

for award in movies['actress'].values():
   of_awards+=award['awards']['siima']
    
print(of_awards)    
    
#14. What is the artist name who has more success rate?
max_success_rate = -1
artist_name = ""
for category in movies.values():
    for artist, details in category.items():
        
        success_rate = float(details['sRate'].strip('%'))  
        if success_rate > max_success_rate:
            max_success_rate = success_rate
            artist_name = details['knownAs']

print(f"The artist with the highest success rate is: {artist_name} with success rate of {max_success_rate}%")

#What is the actress name who is married
married_actresses = []
for actress, details in movies['actress'].items():
    if details['mStatus'] == 'married':
        married_actresses.append(details['knownAs'])

print("Married actresses:", married_actresses)

#Who is the Youngest artist?

youngest_artist = None
youngest_age = float('inf')


for actor, details in movies['actors'].items():
    if details['age'] < youngest_age:
        youngest_age = details['age']
        youngest_artist = details['knownAs']


for actress, details in movies['actress'].items():
    if details['age'] < youngest_age:
        youngest_age = details['age']
        youngest_artist = details['knownAs']

print("The youngest artist is:", youngest_artist)




# Who is smallest actress?
smallest_actress = None
smallest_height = float('inf')
for actress, details in movies['actress'].items():
    if details['height'] < smallest_height:
        smallest_height = details['height']
        smallest_actress = details['knownAs']

print("The smallest actress is:", smallest_actress)


#12. What are actress names who did not win at least one Nandi Award?
actresses_without_nandi = []
for actress, details in movies['actress'].items():
    if details['awards']['nandi'] == 0:
        actresses_without_nandi.append(details['knownAs'])

print("Actresses who did not win at least one Nandi Award:", actresses_without_nandi)

















