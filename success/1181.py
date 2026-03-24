N = int(input())
words = []

for i in range(N) :
    words.append(input())
words = list(set(words))
        
words.sort(key = lambda x : (len(x),x))

for i in words : 
    print(i)