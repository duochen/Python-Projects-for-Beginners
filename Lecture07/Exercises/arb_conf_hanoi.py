def hanoi(n,t):
        if n>0:
                f=pos[n-1]
                if f!=t:
                        w=[i for i in ['A','B','C'] if i!=f and i!=t][0]
                        hanoi(n-1,w)
                        pos[n-1]=t
                        print(f'move disk {n-1} to peg {t}',end='\t')
                        print(pos)
                hanoi(n-1,t)
pos=['C','A','C','B','B','A']
hanoi(6,'C')
