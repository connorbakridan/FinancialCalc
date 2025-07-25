import math
import sys

while True:
    i = round(float(input("Enter Annual effective interest rate, as a percent: ")), 3)
    i = i / 100
    if i == 0:
        print("Formulas don't hold for i = 0, try another value.")
    else:
        while True:
            t = round(float(input("Enter the time in years: ")), 3)
            if t < 0:
                print("t has to be greater than or equal to 0, try another value.")
            else:
                while True:
                    ct = round(float(input("Enter the amount of capital you want to apply to this function: ")), 3)
                    if ct == 0:
                        print("""Theres no point in having capital as 0 your answer will just be 0, 
try a different value.""")
                    else:
                        while True:
                            pc = input(
                                """Is the amount of capital payable in p-thly intervals during the year? 
If yes type Y or no then type N: """)
                            if pc == "N" or pc == "n":
                                d = -(((1 + i) ** -1) - 1)
                                f = math.exp(i)
                                at = (1 + i) ** t
                                vt = at ** -1
                                an = (1 - vt) / i
                                andue = an * (i / d)
                                anf = an * (i / f)
                                sn = an * at
                                sndue = andue * at
                                snf = anf * at
                                Ian = ((andue) - (t * vt)) / i
                                Iandue = Ian * (i / d)
                                Ianf = Ian * (i / f)
                                Ianff = ((anf) - (t * vt)) / f
                                SIan = Ian * at
                                SIandue = Iandue * at
                                SIanf = Ianf * at
                                SIanff = Ianff * at
                                Dan = (t - an) / i
                                Dandue = Dan * (i / d)
                                Danf = Dan * (i / f)
                                Danff = (t - anf) / f
                                SDan = Dan * at
                                SDandue = Dandue * at
                                SDanf = Danf * at
                                SDanff = Danff * at
                                while True:
                                    print("--------------------------------------------------------------------------")
                                    c = input(f"""Choose the function you'd like to work out or if finished click q to quit: """).upper()
                                    if c == "AT":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                        print(f"""The answer is {ct * at}""")
                                    elif c == "VT":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                        print(f"""The answer is {ct * vt}""")
                                    elif c == "AN":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                        print(
                                            f"""The answer is {ct * an}""")
                                    elif c == "ANDUE":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "ANF":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i}, and ct= {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "SN":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "SNDUE":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "SNF":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i}, and ct= {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "IAN":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "IANDUE":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "IANF":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "IANFF":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "SIAN":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "SIANDUE":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "SIANF":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "SIANFF":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "DAN":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "DANDUE":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "DANF":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "DANFF":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "SDAN":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "SDANDUE":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                        print(f"""The answer is {ct * at}""")
                                    elif c == "SDANF":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "SDANFF":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                        print(
                                            f"""The answer is {ct * at}""")
                                    elif c == "Q":
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print("Thanks for using this calculator :)")
                                        print()
                                        sys.exit()

                                    else:
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print(
                                            f"""'{c}' is not a valid annuity function, please choose one that is.""")
                            elif pc == "Y" or pc == "y":
                                while True:
                                    p = float(input("Enter the p-thly time which ct is paid out: "))
                                    if p <= 0 :
                                        print(
                                            "--------------------------------------------------------------------------")
                                        print("""p cant be less than or equal to zero, please try a different value for p.""")
                                        print("--------------------------------------------------------------------------")

                                    else:
                                        while True:
                                            d = -(((1 + i) ** -1) - 1)
                                            dp = -p * ((((1 - d) ** -1) ** (-1 / p)) - 1)
                                            ip = p * ((((1 + i) ** 1) ** (1 / p)) - 1)
                                            f = math.exp(i)
                                            at = (1 + i) ** t
                                            vt = at ** -1
                                            an = (1 - vt) / i
                                            andue = an * (i / d)
                                            anp = an * (i / ip)
                                            anduep = an * (i / dp)
                                            anf = an * (i / f)
                                            sn = an * at
                                            sndue = andue * at
                                            snp = anp * at
                                            snduep = anduep * at
                                            snf = anf * at
                                            Ian = ((andue) - (t * vt)) / i
                                            Iandue = Ian * (i / d)
                                            Ianp = Ian * (i / ip)
                                            Ianduep = Ian * (i / dp)
                                            Ianf = Ian * (i / f)
                                            Ianff = ((anf) - (t * vt)) / f
                                            SIan = Ian * at
                                            SIandue = Iandue * at
                                            SIanp = Ianp * at
                                            SIanduep = Iandue * at
                                            SIanf = Ianf * at
                                            SIanff = Ianff * at
                                            Dan = (t - an) / i
                                            Dandue = Dan * (i / d)
                                            Danp = Dan * (i / ip)
                                            Danduep = Dan * (i / dp)
                                            Danf = Dan * (i / f)
                                            Danff = (t - anf) / f
                                            SDan = Dan * at
                                            SDandue = Dandue * at
                                            SDanp = Danp * at
                                            SDanduep = Danduep * at
                                            SDanf = Danf * at
                                            SDanff = Danff * at
                                            print(
                                                "--------------------------------------------------------------------------")
                                            c = input(
                                                """Choose the function you'd like to work out or if finished click q to quit: """).upper()
                                            if c == "ANP":
                                                print(
                                                    "--------------------------------------------------------------------------")

                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                print(
                                                    f"""The answer is {ct * at}""")
                                            elif c == "ANDUEP":
                                                print(
                                                    "--------------------------------------------------------------------------")

                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                print(
                                                    f"""The answer is {ct * at}""")
                                            elif c == "SNP":
                                                print(
                                                    "--------------------------------------------------------------------------")

                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                print(
                                                    f"""The answer is {ct * at}""")
                                            elif c == "SNDUEP":
                                                print(
                                                    "--------------------------------------------------------------------------")

                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                print(
                                                    f"""The answer is {ct * at}""")
                                            elif c == "IANP":
                                                print(
                                                    "--------------------------------------------------------------------------")

                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                print(
                                                    f"""The answer is {ct * at}""")
                                            elif c == "IANDUEP":
                                                print(
                                                    "--------------------------------------------------------------------------")

                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                print(
                                                    f"""The answer is {ct * at}""")
                                            elif c == "SIANP":
                                                print(
                                                    "--------------------------------------------------------------------------")

                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                print(
                                                    f"""The answer is {ct * at}""")
                                            elif c == "SIANDUEP":
                                                print(
                                                    "--------------------------------------------------------------------------")

                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                print(
                                                    f"""The answer is {ct * at}""")
                                            elif c == "DANP":
                                                print(
                                                    "--------------------------------------------------------------------------")

                                                print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                print(
                                                    f"""The answer is {ct * at}""")
                                            elif c == "DANDUEP":
                                                print(
                                                    "--------------------------------------------------------------------------")

                                                print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                print(
                                                    f"""The answer is {ct * at}""")
                                            elif c == "SDANP":
                                                print(
                                                    "--------------------------------------------------------------------------")

                                                print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                print(
                                                    f"""The answer is {ct * at}""")
                                            elif c == "SDANDUEP":
                                                print(
                                                    "--------------------------------------------------------------------------")

                                                print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                print(
                                                    f"""The answer is {ct * at}""")
                                            elif c == "Q":
                                                print("--------------------------------------------------------------------------")
                                                print("Thanks for using this calculator :)")
                                                print()
                                                sys.exit()
                                            else:
                                                print(
                                                    "--------------------------------------------------------------------------")
                                                print(
                                                    f"""'{c}' is not a valid annuity function, please choose one that is.""")
                            else:
                                    print(f"""{pc} is not Y or N, 
Please enter Y for yes or N for no if the capital is payable p-thly during the Yearly timeframe: """)


















