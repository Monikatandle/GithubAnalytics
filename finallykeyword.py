def function():
    try:
        l=[1,5,6,7]
        i=int(input('enter the index:'))
        print(l[i])
        return 1
    except:
        print('some error has occured')
        return 0
    finally:
        print('i am always executed')

x=function()
print(x)