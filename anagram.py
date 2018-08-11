n = int(input())

for i in range(n):
    str1 = input()
    str2 = input()
    num_remove_str1 = num_remove_str2 = 0
    

    for l in set(str1):
        if l not in str2:
            num_remove_str1 += str1.count(l)
            continue
            
        if str1.count(l) > str2.count(l):
            num_remove_str1 += str1.count(l) - str2.count(l)
            
        if str1.count(l) < str2.count(l):
            num_remove_str2 += str2.count(l) - str1.count(l)
            
    for l in set(str2):
        if l not in str1:
            num_remove_str2 += str2.count(l)
            
    print(str(num_remove_str1+num_remove_str2))
  