import wikipedia as wk

q = 'computer science'
r = wk.summary(q, sentences=3)
print(r)