import collections, sys

if len(sys.argv) > 1:
    cents = sys.argv[1]
else:
    print ("please input coin amount")


def num_coins(cents):

    if cents <= 0:
        return 0
        
    coins = [25, 10, 1]
    
    queue = collections.deque()
    
    queue.append((cents, 0))
    
    while queue:
        
        temp, num_used = queue.popleft()
        
        for coin in coins:
            if temp - coin == 0:
                return num_used + 1
            elif temp - coin > 0:
                queue.append((temp - coin, num_used + 1))   
    
    return -1

def num_coins_dp(cents):
    if cents <= 0:
        return 0
     
    coins = [25, 10, 1]
    dp = [0 for i in range(cents + 1)]
    
    for this_cent in range(1, cents + 1):
        
        for coin in coins:
            if this_cent - coin == 0:
                dp[coin] = 1
            
            elif this_cent - coin > 0 and dp[this_cent - coin] != 0:
                dp[this_cent] = min(dp[this_cent], dp[this_cent - coin] + 1) if dp[this_cent] > 0 else dp[this_cent - coin] + 1

    return dp[cents]
    


try:
    cents = int(cents)  
    print ("minimum number of coins for {} is {}".format(cents, num_coins(cents)))
    print ("minimum number of coins for {} using dp is {}".format(cents, num_coins_dp(cents)))
    
except:
    print ("invalid input")
