#!/usr/bin/env python
# coding: utf-8

# # Create .txt File

# In[57]:


# create movie.txt
with open('movie.txt', 'w') as movie:
    movie.write("""Stranger Things
The Nun
When Life Gives You Tangerines
Adolescence
Ejen Ali
Doremon
Reply 1988
Ali Setan
Juvenile Justice
Money Heist""")

# create sport.txt
with open('sport.txt', 'w') as sport:
    sport.write("""Badminton
Football
Basketball
Tennis
Diving
Swimming
Cycling
Bowling
Volleyball
Wushu""")


# # Read Files

# In[59]:


try:
    print("Movies:")
    with open('movie.txt', 'r') as movie_file:
        for i, line in enumerate(movie_file, 1):
            print(f"{i}. {line.strip()}")

    print("\n\nSports:")
    with open('sport.txt', 'r') as sport_file:
        for i, line in enumerate(sport_file, 1):
            print(f"{i}. {line.strip()}")

except FileNotFoundError as e:
    print(f"Error: {e.filename} not found. Please check the file location.")


# # Upadte Files

# In[69]:


#Update movies.txt
with open('movie.txt', 'w') as movie_update:
    movie_update.write("""Stranger Things - A secret lab opens a portal to the Upside Down, unleashing terror on the town.
The Nun - Demonic nun haunts cursed abbey.
When Life Gives You Tangerines - Youth, family, bittersweet coming-of-age.
Adolescence - Teenage struggles and identity search.
Ejen Ali - Young spy saves futuristic city.
Doremon - Robot cat helps schoolboy's life.
Reply 1988 - Nostalgic friendship in 1980s Seoul.
Ali Setan - Campus love with rebellious twist.
Juvenile Justice - Tough judge handles teen crime.
Money Heist - Mastermind leads daring bank heist.
The Matrix - Reality questioned in cyber world.
Parasite - Class struggle turns deadly dark.
Avengers - Heroes unite to save universe.
Interstellar - Space mission to save humanity.
Geostrom - Climate disaster threatens earth's survival.""")


#Update sport.txt
with open('sport.txt', 'w') as sport_update:
    sport_update.write("""Badminton - A fast-paced racquet shuttle game.
Football - A Global game with goal scoring.
Basketball - Court game with hoops.
Tennis - Racquet dual on various courts.
Diving - Acrobatic jumps into water.
Swimming - Competitive strokes through water.
Cycling - Speed and endurance on wheels.
Bowling - Knock down 10 pins in lanes.
Volleyball - Team spikes over the net.
Wushu - Chinese martial ars with flair.
Sepak Takraw - Acrobatic foot volleyball using a rattan ball.
Kabaddi - High-intensity tag-and-hold game.
Archery - Precision sport using bow and arrow.
Table Tennis - Fast-paced ping pong duels.
Judo - Japanese martial arts focused on throws, grappling and ground control.""")


# # Missing Files Test

# In[71]:


import os

os.rename('sport.txt', 'sport_moved.txt')

try:
    print("Movies:")
    with open('movie.txt', 'r') as movie_file:
        for i, line in enumerate(movie_file, 1):
            print(f"{i}. {line.strip()}")

    print("\n\nSports:")
    with open('sport.txt', 'r') as sport_file:
        for i, line in enumerate(sport_file, 1):
            print(f"{i}. {line.stripe()}")

except FileNotFoundError as e:
    print(f"\nError: The file '{e.filename}' was not found.")
    print("Please make sure the file exists in the correct location.")

os.rename('sport_moved.txt', 'sport.txt')


# # JSON Save Data

# In[98]:


import json

def only_int(prompt, min_val=None, max_val=None, digits=None):
    while True:
        user_input = input(prompt)
        try:
            num = int(user_input)
            if digits is not None and len(user_input) != digits:
                print(f"Error: Must be exactly {digits} digits.")
                continue
            if min_val is not None and num < min_val:
                print(f"Error: Must be at least {min_val}.")
                continue
            if max_val is not None and num > max_val:
                print(f"Error: Must be at most {max_val}.")
                continue
            return num
        except ValueError:
            print("Error: Please enter a valid number (digits only).")
            
birth_year = only_int("Enter your year of birth (e.g., 1997): ", min_val=1900, max_val=2025, digits=4)
fav_num = only_int("Enter your favorite number: ")

user_data = {'birth_year': birth_year, 'fav_num': fav_num}

with open('user_data.json', 'w') as file:
    json.dump(user_data, file)

print("Data saved successfully!")


# # JSON Read Data

# In[100]:


import json

try:
    with open('user_data.json', 'r') as file:
        data = json.load(file)

    print(f"My year of birth: {data['birth_year']}")
    print(f"My favorite number: {data['fav_num']}")

except FileNotFoundError:
    print("Error: user_data.json file is not found.")

except json.JSONDecodeError:
    print(f"Error: The file contais invalid JSON data.")

except keyError:
    print("Error: The JSON file doesn't contain the expected keys.")



# In[ ]:





# In[ ]:





# In[ ]:




