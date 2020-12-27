#!/usr/bin/env Python3
def Array_Intersection(a1,a2):
	if(len(a1)>len(a2)):
	    new=[]
	    for i in range(len(a1)):
		    if a1[i] in a2:
			    new.append(a1[i])
			    
			    
	    return new
	else:
	    new=[]
        for i in range(len(a2)):
            if a2[i] in a1:
                new.append(a2[i])
			    
			    
	    return new

print(Array_Intersection([1,2,3,4],[2,4,5,6,7]))