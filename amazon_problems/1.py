# Reorder Data in Log files

# the goal is to first separate both letter logs and digit logs
# then sort the letter logs based on the content of the logs
# if the content in letter logs is same then sort based on the identifier
# digit logs maintain their original order
# then combine both letter and digit logs and return the result

# Time complexity: O(nlogn) where n is the number of logs
# Space complexity: O(n)



def reorderLogs(logs):
    letter_logs = []
    digit_logs = []
    
    for log in logs:
        # split the log at first space
        # if the second part is a digit then it is a digit log
        # else it is a letter log
        if log.split()[1].isdigit(): 
            digit_logs.append(log)
        else:
            letter_logs.append(log)
            
            
    # sort letter_logs by content first, hence index 1, then by identifier, hence index 0
    letter_logs.sort(key=lambda log: (log.split(' ',1)[1], log.split(' ',1)[0]))
    
    return letter_logs + digit_logs
    
# output = ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']