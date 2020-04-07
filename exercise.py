def digits(x):
    a = list(x)
    b = len(a)
    return b

def count_words(x):
    sentence_list = list(x.split(" "))
    words = len(sentence_list)
    return words

def largest(x):
    max = x[0]
    for i in x:
       if i > max:
           max = i
    return max
