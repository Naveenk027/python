list1= [10,20,30,40,50,60]

mx=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
    if list1[i]>mx:
        secondmax=mx
        mx=list[i]
   elif list1[i]>secondmax and \mx !=list1[i]:
                secondmax=list1[i]

                print("second highest number is :",\
                      str(secondmax))
                
