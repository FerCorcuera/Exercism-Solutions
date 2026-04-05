def commands(binary_str):
    actions = ['wink','double blink','close your eyes','jump','Reverse']
    
    final_actions = []
    
    for x in range(0,len(binary_str)):
        if binary_str[-(x+1)] == '1':
            final_actions.append(actions[x])

    if 'Reverse' in final_actions:
        final_actions.remove('Reverse')
        final_actions.reverse()
    return final_actions