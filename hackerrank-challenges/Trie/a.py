def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):
    
    opt = [[0 for _ in xrange(len(forwardRouteList))] for _ in xrange(len(returnRouteList))]
    min_value = 7000
    for i in xrange(len(returnRouteList)):
        for j in xrange(len(forwardRouteList)):
            opt[i][j] = forwardRouteList[j] + returnRouteList[i]
    print opt


    

    
# for i in range(len(forwardRouteList)):
#     for j in range(len(returnRouteList)):


maxTravelDist = 7000
forwardRouteList = [[1, 2000], [2, 4000], [3, 6000]]
returnRouteList = [[1, 2000]]

print optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList)