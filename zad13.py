print('zad13')

ocena = int(input('podaj ocene\n'))

test = int(input('podeaj wynik tekstu kompetencji\n'))

if ocena >= 1 and ocena <= 6 and test >= 0 and test <= 100:
    if ocena >= 5 or test > 90:
        print('zaawansowana')
    else:
        print('podstawowa')
else:
    print('blende dan')