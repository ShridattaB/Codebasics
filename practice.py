# f=open("funny.txt","r")
# for line in f:
#     print(line)
# f.close()

# #in with statement we dont want to clsoe file 
# with open ("funny.txt","r") as f:
#     for line in f:
#         print(line)

# #read one lines or more lines
# with open ("funny.txt","r") as f:
#     lines=f.readlines()
#     print(lines)


#if we want to write in file
# with open ("funny.txt","w") as f:
#     f.write("i love python")


#if we want to add line then we use append mode
# with open ("funny.txt","a") as f:
#     f.write("\n i love codebasics")


# # add more lines
# with open ("funny.txt","a") as f:
#     f.writelines([
#         "\ni love fortran"
#         "\ni love pascal"
#         "\n i love main framw"
#     ])





#read a one csv file 
# players_score={}
# with open ("scores.csv","r") as f:
#     for line in f:
#         playername,  score=line.split(',')
#         score=int(score)
#         if playername in players_score:
#             players_score[playername]=[score].append(score)
#             pass
#         else:
#             players_score[playername]=[score]

# print(players_score)

#from any csv file here list of names and his scores
# playersscore={}
# with open("scores.csv","r") as f:
#     for line in f:
#         players , score = line.split(',')
#         score=int(score)
#         if players in playersscore:
#             playersscore[players].append(score)
#         else:
#             playersscore[players]=[score]

# print(playersscore)



playersscore={}
with open("scores.csv","r") as f:
    for line in f:
        players , score = line.split(',')
        score=int(score)
        if players in playersscore:
            playersscore[players].append(score)
        else:
            playersscore[players]=[score]

print(playersscore)



for players, score_list in playersscore.items():
    print(players,score)
    min_score=min(score_list)
    max_score=max(score_list)
    avg_score=sum(score_list)/len(score_list)

    print(f"{players} ==min{min_score}==max{min_score}==avg{avg_score}")


