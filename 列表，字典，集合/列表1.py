score = {
    "小明": {"math": 90, "english": 78},
    "小红": {"math": 85, "english": 92},
}
a=score["小红"]
print(a["math"])
score["xaiogang"]={"math":60}
for b,c in score.items():
    print(f"\n{b} ,{c["math"]}")
