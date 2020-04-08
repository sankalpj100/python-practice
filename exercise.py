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

def smallest(x):
    min = x[0]
    for i in x:
       if i < min:
        min = i
    return min

def largest_smallest(x):
    min = x[0]
    max = x[0]
    for i in x:
        if i < min:
           min = i
    for j in x:
        if j > max:
            max = j
    return [max, min]


def mean(x):
    l = 0
    d = 0
    while (l < len(x)):
        d = d + int(x[l])
        l += 1
    return d / len(x)

def median(x):
    x.sort()
    if len(x) % 2 == 0:
        return ((x[int(len(x)/2)] + x[int((len(x)/2) - 1)]) / 2)
    else:
        return x[int((len(x) - 1) / 2)]

def tables(x, y):
    i = 1
    while  i <= int(y):
        k = int(x) * int(i)
        a = print(f"{x} x {i}= {k}")
        i += 1

def tables2(x):
       b = 1
       while b <= x:
              for a in range(1,int(x + 1)):
                     print(a * b, end="\t ")
              print('\n')
              if b == 1:
                     print("--+-","-" * 8 * (int(x - 1)))
              print('\n')
              b += 1
       return
       
def panagram(x):
    x =  x.replace(" ", "")
    a = list(x)
    b = list(set(a))
    b.sort()
    c = "abcdefghijklmnopqrstuvwxyz"
    d = list(c)
    if b != d:
        return False
    else:
        return True
