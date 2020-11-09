# !curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt

fd = open("elements1_20.txt", 'r')

elems = []
line = " "
while line:
    line = fd.readline().strip()
    elems.append(line.split('\n')[0])
print(elems)

tf = []
for i in range(20):
    tf.append(False)

result = []
not_result = []

def get_names():
    print("list any 5 of the first 20 elements in the Period table")
    cnt = 0
    while(cnt < 5):
        my_input = input("Enter the name of an element: ")
        flag = False
        for i in range(20):
            if (elems[i].lower() == my_input.lower()) and (tf[i] == False):
                tf[i] = True
                result.append(my_input.capitalize())
                flag = True
                break
            elif (elems[i].lower() == my_input.lower()) and (tf[i] == True):
                print(my_input + " was already entered          <--no duplicates allowed")
                cnt -= 1
                flag = True
                break
        if flag == False:
            not_result.append(my_input.capitalize())
        cnt += 1
    return len(not_result)

print()
print(str(100 - (get_names() * 20)) + " % correct")
str1 = "Found:"
for i in range(len(result)):
    str1 += (' ' + result[i])
str2 = "Not Found:"
for i in range(len(not_result)):
    str2 += (' ' + not_result[i])
print(str1)
print(str2)
