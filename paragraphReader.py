def countWord(s):
    c = len(s.split())
    return c

def countSpace(str):
    count = 0;    
    for i in range (0, len (str)):   
        #Checks whether given character is a punctuation mark  
        if str[i] in ('', " "):  
            count = count + 1;  

    print ("Total number of Space  exists in string: ");  
    print (count);




def puctionCount(str):
    count = 0;
    punctions =[]
    for i in range (0, len (str)):   
        #Checks whether given character is a punctuation mark  
        if str[i] in ('!', "," ,"\'" ,";" ,"\"", ".", "-"  ,"?"):  
            count = count + 1;
            punctions.append(str[i])

    print ( f"Total number of punctuation characters exists in string: {count}  \n puctions =>  {punctions}");  
   
    
    
     


def puctionRemove(str):
    count = list(str)
    count1 = []
    punctions = []
    for i in range (0, len (str)):   
        #Checks whether given character is a punctuation mark  
        if count[i] not  in  ('!', "," ,"\'" ,";", ":" , ".", "-" ,"?" , "/" ,): 
            count1.append(count[i])
        else:
             punctions.append(count[i])
    str1 = ""
    for ele in count1:  
        str1 += ele
    print (f"\npunctuation characters   Removes  in string: {str1}  \n remove Punction is => {punctions} " ); 
    
    
    
    
def serc(para , wod , add):
    count=0
    p=''
    if wod in para:
        print("true")
        for i in range(0 , len(para)):
            if (para[i : len(wod)+i] == wod):
                p = para.replace(para[i : len(wod)+i] , f" {add} ")
                count = count + 1
    print(f"No OF {wod} in Paragrah is {count} \n ADD some string {add} instead of {wod} \nphara graph is {p}")
    