def przytnij(data, start, stop):
    result = []
    for element in data:
        if start(element):
            result.append(element)
        if stop(element):
            break
    return result
data=[1, 2, 3, 4, 5, 6, 7]
start=lambda x: x > 3
stop=lambda x: x == 6

# def test_przytnij():
#     assert przytnij(
#         data=[1, 2, 3, 4, 5, 6, 7],
#         start=lambda x: x > 3,
#         stop=lambda x: x == 6,

x = przytnij(data, start, stop)
print(x)