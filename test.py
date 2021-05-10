import pyhash

bit_vector = [0] * 20

#Non_Cryptographic hash Functions(Murmur and FNV)

fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()


#Calculate the Output of FNV and Murmur Hash Functions for Pikachu and Charmander

fnv_pika = fnv("Pikachu") % 20
fnv_char = fnv("Charmander") % 20

murmur_pika = murmur("Pikachu") % 20
murmur_char = murmur("Charmander") % 20


print("fnv_pika")
print("fnv_char")
print("murmur_pika")
print("murmur_char")

 




