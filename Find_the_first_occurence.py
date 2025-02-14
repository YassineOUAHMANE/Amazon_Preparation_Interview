def find(string,substring):
    p1 = 0
    p2 = 0 
    last = len(substring) - 1
    while p1 < len(string) :
        if string[p1] == substring[p2]:
            if p2 == last:
                return p1 - last
            p1+=1
            p2+=1
        else:
            p1 = p1  - p2 + 1
            p2 = 0
    return -1            