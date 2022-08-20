#Group 007

import math
import BendingModule

#class ANSI colors implemented for better code readability
class bcolors:
    HEADER = '\033[95m'
    MAGENTA = '\033[35m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



#Initializing List structure
force = []
shear = []
bending = []
deflection = []

print()
print(f"{bcolors.HEADER}***INFORMATION***{bcolors.ENDC}")
print()
#calling
BendingModule.cement_info()
E_modulus = BendingModule.rebar_info()




print()
print(f"{bcolors.WARNING}***INPUT***{bcolors.ENDC}")
print()

beam= input(f"{bcolors.MAGENTA}Choose Type \n a.Two point Load \n b.Triangular load  \n c.UDL (Uniformly Distributed Load) \n (choose a,b or c): {bcolors.ENDC}")
while not(beam == 'a' or beam == 'b' or beam == 'c'):
    beam = input(f"{bcolors.FAIL}Invalid input please try again : {bcolors.ENDC}")

print()
L_span_m = float(input('Beam length (unit: m): '))  # unit: m
L_span = L_span_m * 1000  # unit: mm
Width = float(input('Width of cross section of Beam (unit: mm):'))
Height = float(input('Height of cross section of Beam (unit: mm):'))
D_load = float(input('Dead load (N or N/mm): '))  # in kN or N/mm or Kn/m

Inertia = (Width * (Height ** 3)) / 12  # calculation of inertia
print(f"{bcolors.HEADER}Youngs modulus : {bcolors.ENDC}{E_modulus} Pa")

print(f"{bcolors.HEADER}Moment of Inertia :{bcolors.ENDC}{Inertia} mm^4")
print()
t = int(input(f"{bcolors.MAGENTA}Input Number of Loads you want to apply :{bcolors.ENDC}"))

print(f"{bcolors.WARNING}Loads used :{bcolors.ENDC}")

# CALCULATION

if beam == "a":  # Beam with 2-point Load

    for i in range(t):
        I_load = float(input('Imposed load (N): '))  # in N or N/mm or kn/m
        Total_load = D_load + I_load
        force.append(Total_load)

        x = BendingModule.twopoint(Total_load, L_span, E_modulus, Inertia)
        shear.append(x[0])
        bending.append(x[1])
        deflection.append(x[2])





elif beam == "b":  # Beam with Triangular Load
    for i in range(t):
        I_load = float(input('Imposed load (N/mm or KN/m): '))  # in N or N/mm or kn/m
        Total_load = D_load + I_load
        force.append(Total_load)

        x = BendingModule.triangular(Total_load, L_span, E_modulus, Inertia)
        shear.append(x[0])
        bending.append(x[1])
        deflection.append(x[2])




elif beam == "c":  # Beam with UDL Load
    for i in range(t):
        I_load = float(input('Imposed load (N/mm or KN/m): '))  # in N or N/mm or kn/m
        Total_load = D_load + I_load
        force.append(Total_load)

        x = BendingModule.UDL(Total_load, L_span, E_modulus, Inertia)
        shear.append(x[0])
        bending.append(x[1])
        deflection.append(x[2])

# OUTPUT

# we merged the 4 lists to a 2dlist
table = [list(a) for a in zip(force, shear, bending, deflection, )]

# output of list in table format

print()
print(f"{bcolors.HEADER}****OUTPUTS****{bcolors.ENDC}")
print()


print(f"{bcolors.BOLD}TABLE :{bcolors.ENDC}")


def plist(table):
    print(f"{bcolors.UNDERLINE}FORCE(N)| SHEAR(KN)| BENDING(KN.m)|DEFLECTION(mm)|{bcolors.ENDC}")
    for i in table:
        for table in i:
            print(table, end="  |  ")
        print()


plist(table)

bending = sorted(bending)

M = bending[-1] #KN.m
M = M*1000  #KN.mm
y = Width/2 #mm
Max_tensile = (M*y)/Inertia
print()
print(f"{bcolors.FAIL}Max tensile stress :{bcolors.ENDC} {Max_tensile} Mpa")
Max_compressive = M*(-y)/Inertia
print()
print(f"{bcolors.FAIL}Max compressive stress : {bcolors.ENDC}{Max_compressive} Mpa")








