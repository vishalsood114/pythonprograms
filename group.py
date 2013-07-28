def group(x,s):
    return [x[i:i+s] for i in range(0,len(x),s)]
    #result = []
    #for i in range(0,len(x),s):
    #    result.append(x[i:i+s])

    #return result
    

print group(range(1,10),4)
    
