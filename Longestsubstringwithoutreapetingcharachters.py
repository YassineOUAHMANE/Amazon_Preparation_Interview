def longestsubstring(s:str)-> int :
    if not s:
        return 0
    if len(s) == 1:
        return 1
    start = 0 
    max_length = 0 
    element_visited = {}
    for i,el in enumerate(s):
        if el in element_visited and element_visited[el] >= start:
            start = element_visited[el] + 1 
        element_visited[el] = i
        max_length = max(max_length,i-start+1)
    return max_length
            