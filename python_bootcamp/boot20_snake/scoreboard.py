# Create a scoreboard with scores of all players.
from tabulate import tabulate
#from prettytable import PrettyTable

def update_high_scores(nickname, score, version, file):
    '''Updates the list of high scores with specified imput.'''
    f = open(file, "a")
    update = f"{nickname};{score};{version}\n"
    f.write(update)
    f.close()


def high_score_table(file):
    '''Returns a high score table. Takes a comma-separated text file as input.'''
    f = open(file, "r")
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
    table = tabulate(top_10, headers='keys')
    high_scores = f"{'Top 10:': ^35}\n\n{table}"
    #for i, e in enumerate(top_10):	
	#    high_scores += f"\n{i+1}\t{e['nickname']}\t\t{e['score']}\t{e['version']}"
    return high_scores


def list_of_nicks(file):
    '''Returns a list of str from a comma-separted text file.'''
    nicknames = []
    f = open(file, "r")

    for line in f:
        nickname = line.split(";")[0]
        nicknames.append(nickname)
    
    f.close()
    return nicknames