#Group 007
import math
class bcolors:
    HEADER = '\033[95m'
    MAGENTA = '\35m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def twopoint(Total_load, L_span , E_modulus ,Inertia):
    SF = round((Total_load) / 2)
    SF = SF / 1000
    BM = round((Total_load / 2) * (L_span / 3))
    BM = BM / 1000000
    D = float((23 * Total_load * L_span ** 3) / (1296 * E_modulus * Inertia))
    return [SF, BM, D]


def triangular(Total_load, L_span, E_modulus, Inertia):
    SF = round((L_span * Total_load) / 4)
    SF = SF/1000
    BM = round((Total_load * L_span ** 2) / 12)
    BM = BM / 1000000
    D = float((Total_load * L_span ** 4) / (120 * E_modulus * Inertia))
    return [SF,BM,D]


def UDL(Total_load, L_span, E_modulus, Inertia):
    SF = round((L_span * Total_load) / 2)
    SF = SF / 1000
    BM = round((Total_load * L_span ** 2) / 8)
    BM = BM/1000000
    D = float((5 * Total_load * L_span ** 4) / (384 * E_modulus * Inertia))

    return [SF, BM, D]


def cement_info():


    cement = input(f"{bcolors.OKCYAN}Cement you want to use \n a.fresh \n b.shah \n c.bashundhara \n (choose a,b or c):{bcolors.ENDC} ")
    while not (cement == 'a' or cement == 'b' or cement == 'c'):

        cement = input(f"{bcolors.FAIL}Invalid input please try again : {bcolors.ENDC}")

    # dictinary was implemented to store cement information
    c = {"fresh":"95-96% | 15-24% | 0-4%  |   A","shah":"95-97% | 15-23% | 0-5%  | A" ,
         "bashundhara":"94-99% | 15-25% | 0-4% |   A", "info":"clinker| fly_ash| gypsum| grade"}

    print("Cement Info :")
    if cement == "a":
        print()
        print(f"{bcolors.UNDERLINE}{c['info']}{bcolors.ENDC}")
        print(c["fresh"])
        print()

    elif cement == "b":
        print()
        print(f"{bcolors.UNDERLINE}{c['info']}{bcolors.ENDC}")

        print(c["shah"])
        print()

    elif cement == "c":
        print()
        print(f"{bcolors.UNDERLINE}{c['info']}{bcolors.ENDC}")
        print(c["bashundhara"])
        print()

    '''elif cement == "d":
        print("clinker| fly_ash| gypsum| grade")
        print("95-98% | 15-23% | 0-5%  | A")

    elif cement == "e":
        print("clinker| fly_ash| gypsum| grade")
        print("95-99%| 17-25%| 0-4%| A")

    elif cement == "f":
        print("clinker| fly_ash| gypsum| grade")
        print("95-100%| 15-25%| 0-5%| A")'''









def rebar_info():
    rebar = input(f"{bcolors.OKBLUE}Rebar you want to use \n a.bsrm \n b.rsrm \n c.aks \n (choose a,b,c):{bcolors.ENDC} ")
    while not (rebar == 'a' or rebar == 'b' or rebar == 'c'):
        rebar = input(f"{bcolors.FAIL}Invalid input please try again : {bcolors.ENDC}")
    # dictinary was implemented to store cement information
    r = {"bsrm": "   6%    |      1        |         50          |   A", "rsrm": "   7%    |      1        |         51          |   A",
         "aks": "   8%    |      1        |         49          |   B", "info": "tolerance| nominal_weight| cross_sectional_area| grade"}

    print("Rebar info :")

    if rebar == "a":
        print()
        print(f"{bcolors.UNDERLINE}{r['info']}{bcolors.ENDC}")
        print(r["bsrm"])
        print()
        E = 200 * (10 ** 3)
        return (E)
    if rebar == "b":
        print()
        print(f"{bcolors.UNDERLINE}{r['info']}{bcolors.ENDC}")
        print(r["rsrm"])
        print()
        E = 210 * (10 ** 3)
        return (E)
    if rebar == "c":
        print()
        print(f"{bcolors.UNDERLINE}{r['info']}{bcolors.ENDC}")
        print(r["aks"])
        print()
        E = 210 * (10 ** 3)
        return (E)
    '''if rebar == "d":
        print("tolerance| nominal_weight| cross_sectional_area| grade")
        print("9%| 1| 50| A")
        E = 210
        return (E)
    if rebar == "e":
        print("tolerance| nominal_weight| cross_sectional_area| grade")
        print("8%| 1| 52| A")
        E = 210
        return (E)
    if rebar == "f":
        print("tolerance| nominal_weight| cross_sectional_area| grade")
        print("7%| 1| 52| A")
        E = 210
        return (E)'''



