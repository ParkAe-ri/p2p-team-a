from math_function import add,root,max_num


def main():

    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    if operator == "+":
        result = add(data_1, data_2)
        
    print("{} {} {} = {} ".format(data_1, operator, data_2, result))

    if operator == "^":
        result = root(data_1,data_2)
    print("Result for {} root {} is {}".format(data_1,data_2,result))

    if operator == ">":
        result = max_num(data_1,data_2)
        print("{} is the max number".format(result))


if __name__ == "__main__":
    print("Hello Main !")
    main()