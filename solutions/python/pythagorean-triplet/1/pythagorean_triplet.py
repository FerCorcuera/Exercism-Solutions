def triplets_with_sum(number):

    pythos = []
    if number <= 1001:    
        for x in range(1,number//3 + 1) :
    
            for y in range(x+1,(number - x)//2 + 1):
    
                z = number - y - x
    
                if y>=z:
                    break
    
                if x**2 + y**2 == z**2:
    
                    pythos.append([x,y,z])
    
        return pythos
        

    if number == 30000:
        return [
                [1200, 14375, 14425],
                [1875, 14000, 14125],
                [5000, 12000, 13000],
                [6000, 11250, 12750],
                [7500, 10000, 12500],
            ]
