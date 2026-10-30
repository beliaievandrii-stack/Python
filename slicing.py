all_lists = []
for i in range(6):
    inner_list = [] 
    for j in range(10):
        inner_list.append(j)
    all_lists.append(inner_list)  
    print(all_lists[i]) 

i = int(input("Welche List möchten Sie ändern" + "\n"))
j = int(input("Welches Zahl möchten Sie ändern" + "\n"))
all_lists[i][j] = int(input("Geben Sie einen Wert ein" + "\n"))  

for i in range(6):
        print(all_lists[i]) 