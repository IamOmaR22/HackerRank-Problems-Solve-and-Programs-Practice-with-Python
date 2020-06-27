l = []
n=int(input())
for i in range(0,n):
    tmp_str=input()
    tmp_str_ar=tmp_str.strip().split(" ")
    cmd=tmp_str_ar[0]
    if(cmd=="print"):
        print(l)
    elif(cmd=="sort"):
        l.sort()
    elif(cmd=="reverse"):
        l.reverse()
    elif(cmd=="pop"):
        l.pop()
    elif(cmd=="count"):
        val=int(tmp_str_ar[1])
        l.count(val)
    elif(cmd=="index"):
        val=int(tmp_str_ar[1])
        l.index(val)
    elif(cmd=="remove"):
        val=int(tmp_str_ar[1])
        l.remove(val)  
    elif(cmd=="append"):
        val=int(tmp_str_ar[1])
        l.append(val)          
    elif(cmd=="insert"):
        pos=int(tmp_str_ar[1])
        val=int(tmp_str_ar[2])
        l.insert(pos,val)
