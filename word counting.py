def tokenize(lines): #def funktion
    words = []
    
    for line in lines: #gå igenom varje bokstav i lines
        start = 0
        end = start #ska visa vart början och slutet av order ligger

        while start < len(line): #när start är mindre än längden av texten ska den loopa igenom 
                if line[start].isalpha(): #när bokstaven start på line är en bokstav
                    end = start #sätter att end börjar på där start är vilket är 0 i början. Sen ökar end med längden av ordet. 
                    while end < len(line) and line[end].isalpha():
                         end += 1
                    words.append((line[start:end]).lower()) #Ordet läggs sedan till i listan med början start och slutet end.
                    start = end - 1
 
                elif line[start].isdigit():
                    end = start
                    while end < len(line) and line[end].isdigit():
                         end += 1 
                    words.append(line[start:end])
                    start = end - 1
                                    
                elif line[start].isspace(): # om det är whitespace hoppas den över
                     end = end + 1
                else: # Om det är specialtecken läggs endast det tecknet till
                    end = start + 1 
                    words.append(line[start:end])
                
                start = start + 1
        
    return words
