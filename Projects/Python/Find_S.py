import csv 
file_path ='Find_S_dataset.csv'
num_attributes = 6 
a = [] 
print("\n The Given Training Data Set \n") 
with open(file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        a.append (row)
        print(row) 
print("\n The initial value of hypothesis: ") 
hypothesis = ['0'] * num_attributes 
print(hypothesis) 
for j in range(0,num_attributes): 
    hypothesis[j] = a[0][j]; 
print("\n Find S: Finding a Maximally Specific Hypothesis\n") 
for i in range(0,len(a)):
    if a[i][num_attributes]=='yes':
        for j in range(0,num_attributes):
            if a[i][j]!=hypothesis[j]:
                hypothesis[j]='?'
            else :
                hypothesis[j]= a[i][j]
    print("For Training instance No:{0} the hypothesis is\n ".format(i),hypothesis) 
print("\nThe Maximally Specific Hypothesis for a given Training  Examples :\n") 
print(hypothesis)
