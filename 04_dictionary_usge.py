cell_delay = {"INV_X1": 0.1, "NAND2_X2": 0.25, "NOR2_X4": 0.3}

for cell, delay in cell_delay.items():
    print(f"{cell} --> {delay} ns")
    
