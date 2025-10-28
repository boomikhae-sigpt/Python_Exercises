total_area = 0.0
with open("C:\Users\dell\Desktop\CAD\DEMO\util.rpt") as f:
    for line in f:
        if "Area" in line:
            area = float(line.split()[-1])
            total_area += area

print("Total Area:", total_area)
