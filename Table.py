def generatetable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"
    
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2, 101):
    generatetable(i)
#code by salman
#github = numaan28
