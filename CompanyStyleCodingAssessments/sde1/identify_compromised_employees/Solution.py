#The following code only passed 7/15 test cases.
def findBreachedEmployees(modifiedUnits, accessRights):
    n = len(accessRights)
    m = len(accessRights[0])
    
    # Convert modified units to 0-based set
    modified = set(u - 1 for u in modifiedUnits)
    
    # Count how many employees access each storage unit
    access_count = [0] * m
    for i in range(n):
        for j in range(m):
            if accessRights[i][j] == '1':
                access_count[j] += 1
    
    compromised = []
    
    for i in range(n):
        accessed_units = [j for j in range(m) if accessRights[i][j] == '1']
        
        # Condition 1: all accessed units must be modified
        if not accessed_units:
            continue
        
        if any(j not in modified for j in accessed_units):
            continue
        
        # Condition 2: at least one uniquely accessed modified unit
        unique_found = False
        for j in accessed_units:
            if j in modified and access_count[j] == 1:
                unique_found = True
                break
        
        if unique_found:
            compromised.append(i + 1)  # Convert back to 1-based ID
    
    return compromised if compromised else [-1]
