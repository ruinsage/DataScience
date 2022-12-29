q = 'park 800905-1049118'
a = q.rfind("-")
b = q[a+1:]
for i in q[a+1:]:
    q = q.replace(q,i,'*')
print(q)
pass