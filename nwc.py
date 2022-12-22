import json
import random


### solving transportation problem using north west corner method
### note that the supply and demand must be equal
### note that the data is generated randomly so for the same supply and demand the data will be different
### feel free to change the data to your own data

def north_west_corner(demand,supply):
    ### generating the data randomly
    data=[]
    for i in range(len(supply)):
        data.append([])
        for row in demand:
            data[i].append(random.randint(1,10))
    
    ### solving the problem
    
    i,j,i_supply,i_demand=0,0,0,0
    solution={}
    while i < len(supply)  and j <len(demand) and  i_demand < len(demand) and i_supply<len(supply) and sum(demand)!=0 and sum(supply)!=0:

        if demand[i_demand] > supply[i_supply]:
            solution[f"O{i+1},R{j+1}"]=(data[i][j],supply[i_supply])
            demand[i_demand]-=supply[i_supply]
            supply[i_supply]=0
            i_supply+=1
            i+=1
        elif demand[i_demand] < supply[i_supply]:
            solution[f"O{i+1},R{j+1}"]=(data[i][j],demand[i_demand])
            supply[i_supply]-=demand[i_demand]
            demand[i_demand]=0
            i_demand+=1
            j+=1
        else:
            solution[f"O{i+1},R{j+1}"]=(data[i][j],demand[i_demand])
            supply[i_supply]=0
            demand[i_demand]=0
            i_supply ,i_demand = i_supply+1,i_demand+1
            i,j=i+1,j+1
            
    return data,solution

    


### pirnting the matrice of norht west corner method to visualize the data
def print_matrice(data):
    print("|  |",end="")
    for i in range(len(data[0])):
        print(f"|O{i+1}|",end="")
    print()
    for i in range(len(data)):
        print(f"|R{i+1}|",end="")
        for j in range(len(data[i])):
            if len(str(data[i][j]))==1:
                print(f"|{data[i][j]} |",end="")
            else:
                print(f"|{data[i][j]}|",end="")
        print()

### getting the cost of the solution
def getCost(solution):
    cost=0
    for key in solution:
        cost+=solution[key][0]*solution[key][1]
    return cost
    
supply=[50,75,25]  
demand=[20,20,50,60]
data,solution=north_west_corner(demand.copy(),supply.copy())
print_matrice(data)
print(f"supply: {supply}")
print(f"demand: {demand}")
print(solution)
print(f"the cost of the solution is {getCost(solution)}")