import random
import time


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


Cargo_Train = 0
Passenger_Train = 1
Intercity = 2
Waiting = 3

while True:
    importance = random.randrange(Waiting)
    if importance is 0:
        time.sleep(1)
        print("Here comes a" + bcolors.FAIL + bcolors.BOLD + " Cargo Train!" + bcolors.ENDC)
    if importance is 1:
        time.sleep(1)
        print("Here comes a" + bcolors.OKBLUE + bcolors.BOLD + " Passenger Train!" + bcolors.ENDC)
    if importance is 2:
        time.sleep(1)
        print("Here comes an" + bcolors.HEADER + bcolors.BOLD + " Intercity!" + bcolors.ENDC)

    # majd amikor egy vonat végigmegy, akkor jön majd új vonat

    # AZ első verzió: mindíg eltelik egy kör, és a console-ban minden kör egy sor, ezért megy strégen a vonat.

    print(bcolors.BOLD + "  Állomás 1" + "                    " + "Állomás 2" + "                   " + "Állomás 3")
    print("_______________________________________________________________________")

    if importance is 0:
        time.sleep(2)
        print(bcolors.FAIL + bcolors.BOLD + " Cargo Train!" + bcolors.ENDC)
        time.sleep(1.5)
        print("              " + bcolors.FAIL + bcolors.BOLD + " Cargo Train!" + bcolors.ENDC)
        time.sleep(1.5)
        print("                            " + bcolors.FAIL + bcolors.BOLD + " Cargo Train!" + bcolors.ENDC)
        time.sleep(1.5)
        print("                                          " + bcolors.FAIL + bcolors.BOLD + " Cargo Train!" + bcolors.ENDC)
        time.sleep(1.5)
        print("                                                        " + bcolors.FAIL + bcolors.BOLD + " Cargo Train!" + bcolors.ENDC)
        print("_______________________________________________________________________")

    if importance is 1:
        time.sleep(2)
        print(bcolors.OKBLUE + bcolors.BOLD + " Passenger Train!" + bcolors.ENDC)
        time.sleep(1)
        print("             " + bcolors.OKBLUE + bcolors.BOLD + " Passenger Train!" + bcolors.ENDC)
        time.sleep(1)
        print("                          " + bcolors.OKBLUE + bcolors.BOLD + " Passenger Train!" + bcolors.ENDC)
        time.sleep(1)
        print("                                       " + bcolors.OKBLUE + bcolors.BOLD + "  Passenger Train!" + bcolors.ENDC)
        time.sleep(1)
        print("                                                    " + bcolors.OKBLUE + bcolors.BOLD + "   Passenger Train!" + bcolors.ENDC)
        print("_______________________________________________________________________")

    if importance is 2:
        time.sleep(2)
        print(bcolors.HEADER + bcolors.BOLD + " Intercity!" + bcolors.ENDC)
        time.sleep(0.4)
        print("              " + bcolors.HEADER + bcolors.BOLD + " Intercity!" + bcolors.ENDC)
        time.sleep(0.4)
        print("                            " + bcolors.HEADER + bcolors.BOLD + " Intercity!" + bcolors.ENDC)
        time.sleep(0.4)
        print("                                          " + bcolors.HEADER + bcolors.BOLD + " Intercity!" + bcolors.ENDC)
        time.sleep(0.4)
        print("                                                        " + bcolors.HEADER + bcolors.BOLD + " Intercity!" + bcolors.ENDC)
        print("_______________________________________________________________________")
