#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def rle_encode(data):
    encoding = '' 
    prev_char = ''
    count = 1 
    if not data: 
        return ''
    for char in data:  
        if char != prev_char: 
            if prev_char:
                encoding += str(count) + prev_char 
            count = 1
            prev_char = char 
        else:
            count += 1 
    else:
            encoding += str(count) + prev_char 
    return encoding

with open("f1.txt","r") as file1:
    f1=file1.read().strip()

with open("f2.txt","w") as file2:
    file2.write(rle_encode(f1))

print(rle_encode(f1))