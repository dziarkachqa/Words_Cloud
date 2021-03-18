# Here are all the installs and imports you will need for your word cloud script and uploader widget


import wordcloud
from matplotlib import pyplot as plt


# This is the uploader widget

with open ("Alice.txt",encoding="utf-8") as alice:
    file = alice.read()


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''’“”—!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    file_contents = file_contents.lower()
    for char in file_contents:
        if char in punctuations:
            file_contents = file_contents.replace(char, '')

    updated_contents = file_contents
    more_updated_contents = []
    word_dict = {}

    updated_contents = updated_contents.split()
    for word in updated_contents:
        if word not in uninteresting_words:
            more_updated_contents.append(word)

    for word in more_updated_contents:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1


#wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_dict)
    return cloud.to_array()

# Display your wordcloud image
myimage = calculate_frequencies(file)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
