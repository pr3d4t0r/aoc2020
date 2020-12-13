# https://python-minifier.com/
M=print
C=len
from util import mainStart as F
B=7
D=127
def G(fileName):return[A for A in open(fileName,'r').read().split('\n')if C(A)]
def A(data,head):
	A=head;B=0;C=0;D=0
	while B<A:
		D=int((A+B)/2)
		if data[C]=='F'or data[C]=='L':A=D
		else:B=D+1
		C+=1
	return A
def E(boardingPass):return A(boardingPass[:7],D)
def H(boardingPass):return A(boardingPass[-3:],B)
def I(boardingPass):A=boardingPass;B=E(A);C=H(A);return B,C,8*B+C
def J(boardingPasses):
	A=-1;C=list()
	for D in boardingPasses:
		E,E,B=I(D);C.append(B)
		if B>A:A=B
	return A,sorted(C)
def K(seatIDs):
	A=seatIDs;D=A[0]
	for B in range(A[0],C(A)):
		E=A[B-D]
		if B!=E:return B
def L(fileName=None):A=fileName;A=F(A,5);H=G(A);B,D=J(H);E=K(D)if C(D)>100 else 0;M('maxID = %d'%B);M('My seat = %d'%E);return B,E
if'__main__'==__name__:L()
