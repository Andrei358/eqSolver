class eqSolver:

    def __init__(self):
        self.m=0
        self.n=0
        self.a=[]
        self.b=[]
        self.pivot=[]
        self.sol=[]
        self.sol1=[]
        self.freev=[]
        self.freez=0

    def get_sys(self, fileName):
        with open(fileName) as f:
            inn=f.read().split()
            self.m, self.n = int(inn[0]), int(inn[1])
            k=2
            for i in range(self.m):
                self.a.append([])
                for j in range(self.n):
                    self.a[i].append(float(inn[k]))
                    k+=1
                self.b.append(float(inn[k]))
                k+=1

    def substract(self,i, j, q):
        multi=-self.a[i][q]/self.a[j][q]
        for col in range(q+1):
            self.a[i][col]=0
        for col in range(q+1,self.n):
            self.a[i][col]+=multi*self.a[j][col]
        self.b[i]+=multi*self.b[j]

    def flip_row(self,i,j):
        for col in range(self.n):
            self.a[i][col],self.a[j][col]=self.a[j][col],self.a[i][col]
        self.b[i],self.b[j]=self.b[j],self.b[i]

    def first_col(self,i,j):
        for ii in range(i,self.m):
            if self.a[ii][j]:
                return ii
        return None

    def first_e(self):
        i, j = 0, 0
        self.pivot=[None] * self.m

        while i<self.m and j<self.n:
            tt=self.first_col(i,j)
            if tt!=None:
                self.flip_row(i,tt)
                self.pivot[i]=j
                for ii in range(i+1,self.m):
                    self.substract(ii,i,j)
                i+=1
            j+=1

    def solve(self):
        self.first_e()
        self.freev=[-1]*self.n
        for i in range(self.n):
            self.sol.append([])
            self.sol1.append([])
            for j in range(self.n+1):
                self.sol[i].append(0)
                self.sol1[i].append(0)
        for i in range(self.m-1,-1,-1):
            if self.pivot[i]==None and self.b[i]!=0:
                print("\nThe system is unsolvable!")
                break
            if self.pivot[i]==None:
                continue
            j=self.pivot[i]
            self.freev[j]=0
            jj=self.a[i][j]
            self.sol[j][self.n]=self.b[i]/jj
            for k in range(j+1,self.n):
                self.sol[j][k]=-1*self.a[i][k]/jj
                if self.a[i][k] and self.freev[k]==-1:
                    self.freev[k]=1
                    self.freez=1
        for i in range(self.n-1,-1,-1):
            self.sol1[i][self.n]=self.sol[i][self.n]
            for j in range(i+1,self.n):
                if self.freev[j]==1:
                    self.sol1[i][j]+=self.sol[i][j]
                elif not self.freev[j]:
                    for k in range(j+1,self.n+1):
                        self.sol1[i][k]+=self.sol[i][j]*self.sol1[j][k]

    def print_sol(self):
        print('')
        if self.freez:
            print("free variables: ", end='')
            for i in range(self.n):
                if self.freev[i]:
                    print("v{0:d} ".format(i+1), end='')
            print('')
        for i in range(self.n):
            if not self.freev[i]:
                print("v{0:d} = ".format(i+1), end='')
                first=1
                for j in range(i+1,self.n):
                    if self.sol1[i][j]:
                        if self.sol1[i][j]<0:
                            print("-",end='')
                            if not first:
                                print(" ",end='')
                        elif not first:
                            print("+ ",end='')
                        print("{0:.3f} * v{1:d} ".format(abs(self.sol1[i][j]),j+1), end='')
                        first=0
                if self.sol1[i][self.n]<0:
                    print("-",end='')
                    if not first:
                        print(" ",end='')
                if not first and self.sol1[i][self.n]>0:
                    print("+ ",end='')
                if self.sol1[i][self.n]!=0:
                    print(abs(self.sol1[i][self.n]),end='')
                print('')
        print('')
