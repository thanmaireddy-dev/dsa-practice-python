def find_players_with_zero_or_one_losses(matches):
    seen={}
    zero_loss=[]
    one_loss=[]
    for match in matches:
        if match[0] in seen:
            pass
        else:
            seen[match[0]]=0
        if match[1] in seen:
            seen[match[1]]+=1
        else:
            seen[match[1]]=1
    for key,val in seen.items():
        if val==0:
            zero_loss.append(key)
        elif val==1:
            one_loss.append(key)
    zero_loss.sort()
    one_loss.sort()
    return[zero_loss, one_loss]

print(find_players_with_zero_or_one_losses([[2,3],[1,3],[5,4],[6,4]]))