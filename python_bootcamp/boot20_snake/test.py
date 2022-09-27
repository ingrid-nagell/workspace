from tabulate import tabulate
f = open("python_bootcamp/boot20_snake/highscores.txt", "r")
users = []
user = {}
for line in f:
    nickname, score, version = line.split(";")
    user["nickname"] = nickname
    user["score"] = int(score)
    user["version"] = str(int(version))
    u = user.copy()
    users.append(u)
f.close()

users_sorted = sorted(users, key=lambda i: i['score'], reverse=True)
top_10 = users_sorted[0:10]

text = "Place\tNickname\tScore\t\tVersion\n------------------------------------------------"
#for i, e in enumerate(top_10):	
#	text += f"\n{i+1}\t{e['nickname']}\t\t{e['score']: ^10}\t{e['version']: ^10}"

print(text)