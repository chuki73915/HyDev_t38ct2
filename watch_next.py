import spacy

# Loading advanced English model
nlp = spacy.load("en_core_web_md")

# Get description of the movie Hulk and pass to model
description = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

description_nlp = nlp(description)

# Create empty lists to store movie name, description and similarity
movie_name_list = []
movie_desc_list = []
movie_similarity_rating_list = []

with open("movies.txt", "r") as file:
    # For each line in the movie file, save information into the lists
    # Then compute similarity with the description of Planet Hulk
    for line in file:
        movie_name_list.append(line[0:7])
        movie_desc = line[9::]
        movie_desc_list.append(movie_desc.replace('\n', ''))
        similarity = nlp(movie_desc).similarity(description_nlp)
        movie_similarity_rating_list.append(similarity)

# Identify the movie with the highest similarity and print to user
highest_similarity = max(movie_similarity_rating_list)
similarity_index = movie_similarity_rating_list.index(highest_similarity)
print(f'If you liked the movie "Planet Hulk", you will also enjoy {movie_name_list[similarity_index]}.'
      f'\nThe description of the movie is as follows:\n"{movie_desc_list[similarity_index]}"')
