def clean(line):
    
    line=line.replace("，",",")
    a=line.split(",")
    for i in range(0,len(a)):
        a[i]=a[i].strip()
    if len(a)!=3:
        return None
    name,number,lo=a
    if not (number.isdigit() and number.startswith("1")):
        return None
    if "@" not in lo:
        return None
    return [name,number,lo.lower()]
def cinkeyboard():
    ne=[]
    while True:
        ines=input()
        if  ines=="":
            break
        ne.append(ines)
    return ne
def main():
    o=cinkeyboard()
    skip=0
    row=[]
    for line in o:
        line=clean(line)
        if line is None:
            skip+=1
            continue
        row.append(line)
    print(f"有效{len(row)}条，跳过{skip}条")
    m={}
    l=set()
    for rows in row:
        m[rows[1][:3]]=m.get(rows[1][:3],0)+1
        
        l.add(rows[2].split("@")[1])
    b=sorted(m)
    print("号段分布:")
    for k in b:
        print(f"  {k}  {m[k]}")
    print(f"域名去重{",".join(sorted(l))}")
main()       


