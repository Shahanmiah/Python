def main():
    def n23(b):# a = initial number
        c = 0
        l = [b]
        while b != 1:
            if b % 2 == 0:#if even divide it by 2
                b = b // 2
            elif b % 2 == 1:#if odd 3n+1
                b = 3*b +1
            c += 1#counter
            l += [b]

        return l , c
    print(n23(43))
    print(n23(98)[0][-1])# = a
    print("It took {0} steps.".format(n23(13)[1]))#optional finish

if __name__ == '__main__':
    main()
