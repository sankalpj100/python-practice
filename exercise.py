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

    def freq(s):
    a = list(s)
    a.sort()
    inwords = (set(a))
    new = []
    for word in inwords:
        counts = s.count(word)
        new.append(counts)
    freqdict = {}
    for key in inwords:
        for value in new:
            freqdict[key] = value
            new.remove(value)
            break

    return freqdict

def mode(s):
    inwords = (set(s))
    new = []
    for word in inwords:
        counts = s.count(word)
        new.append(counts)
    freqdict = {}
    for key in new:
        for value in inwords:
            freqdict[key] = value
            inwords.remove(value)
            break

    return  freqdict[max(freqdict.keys())]

def den(x):
    a = 0
    while x >= 2000:
        x -= 2000
        a += 1
        print(f"2000 x {a} = {2000 * a} ({x} left)")
    a = 0
    while x >= 500:
        x -= 500
        a += 1
        print(f"500 x {a} = {500 * a} ({x} left)")
    a = 0
    while x >= 200:
        x -= 200
        a += 1
        print(f"200 x {a} = {200 * a} ({x} left)")
    a = 0
    while x >= 100:
        x -= 100
        a += 1
        print(f"100 x {a} = {100 * a} ({x} left)")
    a = 0
    while x >= 50:
        x -= 0
        a += 1
        print(f"50 x {a} = {50 * a} ({x} left)")
    a = 0
    while x >= 20:
        x -= 20
        a += 1
        print(f"20 x {a} = {20 * a} ({x} left)")
    a = 0
    while x >= 10:
        x -= 10
        a += 1
        print(f"10 x {a} = {10 * a} ({x} left)")
    a = 0
    while x >= 5:
        x -= 5
        a += 1
        print(f"5 x {a} = {5 * a} ({x} left)")
    a = 0
    while x >= 1:
        x -= 1
        a += 1
        print(f"1 x {a} = {1 * a} ({x} left)")
    
    return
