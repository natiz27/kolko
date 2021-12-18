# Gra kółko i krzyżyk

PlanszaDoGry = {'7':' ','8':' ','9':' ',
                '4':' ','5':' ','6':' ',
                '1':' ','2':' ','3':' '}

klawiszeGry=[]

for key in PlanszaDoGry:
    klawiszeGry.append(key)
    #print(klawiszeGry)
#print(klawiszeGry)


def drukujPlansze(pole):
    print(f"{pole['7']}|{pole['8']}|{pole['9']}")
    print('-+-+-')
    print(f"{pole['4']}|{pole['5']}|{pole['6']}")
    print('-+-+-')
    print(f"{pole['1']}|{pole['2']}|{pole['3']}")

drukujPlansze(PlanszaDoGry)