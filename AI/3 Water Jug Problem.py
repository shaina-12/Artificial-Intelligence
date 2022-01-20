# implementation of 3 water jug problem
ans = []
from collections import defaultdict
def jugs(j1,j2,j3,mj1,mj2,mj3,fj1,fj2,fj3,vis):
    # if goal state is reached
    if(j1==fj1 and j2==fj2 and j3==fj3):
        ans.append((j1,j2,j3))
        return True
    # if the current state is already visited
    if((j1,j2,j3) in vis):
        return False
    vis[(j1,j2,j3)] = True
    # empty jug 1
    if(j1>0):
        # empty jug 1 into jug 2
        if(j1+j2<=mj2):
            if(jugs(0,j1+j2,j3,mj1,mj2,mj3,fj1,fj2,fj3,vis)):
                ans.append((j1,j2,j3))
                return True
        else:
            if(jugs(j1-(mj2-j2),mj2,j3,mj1,mj2,mj3,fj1,fj2,fj3,vis)):
                ans.append((j1,j2,j3))
                return True
        # empty jug 1 into jug 3
        if(j1+j3<=mj3):
            if(jugs(0,j2,j1+j3,mj1,mj2,mj3,fj1,fj2,fj3,vis)):
                ans.append((j1,j2,j3))
                return True
        else:
            if(jugs(j1-(mj3-j3),j2,mj3,mj1,mj2,mj3,fj1,fj2,fj3,vis)):
                ans.append((j1,j2,j3))
                return True
    # empty jug 2
    if(j2>0):
        # empty jug 2 into jug 1
        if(j1+j2<=mj1):
            if(jugs(j1+j2,0,j3,mj1,mj2,mj3,fj1,fj2,fj3,vis)):
                ans.append((j1,j2,j3))
                return True
        else:
            if(jugs(mj1,j2-(mj1-j1),j3,mj1,mj2,mj3,fj1,fj2,fj3,vis)):
                ans.append((j1,j2,j3))
                return True
        # empty jug 2 into jug 3
        if(j2+j3<=mj3):
            if(jugs(j1,0,j2+j3,mj1,mj2,mj3,fj1,fj2,fj3,vis)):
                ans.append((j1,j2,j3))
                return True
        else:
            if(jugs(j1,j2-(mj3-j3),mj3,mj1,mj2,mj3,fj1,fj2,fj3,vis)):
                ans.append((j1,j2,j3))
                return True
    # empty jug 3
    if(j3>0):
        # empty jug 3 into jug 1
        if(j1+j3<=mj1):
            if(jugs(j1+j3,j2,0,mj1,mj2,mj3,fj1,fj2,fj3,vis)):
                ans.append((j1,j2,j3))
                return True
        else:
            if(jugs(mj1,j2,j3-(mj1-j1),mj1,mj2,mj3,fj1,fj2,fj3,vis)):
                ans.append((j1,j2,j3))
                return True
        # empty jug 3 inot jug 2
        if(j2+j3<=mj2):
            if(jugs(j1,j2+j3,0,mj1,mj2,mj3,fj1,fj2,fj3,vis)):
                ans.append((j1,j2,j3))
                return True
        else:
            if(jugs(j1,mj2,j3-(mj2-j2),mj1,mj2,mj3,fj1,fj2,fj3,vis)):
                ans.append((j1,j2,j3))
                return True
    return False
def main():
   mj1, mj2, mj3 = tuple(map(int,input('Enter the maximum capacity of jug 1, jug 2 and jug 3: ').split()))
   j1, j2, j3 = tuple(map(int,input('Enter the initial capacity of jug 1, jug 2 and jug 3: ').split()))
   fj1, fj2, fj3 = tuple(map(int,input('Enter the final capacity of jug 1, jug 2 and jug 3: ').split()))
   vis = defaultdict(lambda: False)
   print('Jug1\tJug2\tJug3')
   jugs(j1,j2,j3,mj1,mj2,mj3,fj1,fj2,fj3,vis)
   ans.reverse()
   for i in range(len(ans)):
       print(str(ans[i][0])+'\t'+str(ans[i][1])+'\t'+str(ans[i][2]))
if __name__=="__main__":
    main()
