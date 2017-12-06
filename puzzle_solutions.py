#function to check most wanted character
def checkio(text):
    tc=text.lower()
    ln=len(tc)
    count={}
    result={}
    al=''
    for c in tc:
        if c.isalpha():
            if c in count:
                count[c]+=1
            else:
                count[c]=1
    #al= max(count, key=count.get)
    for val in count:
        if count[val] in result:
            result[count[val]].append(val)
        else:
            result[count[val]] = [val]
    max_key=max(result)
    if len(result[max_key])>1:
        al=min(result[max_key])
    else:
        al=result[max_key][0]
        
    return al

#function to check repeated elements in list
def checkio(data):
    an_list=[]
    dup_list=[]
    for d in data:
        if d in an_list:
            dup_list.append(d)
        else:
            an_list.append(d)
    lt=[x for x in data if x in dup_list]
    return lt

#function for password strength
def checkio(data):
    import re
    pass_len=len(data)
    if pass_len>=10:
        if any(x.isupper() for x in data) and any(x.islower() for x in data) and any(x.isdigit() for x in data):   
            print(data)
            return True
        #replace this for solution
    return False

#function for checking substring in from list
def count_words(text, words):
    words_list=list(words)
    contain_list=[]
    words_list=[x.lower() for x in words_list]
    input_str=text.split(" ")
    input_str=[x.lower() for x in input_str]
    print(input_str)
    print(words_list)
    for i in words_list:
        if text.lower().find(i)!=-1:
            contain_list.append(i)
    return len(contain_list)

#function for tic tac toe
def checkio(game_result):
    col1=[]
    col2=[]
    col3=[]
    win=''
    for r in game_result:
        col1.append(r[0])
        col2.append(r[1])
        col3.append(r[2])
    print(col1)
    print(col2)
    print(col3)
    if len(set(col1)) == 1 and col1[0]!='.':
        win=col1[0]
    elif len(set(col2)) == 1 and col2[0]!='.':
        win=col2[0]
    elif len(set(col3)) == 1 and col3[0]!='.':
        win=col3[0]
    elif (col1[0]==col2[1] and col2[1]==col3[2] and col1[0]!='.') or (col1[2]==col2[1] and col2[1]==col3[0] and col3[0]!='.'):
        win=col2[1]
    elif (col1[0]==col2[0] and col2[0]==col3[0] and col1[0]!='.'):
        win=col1[0]
    elif(col1[1]==col2[1] and col2[1]==col3[1] and col1[1]!='.'):
        win=col1[1]
    elif(col1[2]==col2[2] and col2[2]==col3[2] and col1[2]!='.'):
        win=col1[2]
    else:
        win='D'
    print(win)
    return win
