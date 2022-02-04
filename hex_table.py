from pathlib import Path
import sys
if __name__ == "__main__":
    file_name = ""
    if not len(sys.argv) > 1:
        file_name = input("PATH> ")
        if not Path(file_name).exists():
            raise "This file dose not exist!"
    else:
        file_name = sys.argv[1]
    with open(file_name, 'rb') as f:
        spacing = 6
        front_spacing = 10
        end_spcing = 0
        l = 0
        line_rep = ""
        print("LINE", " "*(front_spacing-4), "|", (" "*(spacing-1)).join(['0', '1', '2', '3' , '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']), " "*((spacing-1) + end_spcing), "|TEXT", sep="")
        print("-"*(front_spacing + (16*spacing) + end_spcing + 18))
        print(hex(l), " "*(front_spacing-len(hex(l))), "|", sep="", end="")
        while data := f.read(1):
            bs = str(hex(data[0]))
            line_rep += chr(data[0]) if data[0] >= 0x20 and data[0] <= 0x7e else '.'
            print(bs, " "*(spacing-len(bs)), sep="", end="")
            l += 1
            if l > 0 and l % 16 == 0:
                print(" "*end_spcing, "|", line_rep, sep="")
                print(hex(l), " "*(front_spacing-len(hex(l))), "|", sep="", end="")
                line_rep = ""
        print(" "*((spacing*(16-(l%16))) + end_spcing), "|", line_rep, sep="")
    