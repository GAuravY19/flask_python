
def coding(msg, first, sec):
    lst = " "
    nxt=msg.split() 
    for j in nxt:
        if len(j)<=2: 
            new=j[-1::-1] 
            lst = lst + new + " "
        else:
            new= first + j[-1::-1] + sec 
            lst = lst + new + " "
            
    return lst    
         
def decoding(msg):
    dec = ' '
    nxt=msg.split() 
    for k in nxt: 
        if len(k)<=3:
            new=k[-1::-1]
            dec = dec + new + ' '
        else:
            new=k[3:-3]  
            new_dug=new[-1::-1] 
            dec = dec + new_dug + " "
            
    return dec