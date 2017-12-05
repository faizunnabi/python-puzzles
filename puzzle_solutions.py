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
