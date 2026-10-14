alice = {"Bob", "Carol", "Dave"}
bob   = {"Carol", "Dave", "Eve"}
a=alice & bob
b=alice ^ bob
c=alice | bob

print(a,b,c,"\n")
def ded(seq):
    a=set()
    b=[]
    for i in seq:
        if i not in a:
            a.add(i)
            b.append(i)
    print(b)
s=[3, 1, 3, 2, 1]
ded(s)