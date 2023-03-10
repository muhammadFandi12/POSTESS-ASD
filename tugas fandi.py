arrr =["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
def linearsearch(arrr,x):
    for l in range(len(arrr)):
        if type(arrr[l]) == list:
            hasil_x = linearsearch(arrr[l],x)
            if hasil_x == -1:
                return -1
            else:
                print(f'{x} ditemukan pada indeks {l} kolom {hasil_x}')
                exit()
        elif arrr[l] == x:
            return l
    return -1


def jumpSearch (var, target , length) :
    stepp = length**0.5
    prev = 0
    for T in range(len(var)):
        if type(var[T]) == list:
            hasil_g = jumpSearch (var[int(T)],target,len(var[int(T)]))
            if hasil_g == -1:
                var[int(T)]="berhasil"
            else:
                print(target ,"ditemukan pada indeks", int(T) , "kolom", hasil_g)
                exit()


    while var[int (min(stepp, length) -1)] < target:
        prev = stepp
        stepp += length**0.5 
        if (prev >= length) :
            return -1
        
    while var[int (prev)]< target:
        prev += 1
        if prev == min(stepp, length) :
            return -1
    if var[int(prev)]== target:
        return int(prev)
    return -1




while True:
    print("|=================|")
    print("| 1. linearsearch |")
    print("| 2. jumpSearch   |")
    print("|=================|")

    pilih = input("masukan no yang anda inginkan :")

    if pilih == "1" :
        print(arrr)
        x = input('Masukan nama : ')
        hasil_y = linearsearch(arrr,x)
        if hasil_y == -1:
            print(f'{x} ditemukan pada indeks {hasil_y}')
        else:
            print(f'{x} ditemukan pada indeks {hasil_y}')
        exit()

    elif pilih == "2" :
        print(arrr)
        length = len(arrr)
        
        target = str(input("masukan nama :"))
        hasil_x = jumpSearch(arrr,target, length)
        if hasil_x == -1:
            print(target, 'tidak ada')
        else:
            print(target,'ada di indeks ke',hasil_x)
        exit()