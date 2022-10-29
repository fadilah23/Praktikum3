# penggunaan end
print('A', end='')
print('B', end='')
print('C', end='')
print()
print('X')
print('Y')
print('Z')

print("========================================================")

# penggunaan separator
w, x, y, z = 10, 15, 20, 25
print(w, x, y, z)
print(w, x, y, z, sep=',')
print(w, x, y, z, sep='')
print(w, x, y, z, sep=':')
print(w, x, y, z, sep='------')

print("========================================================")

# Sting format
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**6)
print(7, 10**7)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)

print("========================================================")

# Sting format
print('{0:>3} {1:>16}'.format(0, 10**0))
print('{0:>3} {1:>16}'.format(1, 10**1))
print('{0:>3} {1:>16}'.format(2, 10**2))
print('{0:>3} {1:>16}'.format(3, 10**3))
print('{0:>3} {1:>16}'.format(4, 10**4))
print('{0:>3} {1:>16}'.format(5, 10**5))
print('{0:>3} {1:>16}'.format(6, 10**6))
print('{0:>3} {1:>16}'.format(7, 10**7))
print('{0:>3} {1:>16}'.format(8, 10**8))
print('{0:>3} {1:>16}'.format(9, 10**9))
print('{0:>3} {1:>16}'.format(10, 10**10))

print("========================================================")
a=input("masukan nilai a:")
b=input("masukan nilai b:")
print("variable a=" ,a)
print("variable b= ,b")
print("hasil penggabungan {1}&{0}=%s" .format(a,b) %(a+b))

# Konversi nilai variable
a=int(a)
b=int(b)
print("hasil penjumlahan {1}+{0}=%s" .format(a,b) %(a+b))
print("hasil pembagian {1}/{0}=%s" .format(a,b) %(a/b))

print("========================================================")
print("      Ini adalah Script Python")
print("-------------------------------------")
print('{0:>16}' .format('*'))
print('{0:>17}'.format('***'))
print('{0:>18}'.format('*****'))
print('{0:>19}'.format('*******'))
print('{0:>20}'.format('*********'))
print('{0:>19}'.format('*******'))
print('{0:>18}'.format('*****'))
print('{0:>17}'.format('***'))
print('{0:>16}'.format('*'))

