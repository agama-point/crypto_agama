from crypto_agama.cipher import fleissner_decrypt


f7_A = ((0,1),(0,4),(0,5),(1,2),(2,1),(2,4),(3,0),(3,4),(4,0),(5,1),(5,3),(6,6))
f7_a = ((0,3),(0,4),(1,0),(1,2),(1,5),(2,1),(3,5),(4,0),(4,2),(4,3),(5,0),(6,6)) # inverse
f7_B = ((0,1),(0,5),(1,2),(1,4),(2,3),(3,0),(3,1),(4,4),(4,6),(5,5),(6,4),(6,6))
f7_b = () #i
f7_C = ((0,2),(0,6),(1,0),(1,5),(2,4),(3,2),(3,6),(4,1),(4,5),(5,0),(5,3),(6,2))


t48 = "123456789012345678901234567890123456789012345678"
t48 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV"

print(fleissner_decrypt(t48, f=f7_A, ccw=True, center="A"))

print(fleissner_decrypt(t48, f=f7_B, ccw=True, center="B"))

print(fleissner_decrypt(t48, f=f7_C, ccw=True, center="C",debug=True))