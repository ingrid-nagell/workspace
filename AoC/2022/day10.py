# ptI
data_path = "AoC\\2022\\test.txt"
data_path = "AoC\\2022\\input10.txt"
input = [line.strip().split(" ") for line in open(data_path, 'r')]

def signal_strength(cycles):
    if cycles < 221 and cycles % 40 == 20 or cycles == 20:
        return True

cycles = 0
x = 1
sum = 0

for l in input:
    cycles += 1
    if signal_strength(cycles):
        sum += cycles*x
    if l[0]=="addx":
        cycles += 1
        if signal_strength(cycles):
            sum += cycles*x
        x += int(l[1])

print(sum)

# ptII
def run_cycle(cycles, cpu_position, sprite_position, cpu_row, cpu_image):      
    if cpu_position in sprite_position:
        cpu_row += "#"
    else:
        cpu_row += "."
            
    if cycles % 40 == 0:
        cpu_image += "\n" + cpu_row
        cpu_row = ""
        cpu_position = 0
    else:
        cpu_position += 1 
    
    cycles += 1

    return cycles, cpu_position, sprite_position, cpu_row, cpu_image
    

def ptII():
    cycles = 1
    x = 1
    cpu_position = 0
    cpu_row = ""
    cpu_image = ""
    
    for l in input:
        sprite_position = [x-1, x, x+1]
        cycles, cpu_position, sprite_position, cpu_row, cpu_image = run_cycle(cycles, cpu_position, sprite_position, cpu_row, cpu_image)

        if l[0]=="addx":
            cycles, cpu_position, sprite_position, cpu_row, cpu_image = run_cycle(cycles, cpu_position, sprite_position, cpu_row, cpu_image)
            x += int(l[1])

    print(cpu_image)


if __name__ == "__main__":
    ptII()