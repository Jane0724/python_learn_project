#找出2000到3200中可以被7整除而不能被5整除的数并将其以‘，’连接起来
def find_number():
    number = (str(i) for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0)
    print(','.join(number))
if __name__ =='__main__':
    find_number()
