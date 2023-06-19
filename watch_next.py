
import spacy

nlp = spacy.load('en_core_web_md')


def movie(description):
    
    movies = open("movies.txt", "r")
    split_list = []#split the movie and store the title in a list

    
    for i in movies:
        split_list.append(i.split(':'))


    count = len(split_list)
    list_of_simmilarities = []

    model_sentence = nlp(description)

    for i in range(0, count):
        list_of_simmilarities.append(nlp(split_list[i][1]).similarity(model_sentence))

    #max_similarity = max(split_list)

    max_similarity = max(list_of_simmilarities)
    max_similarity_index = list_of_simmilarities.index(max_similarity) #getting the index of the most similarity value

    
    return split_list[max_similarity_index][0] # return the title of the most similar movie

# The movie description to be compared with
hulk_description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""


print("The most simillar movie to watch next from movies.txt is : " + movie(hulk_description))
