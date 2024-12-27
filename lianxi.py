def find_number():
    number = (str(i) for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0)
    print(','.join(number))
if __name__ =='__main__':
    find_number()
