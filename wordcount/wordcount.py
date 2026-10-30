from pathlib import Path
from os import path
text="""The quick brown fox jumps over the lazy dog. The dog barks and the fox runs away.
A quick fox is a happy fox, and the lazy dog sleeps.
The fox and the dog are friends."""
p=Path("wordcount.py").parent
d=p/"text.txt"
d.write_text(text,encoding="utf-8")
m=text.strip(".?;:!,").rstrip("\n").split()
l={}
o=1
for i in m:
    i=i.lower().strip(".?;:!,")
    cout= l.get(i,0)+1
    l[i]=cout
a=sorted(l,key=l.get,reverse=True)[:20]
with open("text.txt","a",encoding="utf-8") as f:
    for c in a:
        f.write("\n")
        f.write(f"{o}.{c}-{l[c]}\n")
        o+=1
                                    


