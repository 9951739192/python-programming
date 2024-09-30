#6. What are the total number of awards own by Ram Charan?
#7. Which actor won more number of Nandi Awards?
#8. What is the success rate of Prince?
#9. Which artist has more number of Hits?
#10. Who is Milky Beauty?
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

ram_awards=movies['actors']['ramcharan']['awards']
print(ram_awards,type(ram_awards))

#8. What is the success rate of Prince?
s_rate=movies['actors']['mahesh']['sRate']
print(s_rate)

#Which actor won more number of Nandi Awards?
max_nandi_awards = -1
best_actor = None

for actor_name, details in movies['actors'].items():
    nandi_awards = details['awards']['nandi']
    if nandi_awards > max_nandi_awards:
        max_nandi_awards = nandi_awards
        best_actor = actor_name
if best_actor:
    print(f"The actor who won the most Nandi Awards is {movies['actors'][best_actor]['knownAs']} ({best_actor}) with {max_nandi_awards} awards.")

#Which artist has more number of Hits?
more_hits=-1
best_performer=None
for actor_name,details in movies['actors'].items():
    hits=details['hits']['industry']+details['hits']['super']
    if hits > more_hits:
        more_hits=hits
        best_performer=actor_name
print(f"The best performer:{best_performer} with {more_hits}")
    
##10. Who is Milky Beauty?
beuty=movies['actress']['tamanna']['knownAs']
print(beuty)                        
