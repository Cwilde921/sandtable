import math

def heuristic(pos, orig, dest, safe_mode=True):
    p = to_lst(pos)
    o = to_lst(orig)
    d = to_lst(dest)

    multiplier = 1
    if safe_mode:
        if ( pos['r'] < 0 ): multiplier += ( abs(pos['r']) * 3 )
        if ( pos['r'] > 1 ): multiplier += ( (pos['r'] -1) * 3 )

    return ( dist(p, p) + line_dist(p, o, d) ) * multiplier

def simple_heuristic(pos, dest, safe_mode=True):
    p = to_lst(pos)
    d = to_lst(dest)
    # print(p)

    multiplier = 1
    if safe_mode:
        if ( pos['r'] < 0 ): multiplier += ( abs(pos['r']) * 3 )
        if ( pos['r'] > 1 ): multiplier += ( (pos['r'] -1) * 3 )


    res = dist(p, p) * multiplier
    # print("multiplier", multiplier)
    # print("results", res)
    return res

def to_lst(obj):
    if type(obj) == list:
        return obj
    if 'th' in obj:
        return [obj['th'], obj['r']]
    if 'x' in obj:
        return [obj['x'], obj['y']]

def to_polar(lst):
    if type(lst) == dict:
        return lst
    return {
        'th': lst[0],
        'r': lst[1],
    }

def to_cartesian(lst):
    if type(lst) == dict:
        return lst
    return {
        'x': lst[0],
        'y': lst[1],
    }

def dist(p1, p2):
    d_x = p2[0] - p1[0]
    d_y = p2[1] - p1[1]
    print(p1)
    res = math.sqrt( math.pow(d_x, 2) + math.pow(d_y, 2) )
    print(res)
    return res
    
# Function to return the minimum distance
# between a line segment AB and a point E
def line_dist(E, A, B) :
    # vector AB
    AB = [None, None];
    AB[0] = B[0] - A[0];
    AB[1] = B[1] - A[1];
    # vector BP
    BE = [None, None];
    BE[0] = E[0] - B[0];
    BE[1] = E[1] - B[1];
    # vector AP
    AE = [None, None];
    AE[0] = E[0] - A[0];
    AE[1] = E[1] - A[1];
    # Variables to store dot product
    # Calculating the dot product
    AB_BE = AB[0] * BE[0] + AB[1] * BE[1];
    AB_AE = AB[0] * AE[0] + AB[1] * AE[1];
    # Minimum distance from
    # point E to the line segment
    reqAns = 0;
    if (AB_BE > 0) :
        # Finding the magnitude
        y = E[1] - B[1];
        x = E[0] - B[0];
        reqAns = math.sqrt(x * x + y * y);
    elif (AB_AE < 0) :
        y = E[1] - A[1];
        x = E[0] - A[0];
        reqAns = math.sqrt(x * x + y * y);
    else:
        # Finding the perpendicular distance
        x1 = AB[0];
        y1 = AB[1];
        x2 = AE[0];
        y2 = AE[1];
        mod = math.sqrt(x1 * x1 + y1 * y1);
        reqAns = abs(x1 * y2 - y1 * x2) / mod;
    return reqAns;
 
# Driver code
if __name__ == "__main__" :
 
    A = [0, 0];
    B = [2, 0];
    E = [4, 0];
 
    print(line_dist(A, B, E));
 
