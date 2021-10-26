pilihan = int(input("pilih satuan suhu\n1. celcius\n2. fahrenheit\n3. kelvin\n4. reamur\nmasukkan pilihan: "))

#------------------------------------------------------------------------------------------------------------------------#

if pilihan == 1: 
    suhu = int(input("masukkan angka suhu dalam celcius: "))
    pilihan2 = int(input("pilih konversi\n1. Fahrenheit\n2. Kelvin\n3. Reamur\nMasukkan pilihan: "))
    if pilihan2 == 1: #C > F
        suhu2 = (suhu*9/5)+32
        print('Suhu (Celcius): ' + str(suhu) + '\nSuhu Konversi ke Fahrenheit: '+ str(suhu2) + ' F') 
    elif pilihan2 == 2: #C > K
        suhu2 = suhu+273.15
        print('Suhu (Celcius): ' + str(suhu) + '\nSuhu Konversi ke Kelvin: '+ str(suhu2) + ' K')
    elif pilihan2 == 3: #C > R
        suhu2 = 4/5*suhu
        print('Suhu (Celcius): ' + str(suhu) + '\nSuhu Konversi ke Reamur: '+ str(suhu2) + ' R')

#------------------------------------------------------------------------------------------------------------------------#

elif pilihan == 2: 
    suhu = int(input("masukkan angka suhu ke dalam fahrenheit: "))
    pilihan2 = int(input("pilih konversi\n1. Celcius\n2. Kelvin\n3. Reamur\nMasukkan pilihan: "))
    if pilihan2 == 1: #F > C
        suhu2 = (suhu - 32) * 5/9
        print('suhu (Fahrenheit): ' + str(suhu) + '\nSuhu Konversi ke Celcius: '+ str(suhu2) + ' C')
    elif pilihan2 == 2: #F > K
        suhu2 = (suhu - 32) * 5/9 + 273.15
        print('Suhu (Farenheit): ' + str(suhu) + '\nSuhu Konversi ke Kelvin: '+ str(suhu2) + ' K')
    elif pilihan2 == 3: #F > R
        suhu2 = 4/9 * (suhu - 32)
        print('Suhu (Fahrenheit): ' + str(suhu) + '\nSuhu Konversi ke Reamur: '+ str(suhu2) + ' R')

#------------------------------------------------------------------------------------------------------------------------#

elif pilihan == 3: 
    suhu = int(input("masukkan angka suhu ke dalam kelvin: "))
    pilihan2 = int(input("pilih konversi\n1. Celcius\n2. Fahrenheit\n3. Reamur\nMasukkan pilihan: "))
    if pilihan2 == 1: #K > C
        suhu2 = suhu-273.15
        print('suhu (Kelvin): ' + str(suhu) + '\nSuhu Konversi ke Celcius: '+ str(suhu2) + ' C')
    elif pilihan2 == 2: #K > F
        suhu2 = (suhu-273.15)*9/5+32
        print('Suhu (Kelvin): ' + str(suhu) + '\nSuhu Konversi ke Fahrenheit: '+ str(suhu2) + ' F')
    elif pilihan2 == 3: #K > R 
        suhu2 = 4/5*(suhu-273)
        print('Suhu (Kelvin): ' + str(suhu) + '\nSuhu Konversi ke Reamur: '+ str(suhu2) + ' R')

#------------------------------------------------------------------------------------------------------------------------#

elif pilihan == 4:
    suhu = int(input("masukkan angka suhu ke dalam reamur: "))
    pilihan2 = int(input("pilih konversi\n1. Celcius\n2. fahrenheit\n3. kelvin \nMasukkan pilihan: "))
    if pilihan2 == 1: #R > C
        suhu2 = (5/4)*suhu
        print('suhu (Reamur): ' + str(suhu) + '\nSuhu Konversi ke Celcius: '+ str(suhu2) + ' C')
    elif pilihan2 == 2: #R > F
        suhu2 = (9/4*suhu)+32
        print('Suhu (Reamur): ' + str(suhu) + '\nSuhu Konversi ke Fahrenheit: '+ str(suhu2) + ' F')
    elif pilihan2 == 3: #R > K 
        suhu2 = suhu+273
        print('Suhu (Reamur): ' + str(suhu) + '\nSuhu Konversi ke Kelvin: '+ str(suhu2) + ' K')
else:
    print("pilihan tidak valid")