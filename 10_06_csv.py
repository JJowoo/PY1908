# CSV : Comma Separated Values
# TSV : Tab Separated Values

with open("data/climate.csv", "r") as f:
    f.readline()   # 첫번째 line 은 pass
    result = []
    for line in f:
        result.append(line.split(","))
    print(result)
