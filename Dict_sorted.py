import operator
Dict={"Hello":56,"at":26,"XxX":99,"utest":43,"this":43}
print(Dict)
sorted_x=sorted(Dict.items(),key=operator.itemgetter(1))
print(sorted_x)
sorted_y=sorted(Dict.items(),key=operator.itemgetter(1),reverse=True)
print(sorted_y)

