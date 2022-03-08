# Initial values of alpha and beta
MIN = -99999
MAX = 99999

# Function to calculate the best move using alpha and beta pruning
def alphaBetaPruning(depth, nodeIndex, maxTurn, values, alpha, beta):
    if(depth==3):
        return values[nodeIndex]
    if(maxTurn):
        bestVal = MIN
        for i in range(2):
            value = alphaBetaPruning(depth+1,nodeIndex*2+i,False,values,alpha,beta)
            bestVal = max(bestVal,value)
            alpha = max(alpha,bestVal)
            if(beta<=alpha):
                break
        return bestVal
    else:
        bestVal = MAX
        for i in range(0,2):
            value = alphaBetaPruning(depth+1,nodeIndex*2+i,True,values,alpha,beta)
            bestVal = min(bestVal,value)
            beta = min(beta,bestVal)
            if(beta<=alpha):
                break
        return bestVal

# Main Function
if __name__ == "__main__":
  
    values = [3, 5, 6, 9, 1, 2, 0, -1] 
    print("The optimal value is :", alphaBetaPruning(0, 0, True, values, MIN, MAX))
