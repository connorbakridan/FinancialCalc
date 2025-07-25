import math
import sys
from itertools import repeat
while True:
    T = input("Do you want to convert one interest (p) type to another or work out an accumulated or discounted cashflow (c): ").upper()
    if T == "C":
        while True:
            Int = input("Choose the interest type your working in: ").upper()
            if Int == "I" or Int == "EFFECTIVE RATE OF INTEREST PER ANNUM" or Int == "EFFECTIVE RATE OF INTEREST" or Int == "EFFECTIVE INTEREST RATE" or Int == "EFFECTIVE" or Int == "EFFECTIVE INTEREST" or Int == "INTEREST EFFECTIVE" or Int == "EFFECTIVE INTEREST" or Int == "INTEREST EFF" or Int == "RATE OF INT":
                i = float(input("Enter the effective rate of interest per annum that you're working in: "))
                if i == 0:
                    print("The effective rate of interest per annum can't be equal to zero please enter a different value,")
                else:
                    i = i / 100
                    while True:
                        t = round(float(input("Enter the time in years: ")), 3)
                        if t < 0:
                            print("t has to be greater than or equal to 0, try another value.")
                        else:
                            while True:
                                ct = round(
                                    float(input("Enter the amount of capital you want to apply to this function: ")), 3)
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
                                                print(
                                                    "--------------------------------------------------------------------------")
                                                c = input(f"""Choose the function you'd like to work out or if finished click q to quit: 
                   at, vt, an, andue, anf, sn, sndue, snf, 
                   Ian, Iandue, Ianf, Ianff, SIan, SIandue, SIanf, SIanff, 
                   Dan, Dandue, Danf, Danff, SDan, SDandue, SDanf or SDanff.
                   Input choice: """).upper()
                                                if c == "AT":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(f"""This is the accumulated value: {ct * at}""")
                                                elif c == "VT":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(f"""This is the discounted value: {ct * vt}""")
                                                elif c == "AN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV applying ct @{ct} to an @{an}: {ct * an}""")
                                                elif c == "ANDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                   payed in advance of {ct} from 
                   t= 0 to t= {t} @i= {i}: {ct * andue}""")
                                                elif c == "ANF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i}, and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                   payed continuously per year of {ct} from 
                   t= 0 to t= {t} @i= {i}: {ct * anf}""")
                                                elif c == "SN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments,
                   payed in arrears of {ct} from 
                   t= 0 to t= {t} @i= {i}: {ct * sn}""")
                                                elif c == "SNDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments, 
                   payed in advance of {ct} from 
                   t= 0 to t= {t} @i= {i}: {ct * sndue}""")
                                                elif c == "SNF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i}, and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments, 
                   payed continuously per year of {ct} from 
                   t= 0 to t= {t} @i= {i}: {ct * snf}""")
                                                elif c == "IAN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                   payed in arrears where each payment of 
                   {ct} increases per year by a multiple of 
                   {t}-({t}-n) where n is the time that corresponds 
                   with the payment and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Ian}""")
                                                elif c == "IANDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                   payed in advance where each payment of 
                   {ct} increases per year by a multiple of 
                   {t}-({t}-(n+1)) where n is the time that corresponds 
                   with the payment and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Iandue}""")
                                                elif c == "IANF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                   payed continuously per year where each payment 
                   increases per year by a multiple of 
                   {t}-({t}-n) where n is the time that corresponds 
                   with the payment payed from [n-1,n]. 
                   This payed from: 
                   t= 0 to t= {t} @i= {i}: {ct * Ianf}""")
                                                elif c == "IANFF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                   payed continuously per year where each payment 
                   increases per year at a continuous rate such that 
                   the multiple that each payment is multiplied, 
                   increases to {t}-({t}-n) where n is the time 
                   that corresponds with the payment payed from [n-1,n]. 
                   This payed from: 
                   t= 0 to t= {t} @i= {i}: {ct * Ianff}""")
                                                elif c == "SIAN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments, 
                   payed in arrears where each payment 
                   increases each year by a multiple of 
                   {t}-({t}-n) where n is any given 
                   discrete time between t=0 and t={t} and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * SIan}""")
                                                elif c == "SIANDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments, 
                   payed in advance where each payment 
                   increases each year by a multiple of 
                   {t}-({t}-(n+1)) where n is any given 
                   discrete time between t=0 and t={t} 
                   and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * SIandue}""")
                                                elif c == "SIANF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments,
                   payed continuously per year where each payment 
                   increases per year by a multiple of 
                   {t}-({t}-n) where n is the time that 
                   corresponds with the payment payed from [n-1,n]. 
                   This payed from:
                   t= 0 to t= {t} @i= {i}: {ct * Ianf}""")
                                                elif c == "SIANFF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments, 
                   payed continuously per year where each payment 
                   increases per year at a continuous rate 
                   such that the multiple that each payment is multiplied, 
                   increases to {t}-({t}-n) where n is the 
                   time that corresponds with the payment payed from [n-1,n]. 
                   This payed from: t= 0 to t= {t} @i= {i}: {ct * Ianff}""")
                                                elif c == "DAN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments,
                   payed in arrears where each payment of 
                   {ct} decreases per year by a multiple of 
                   {t}-(n-1) where n is the time that 
                   corresponds with the payment and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Dan}""")
                                                elif c == "DANDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments,
                   payed in advance where each payment of 
                   {ct} decreases per year by a multiple of 
                   {t}-n where n is the time that 
                   corresponds with the payment and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Dandue}""")
                                                elif c == "DANF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments,
                    payed continuously where each payment 
                    decreases per year by a multiple of 
                   {t}-(n-1) where n is the time that 
                   corresponds with the payment payed from [n-1,n]. 
                   This payed from:
                   t= 0 to t= {t} @i= {i}: {ct * Danf}""")
                                                elif c == "DANFF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                   payed continuously where each payment 
                   decreases per year at a continuous rate 
                   such that the multiple that each payment is multiplied, 
                   decreases to {t}-(n-1) where n is the time that 
                   corresponds with the payment payed from [n-1,n]. 
                   This payed from: t= 0 to t= {t} @i= {i}: {ct * Danff}""")
                                                elif c == "SDAN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of the 
                   Decreasing annuity in arrears: {ct * SDan}""")
                                                elif c == "SDANDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(f"""This is the accumulated value of the 
                   Decreasing annuity due: {ct * SDandue}""")
                                                elif c == "SDANF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of the 
                   Decreasing annuity payable continuously: {ct * SDanf}""")
                                                elif c == "SDANFF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of the 
                   Decreasing annuity payable continuously 
                   and decreasing continuously: {ct * SDanff}""")
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
                                                        f"""'{c}' is not a valid annuity function,
                    please choose one listed below.""")
                                        elif pc == "Y" or pc == "y":
                                            while True:
                                                p = float(input("Enter the p-thly time which ct is paid out: "))
                                                if p <= 0:
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print("""p cant be less than or equal to zero,                                    
                   please try a different value for p.""")
                                                    print(
                                                        "--------------------------------------------------------------------------")

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
                                                            """Choose the function you'd like to work out or if finished click q to quit: 
            anp, anduep, snp, snduep, 
            Ianp, Ianduep, SIanp, SIanduep, 
            Danp, Danduep, SDanp or SDanduep.
            Input choice: """).upper()
                                                        if c == "ANP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                   payed {p} thly in arrears of {ct} 
                   from t= 0 to t= {t} @i= {i}: {ct * anp}""")
                                                        elif c == "ANDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                   payed {p} thly in advance of {ct} 
                   from t= 0 to t= {t} @i= {i}: {ct * anduep}""")
                                                        elif c == "SNP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of a series of yearly payments
                   payed {p} thly in arrears of {ct} 
                   from t= 0 to t= {t} @i= {i}: {ct * snp}""")
                                                        elif c == "SNDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of a series of yearly payments 
                   payed {p} thly in advance of {ct} 
                   from t= 0 to t= {t} @i= {i}: {ct * snduep}""")
                                                        elif c == "IANP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                   payed {p} thly in arrears where each 
                   payment of {ct} increases per year by 
                   a multiple of {t}-({t}-n) where n is 
                   the time that corresponds with the payment 
                   and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Ianp}""")
                                                        elif c == "IANDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                   payed {p} thly in advance where 
                   each payment of {ct} increases per year 
                   by a multiple of {t}-({t}-(n+1)) 
                   where n is the time that corresponds 
                   with the payment and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Ianduep}""")
                                                        elif c == "SIANP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of a series of yearly payments 
                   payed {p} thly in arrears where each 
                   payment increases each year by a multiple 
                   of {t}-({t}-n) and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * SIanp}""")
                                                        elif c == "SIANDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of a series of yearly payments 
                   payed {p} thly in advance where each 
                   payment increases each year by a 
                   multiple of {t}-({t}-(n+1)) and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * SIanduep}""")
                                                        elif c == "DANP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                   payed {p} thly in arrears where each 
                   payment decreases per year by a multiple of 
                   {t}-(n-1) where n is the time that 
                   corresponds with the payment and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Danp}""")
                                                        elif c == "DANDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                   payed {p} thly in advance where each payment 
                   decreases per year by a multiple of {t}-n 
                   where n is the time that corresponds with 
                   the payment and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Danduep}""")
                                                        elif c == "SDANP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of the 
                   Decreasing annuity in arrears 
                   payable {p} thly: {ct * SDanp}""")
                                                        elif c == "SDANDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of the 
                   Decreasing annuity in advance 
                   payable {p} thly: {ct * SDanduep}""")
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
                                                                f"""'{c}' is not a valid annuity function,
                   please choose one listed below.""")
                                            else:
                                                print(f"""{pc} is not Y or N, 
                   Please enter Y for yes or N for no if the capital is payable p-thly: """)
            elif Int == "D" or Int == "EFFECTIVE RATE OF DISCOUNT PER ANNUM" or Int == "EFFECTIVE RATE OF DISCOUNT" or Int == "EFFECTIVE DISCOUNT RATE" or Int == "DISCOUNT EFF" or Int == "EFFECTIVE DISCOUNT" or Int == "DISCOUNT EFFECTIVE" or Int == "EFFECTIVE DISCOUNT" or Int == "RATE OF DIS":
                d = float(input("Enter the effective rate of discount per annum as a percent that you're working in: "))
                if d == 0:
                    print("The effective rate of discount per annum can't be equal to zero please enter a different value,")
                else:
                    d = d / 100
                    i = (((1 - d) ** -1) - 1)
                    while True:
                        t = round(float(input("Enter the time in years: ")), 3)
                        if t < 0:
                            print("t has to be greater than or equal to 0, try another value.")
                        else:
                            while True:
                                ct = round(
                                    float(input("Enter the amount of capital you want to apply to this function: ")), 3)
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
                                                print(
                                                    "--------------------------------------------------------------------------")
                                                c = input(f"""Choose the function you'd like to work out or if finished click q to quit: 
                   at, vt, an, andue, anf, sn, sndue, snf, 
                   Ian, Iandue, Ianf, Ianff, SIan, SIandue, SIanf, SIanff, 
                   Dan, Dandue, Danf, Danff, SDan, SDandue, SDanf or SDanff.
                   Input choice: """).upper()
                                                if c == "AT":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, d= {d} and ct= {ct}.")
                                                    print(f"""This is the accumulated value of 
                   {ct} from t= 0 to t= {t} @d= {d}: {ct * at}""")
                                                elif c == "VT":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(f"""This is the discounted value of 
                   {ct} from t= {t} to t= 0 @i= {i}: {ct * vt}""")
                                                elif c == "AN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                   payed in arrears of {ct} from 
                   t= 0 to t= {t} @i= {i}: {ct * an}""")
                                                elif c == "ANDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                   payed in advance of {ct} from 
                   t= 0 to t= {t} @i= {i}: {ct * andue}""")
                                                elif c == "ANF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i}, and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                   payed continuously per year of {ct} from 
                   t= 0 to t= {t} @i= {i}: {ct * anf}""")
                                                elif c == "SN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments,
                   payed in arrears of {ct} from 
                   t= 0 to t= {t} @i= {i}: {ct * sn}""")
                                                elif c == "SNDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments, 
                   payed in advance of {ct} from 
                   t= 0 to t= {t} @i= {i}: {ct * sndue}""")
                                                elif c == "SNF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i}, and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments, 
                   payed continuously per year of {ct} from 
                   t= 0 to t= {t} @i= {i}: {ct * snf}""")
                                                elif c == "IAN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                   payed in arrears where each payment of 
                   {ct} increases per year by a multiple of 
                   {t}-({t}-n) where n is the time that corresponds 
                   with the payment and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Ian}""")
                                                elif c == "IANDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                   payed in advance where each payment of 
                   {ct} increases per year by a multiple of 
                   {t}-({t}-(n+1)) where n is the time that corresponds 
                   with the payment and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Iandue}""")
                                                elif c == "IANF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                   payed continuously per year where each payment 
                   increases per year by a multiple of 
                   {t}-({t}-n) where n is the time that corresponds 
                   with the payment payed from [n-1,n]. 
                   This payed from: 
                   t= 0 to t= {t} @i= {i}: {ct * Ianf}""")
                                                elif c == "IANFF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                   payed continuously per year where each payment 
                   increases per year at a continuous rate such that 
                   the multiple that each payment is multiplied, 
                   increases to {t}-({t}-n) where n is the time 
                   that corresponds with the payment payed from [n-1,n]. 
                   This payed from: 
                   t= 0 to t= {t} @i= {i}: {ct * Ianff}""")
                                                elif c == "SIAN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments, 
                   payed in arrears where each payment 
                   increases each year by a multiple of 
                   {t}-({t}-n) where n is any given 
                   discrete time between t=0 and t={t} and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * SIan}""")
                                                elif c == "SIANDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments, 
                   payed in advance where each payment 
                   increases each year by a multiple of 
                   {t}-({t}-(n+1)) where n is any given 
                   discrete time between t=0 and t={t} 
                   and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * SIandue}""")
                                                elif c == "SIANF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments,
                   payed continuously per year where each payment 
                   increases per year by a multiple of 
                   {t}-({t}-n) where n is the time that 
                   corresponds with the payment payed from [n-1,n]. 
                   This payed from:
                   t= 0 to t= {t} @i= {i}: {ct * Ianf}""")
                                                elif c == "SIANFF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments, 
                   payed continuously per year where each payment 
                   increases per year at a continuous rate 
                   such that the multiple that each payment is multiplied, 
                   increases to {t}-({t}-n) where n is the 
                   time that corresponds with the payment payed from [n-1,n]. 
                   This payed from: t= 0 to t= {t} @i= {i}: {ct * Ianff}""")
                                                elif c == "DAN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments,
                   payed in arrears where each payment of 
                   {ct} decreases per year by a multiple of 
                   {t}-(n-1) where n is the time that 
                   corresponds with the payment and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Dan}""")
                                                elif c == "DANDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments,
                   payed in advance where each payment of 
                   {ct} decreases per year by a multiple of 
                   {t}-n where n is the time that 
                   corresponds with the payment and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Dandue}""")
                                                elif c == "DANF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments,
                    payed continuously where each payment 
                    decreases per year by a multiple of 
                   {t}-(n-1) where n is the time that 
                   corresponds with the payment payed from [n-1,n]. 
                   This payed from:
                   t= 0 to t= {t} @i= {i}: {ct * Danf}""")
                                                elif c == "DANFF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                   payed continuously where each payment 
                   decreases per year at a continuous rate 
                   such that the multiple that each payment is multiplied, 
                   decreases to {t}-(n-1) where n is the time that 
                   corresponds with the payment payed from [n-1,n]. 
                   This payed from: t= 0 to t= {t} @i= {i}: {ct * Danff}""")
                                                elif c == "SDAN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of the 
                   Decreasing annuity in arrears: {ct * SDan}""")
                                                elif c == "SDANDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(f"""This is the accumulated value of the 
                   Decreasing annuity due: {ct * SDandue}""")
                                                elif c == "SDANF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of the 
                   Decreasing annuity payable continuously: {ct * SDanf}""")
                                                elif c == "SDANFF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of the 
                   Decreasing annuity payable continuously 
                   and decreasing continuously: {ct * SDanff}""")
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
                                                        f"""'{c}' is not a valid annuity function,
                    please choose one listed below.""")
                                        elif pc == "Y" or pc == "y":
                                            while True:
                                                p = float(input("Enter the p-thly time which ct is paid out: "))
                                                if p <= 0:
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print("""p cant be less than or equal to zero,                                    
                   please try a different value for p.""")
                                                    print(
                                                        "--------------------------------------------------------------------------")
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
                                                            """Choose the function you'd like to work out or if finished click q to quit: 
            anp, anduep, snp, snduep, 
            Ianp, Ianduep, SIanp, SIanduep, 
            Danp, Danduep, SDanp or SDanduep.
            Input choice: """).upper()
                                                        if c == "ANP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                   payed {p} thly in arrears of {ct} 
                   from t= 0 to t= {t} @i= {i}: {ct * anp}""")
                                                        elif c == "ANDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                   payed {p} thly in advance of {ct} 
                   from t= 0 to t= {t} @i= {i}: {ct * anduep}""")
                                                        elif c == "SNP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of a series of yearly payments
                   payed {p} thly in arrears of {ct} 
                   from t= 0 to t= {t} @i= {i}: {ct * snp}""")
                                                        elif c == "SNDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of a series of yearly payments 
                   payed {p} thly in advance of {ct} 
                   from t= 0 to t= {t} @i= {i}: {ct * snduep}""")
                                                        elif c == "IANP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                   payed {p} thly in arrears where each 
                   payment of {ct} increases per year by 
                   a multiple of {t}-({t}-n) where n is 
                   the time that corresponds with the payment 
                   and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Ianp}""")
                                                        elif c == "IANDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                   payed {p} thly in advance where 
                   each payment of {ct} increases per year 
                   by a multiple of {t}-({t}-(n+1)) 
                   where n is the time that corresponds 
                   with the payment and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Ianduep}""")
                                                        elif c == "SIANP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of a series of yearly payments 
                   payed {p} thly in arrears where each 
                   payment increases each year by a multiple 
                   of {t}-({t}-n) and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * SIanp}""")
                                                        elif c == "SIANDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of a series of yearly payments 
                   payed {p} thly in advance where each 
                   payment increases each year by a 
                   multiple of {t}-({t}-(n+1)) and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * SIanduep}""")
                                                        elif c == "DANP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                   payed {p} thly in arrears where each 
                   payment decreases per year by a multiple of 
                   {t}-(n-1) where n is the time that 
                   corresponds with the payment and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Danp}""")
                                                        elif c == "DANDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                   payed {p} thly in advance where each payment 
                   decreases per year by a multiple of {t}-n 
                   where n is the time that corresponds with 
                   the payment and is payed from 
                   t= 0 to t= {t} @i= {i}: {ct * Danduep}""")
                                                        elif c == "SDANP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of the 
                   Decreasing annuity in arrears 
                   payable {p} thly: {ct * SDanp}""")
                                                        elif c == "SDANDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of the 
                   Decreasing annuity in advance 
                   payable {p} thly: {ct * SDanduep}""")
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
                                                                f"""'{c}' is not a valid annuity function,
                   please choose one listed below.""")
                                            else:
                                                print(f"""{pc} is not Y or N, 
                   Please enter Y for yes or N for no if the capital is payable p-thly: """)
            elif Int == "IP" or Int == "NOMINAL RATE OF INTEREST PER ANNUM" or Int == "NOMINAL RATE OF INTEREST PAYABLE PTHLY PER ANNUM" or Int == "NOMINAL RATE OF INTEREST PAYABLE P-THLY PER ANNUM" or Int == "NOMINAL RATE OF INTEREST" or Int == "NOMINAL RATE OF INTEREST PAYABLE PTHLY" or Int == "NOMINAL RATE OF INTEREST PAYABLE P-THLY" or Int == "NOMINAL INTEREST RATE" or Int == "NOMINAL INTEREST RATE PAYABLE PTHY" or Int == "NOMINAL INTEREST RATE PAYABLE P-THLY" or Int == "NOMINAL INTEREST" or Int == "INTEREST NOMINAL" or Int == "INTEREST NOM" or Int == "NOMINAL RATE OF INT" or Int == "NOM RATE OF INT":
                pz = float(input("Enter the 'p' in ip."))
                if pz == 0:
                    print("'p' can't be equal to zero.")
                elif pz < 0:
                    print("'p' can't be negative.")
                else:
                    ipz = float(input(f"Enter the nominal interest payable {pz}-thly per annum as a percent that you're working in: "))
                    if ipz == 0:
                        print(f"The nominal interest payable {pz}-thly per annum can't be equal to zero please enter a different value,")
                    else:
                        while True:
                            ipz = ipz / 100
                            t = round(float(input("Enter the time in years: ")), 3)
                            if t < 0:
                                print("t has to be greater than or equal to 0, try another value.")
                            else:
                                while True:
                                    ct = round(
                                        float(input("Enter the amount of capital you want to apply to this function: ")), 3)
                                    if ct == 0:
                                        print("""Theres no point in having capital as 0 your answer will just be 0, 
                       try a different value.""")
                                    else:
                                        while True:
                                            pc = input(
                                                """Is the amount of capital payable in p-thly intervals during the year? 
                If yes type Y or no then type N: """)
                                            if pc == "N" or pc == "n":
                                                i = (((1 + (ipz / pz)) ** pz) - 1)
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
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    c = input(f"""Choose the function you'd like to work out or if finished click q to quit: 
                       at, vt, an, andue, anf, sn, sndue, snf, 
                       Ian, Iandue, Ianf, Ianff, SIan, SIandue, SIanf, SIanff, 
                       Dan, Dandue, Danf, Danff, SDan, SDandue, SDanf or SDanff.
                       Input choice: """).upper()
                                                    if c == "AT":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(f"""This is the accumulated value of 
                       {ct} from t= 0 to t= {t} @i= {i}: {ct * at}""")
                                                    elif c == "VT":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(f"""This is the discounted value of 
                       {ct} from t= {t} to t= 0 @i= {i}: {ct * vt}""")
                                                    elif c == "AN":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed in arrears of {ct} from 
                       t= 0 to t= {t} @i= {i}: {ct * an}""")
                                                    elif c == "ANDUE":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed in advance of {ct} from 
                       t= 0 to t= {t} @i= {i}: {ct * andue}""")
                                                    elif c == "ANF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i}, and ct= {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed continuously per year of {ct} from 
                       t= 0 to t= {t} @i= {i}: {ct * anf}""")
                                                    elif c == "SN":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of a series of yearly payments,
                       payed in arrears of {ct} from 
                       t= 0 to t= {t} @i= {i}: {ct * sn}""")
                                                    elif c == "SNDUE":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of a series of yearly payments, 
                       payed in advance of {ct} from 
                       t= 0 to t= {t} @i= {i}: {ct * sndue}""")
                                                    elif c == "SNF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i}, and ct= {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of a series of yearly payments, 
                       payed continuously per year of {ct} from 
                       t= 0 to t= {t} @i= {i}: {ct * snf}""")
                                                    elif c == "IAN":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed in arrears where each payment of 
                       {ct} increases per year by a multiple of 
                       {t}-({t}-n) where n is the time that corresponds 
                       with the payment and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Ian}""")
                                                    elif c == "IANDUE":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed in advance where each payment of 
                       {ct} increases per year by a multiple of 
                       {t}-({t}-(n+1)) where n is the time that corresponds 
                       with the payment and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Iandue}""")
                                                    elif c == "IANF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed continuously per year where each payment 
                       increases per year by a multiple of 
                       {t}-({t}-n) where n is the time that corresponds 
                       with the payment payed from [n-1,n]. 
                       This payed from: 
                       t= 0 to t= {t} @i= {i}: {ct * Ianf}""")
                                                    elif c == "IANFF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed continuously per year where each payment 
                       increases per year at a continuous rate such that 
                       the multiple that each payment is multiplied, 
                       increases to {t}-({t}-n) where n is the time 
                       that corresponds with the payment payed from [n-1,n]. 
                       This payed from: 
                       t= 0 to t= {t} @i= {i}: {ct * Ianff}""")
                                                    elif c == "SIAN":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of a series of yearly payments, 
                       payed in arrears where each payment 
                       increases each year by a multiple of 
                       {t}-({t}-n) where n is any given 
                       discrete time between t=0 and t={t} and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * SIan}""")
                                                    elif c == "SIANDUE":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of a series of yearly payments, 
                       payed in advance where each payment 
                       increases each year by a multiple of 
                       {t}-({t}-(n+1)) where n is any given 
                       discrete time between t=0 and t={t} 
                       and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * SIandue}""")
                                                    elif c == "SIANF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of a series of yearly payments,
                       payed continuously per year where each payment 
                       increases per year by a multiple of 
                       {t}-({t}-n) where n is the time that 
                       corresponds with the payment payed from [n-1,n]. 
                       This payed from:
                       t= 0 to t= {t} @i= {i}: {ct * Ianf}""")
                                                    elif c == "SIANFF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of a series of yearly payments, 
                       payed continuously per year where each payment 
                       increases per year at a continuous rate 
                       such that the multiple that each payment is multiplied, 
                       increases to {t}-({t}-n) where n is the 
                       time that corresponds with the payment payed from [n-1,n]. 
                       This payed from: t= 0 to t= {t} @i= {i}: {ct * Ianff}""")
                                                    elif c == "DAN":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments,
                       payed in arrears where each payment of 
                       {ct} decreases per year by a multiple of 
                       {t}-(n-1) where n is the time that 
                       corresponds with the payment and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Dan}""")
                                                    elif c == "DANDUE":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments,
                       payed in advance where each payment of 
                       {ct} decreases per year by a multiple of 
                       {t}-n where n is the time that 
                       corresponds with the payment and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Dandue}""")
                                                    elif c == "DANF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments,
                        payed continuously where each payment 
                        decreases per year by a multiple of 
                       {t}-(n-1) where n is the time that 
                       corresponds with the payment payed from [n-1,n]. 
                       This payed from:
                       t= 0 to t= {t} @i= {i}: {ct * Danf}""")
                                                    elif c == "DANFF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed continuously where each payment 
                       decreases per year at a continuous rate 
                       such that the multiple that each payment is multiplied, 
                       decreases to {t}-(n-1) where n is the time that 
                       corresponds with the payment payed from [n-1,n]. 
                       This payed from: t= 0 to t= {t} @i= {i}: {ct * Danff}""")
                                                    elif c == "SDAN":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of the 
                       Decreasing annuity in arrears: {ct * SDan}""")
                                                    elif c == "SDANDUE":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(f"""This is the accumulated value of the 
                       Decreasing annuity due: {ct * SDandue}""")
                                                    elif c == "SDANF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of the 
                       Decreasing annuity payable continuously: {ct * SDanf}""")
                                                    elif c == "SDANFF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of the 
                       Decreasing annuity payable continuously 
                       and decreasing continuously: {ct * SDanff}""")
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
                                                            f"""'{c}' is not a valid annuity function,
                        please choose one listed below.""")
                                            elif pc == "Y" or pc == "y":
                                                while True:
                                                    p = float(input("Enter the p-thly time which ct is paid out: "))
                                                    if p == 0:
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print("""p can't equal to zero,                                    
                       please try a different value for p.""")
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                    elif p < 0:
                                                            print(
                                                                "--------------------------------------------------------------------------")
                                                            print("""p can't be less than zero,                                    
                                                    please try a different value for p.""")
                                                            print(
                                                                "--------------------------------------------------------------------------")
                                                    else:
                                                        while True:
                                                            i = (((1 + (ipz / pz)) ** pz) - 1)
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
                                                                """Choose the function you'd like to work out or if finished click q to quit: 
                anp, anduep, snp, snduep, 
                Ianp, Ianduep, SIanp, SIanduep, 
                Danp, Danduep, SDanp or SDanduep.
                Input choice: """).upper()
                                                            if c == "ANP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the PV of a series of yearly payments 
                       payed {p} thly in arrears of {ct} 
                       from t= 0 to t= {t} @i= {i}: {ct * anp}""")
                                                            elif c == "ANDUEP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the PV of a series of yearly payments 
                       payed {p} thly in advance of {ct} 
                       from t= 0 to t= {t} @i= {i}: {ct * anduep}""")
                                                            elif c == "SNP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the accumulated value of a series of yearly payments
                       payed {p} thly in arrears of {ct} 
                       from t= 0 to t= {t} @i= {i}: {ct * snp}""")
                                                            elif c == "SNDUEP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the accumulated value of a series of yearly payments 
                       payed {p} thly in advance of {ct} 
                       from t= 0 to t= {t} @i= {i}: {ct * snduep}""")
                                                            elif c == "IANP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the PV of a series of yearly payments 
                       payed {p} thly in arrears where each 
                       payment of {ct} increases per year by 
                       a multiple of {t}-({t}-n) where n is 
                       the time that corresponds with the payment 
                       and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Ianp}""")
                                                            elif c == "IANDUEP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the PV of a series of yearly payments 
                       payed {p} thly in advance where 
                       each payment of {ct} increases per year 
                       by a multiple of {t}-({t}-(n+1)) 
                       where n is the time that corresponds 
                       with the payment and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Ianduep}""")
                                                            elif c == "SIANP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the accumulated value of a series of yearly payments 
                       payed {p} thly in arrears where each 
                       payment increases each year by a multiple 
                       of {t}-({t}-n) and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * SIanp}""")
                                                            elif c == "SIANDUEP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the accumulated value of a series of yearly payments 
                       payed {p} thly in advance where each 
                       payment increases each year by a 
                       multiple of {t}-({t}-(n+1)) and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * SIanduep}""")
                                                            elif c == "DANP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                                print(
                                                                    f"""This is the PV of a series of yearly payments 
                       payed {p} thly in arrears where each 
                       payment decreases per year by a multiple of 
                       {t}-(n-1) where n is the time that 
                       corresponds with the payment and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Danp}""")
                                                            elif c == "DANDUEP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                                print(
                                                                    f"""This is the PV of a series of yearly payments 
                       payed {p} thly in advance where each payment 
                       decreases per year by a multiple of {t}-n 
                       where n is the time that corresponds with 
                       the payment and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Danduep}""")
                                                            elif c == "SDANP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                                print(
                                                                    f"""This is the accumulated value of the 
                       Decreasing annuity in arrears 
                       payable {p} thly: {ct * SDanp}""")
                                                            elif c == "SDANDUEP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                                print(
                                                                    f"""This is the accumulated value of the 
                       Decreasing annuity in advance 
                       payable {p} thly: {ct * SDanduep}""")
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
                                                                    f"""'{c}' is not a valid annuity function,
                       please choose one listed below.""")
                                                else:
                                                    print(f"""{pc} is not Y or N, 
                       Please enter Y for yes or N for no if the capital is payable p-thly: """)
            elif Int == "DP" or Int == "NOMINAL RATE OF DISCOUNT PER ANNUM" or Int == "NOMINAL RATE OF DISCOUNT PAYABLE PTHLY PER ANNUM" or Int == "NOMINAL RATE OF DISCOUNT PAYABLE P-THLY PER ANNUM" or Int == "NOMINAL RATE OF DISCOUNT" or Int == "NOMINAL RATE OF DISCOUNT PAYABLE PTHLY" or Int == "NOMINAL RATE OF DISCOUNT PAYABLE P-THLY" or Int == "NOMINAL DISCOUNT RATE" or Int == "NOMINAL DISCOUNT RATE PAYABLE PTHY" or Int == "NOMINAL DISCOUNT RATE PAYABLE P-THLY" or Int == "NOMINAL DISCOUNT" or Int == "DISCOUNT NOMINAL" or Int == "DISCOUNT NOM" or Int == "NOMINAL RATE OF DIS" or Int == "NOM RATE OF DIS":
                pz = float(input("Enter the 'p' in dp."))
                if pz == 0:
                    print("'p' can't be equal to zero.")
                elif pz < 0:
                    print("'p' can't be negative.")
                else:
                    dpz = float(input(f"Enter the nominal discount payable {pz}-thly per annum as a percent that you're working in: "))
                    if dpz == 0:
                        print(f"The nominal discount payable {pz}-thly per annum can't be equal to zero please enter a different value,")
                    else:
                        while True:
                            dpz = dpz / 100
                            t = round(float(input("Enter the time in years: ")), 3)
                            if t < 0:
                                print("t has to be greater than or equal to 0, try another value.")
                            else:
                                while True:
                                    ct = round(
                                        float(input("Enter the amount of capital you want to apply to this function: ")), 3)
                                    if ct == 0:
                                        print("""Theres no point in having capital as 0 your answer will just be 0, 
                       try a different value.""")
                                    else:
                                        while True:
                                            pc = input(
                                                """Is the amount of capital payable in p-thly intervals during the year? 
                If yes type Y or no then type N: """)
                                            if pc == "N" or pc == "n":
                                                i = (((1 - (dpz / pz)) ** -pz) - 1)
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
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    c = input(f"""Choose the function you'd like to work out or if finished click q to quit: 
                       at, vt, an, andue, anf, sn, sndue, snf, 
                       Ian, Iandue, Ianf, Ianff, SIan, SIandue, SIanf, SIanff, 
                       Dan, Dandue, Danf, Danff, SDan, SDandue, SDanf or SDanff.
                       Input choice: """).upper()
                                                    if c == "AT":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(f"""This is the accumulated value of 
                       {ct} from t= 0 to t= {t} @i= {i}: {ct * at}""")
                                                    elif c == "VT":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(f"""This is the discounted value of 
                       {ct} from t= {t} to t= 0 @i= {i}: {ct * vt}""")
                                                    elif c == "AN":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed in arrears of {ct} from 
                       t= 0 to t= {t} @i= {i}: {ct * an}""")
                                                    elif c == "ANDUE":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed in advance of {ct} from 
                       t= 0 to t= {t} @i= {i}: {ct * andue}""")
                                                    elif c == "ANF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i}, and ct= {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed continuously per year of {ct} from 
                       t= 0 to t= {t} @i= {i}: {ct * anf}""")
                                                    elif c == "SN":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of a series of yearly payments,
                       payed in arrears of {ct} from 
                       t= 0 to t= {t} @i= {i}: {ct * sn}""")
                                                    elif c == "SNDUE":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of a series of yearly payments, 
                       payed in advance of {ct} from 
                       t= 0 to t= {t} @i= {i}: {ct * sndue}""")
                                                    elif c == "SNF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i}, and ct= {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of a series of yearly payments, 
                       payed continuously per year of {ct} from 
                       t= 0 to t= {t} @i= {i}: {ct * snf}""")
                                                    elif c == "IAN":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed in arrears where each payment of 
                       {ct} increases per year by a multiple of 
                       {t}-({t}-n) where n is the time that corresponds 
                       with the payment and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Ian}""")
                                                    elif c == "IANDUE":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed in advance where each payment of 
                       {ct} increases per year by a multiple of 
                       {t}-({t}-(n+1)) where n is the time that corresponds 
                       with the payment and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Iandue}""")
                                                    elif c == "IANF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed continuously per year where each payment 
                       increases per year by a multiple of 
                       {t}-({t}-n) where n is the time that corresponds 
                       with the payment payed from [n-1,n]. 
                       This payed from: 
                       t= 0 to t= {t} @i= {i}: {ct * Ianf}""")
                                                    elif c == "IANFF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed continuously per year where each payment 
                       increases per year at a continuous rate such that 
                       the multiple that each payment is multiplied, 
                       increases to {t}-({t}-n) where n is the time 
                       that corresponds with the payment payed from [n-1,n]. 
                       This payed from: 
                       t= 0 to t= {t} @i= {i}: {ct * Ianff}""")
                                                    elif c == "SIAN":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of a series of yearly payments, 
                       payed in arrears where each payment 
                       increases each year by a multiple of 
                       {t}-({t}-n) where n is any given 
                       discrete time between t=0 and t={t} and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * SIan}""")
                                                    elif c == "SIANDUE":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of a series of yearly payments, 
                       payed in advance where each payment 
                       increases each year by a multiple of 
                       {t}-({t}-(n+1)) where n is any given 
                       discrete time between t=0 and t={t} 
                       and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * SIandue}""")
                                                    elif c == "SIANF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of a series of yearly payments,
                       payed continuously per year where each payment 
                       increases per year by a multiple of 
                       {t}-({t}-n) where n is the time that 
                       corresponds with the payment payed from [n-1,n]. 
                       This payed from:
                       t= 0 to t= {t} @i= {i}: {ct * Ianf}""")
                                                    elif c == "SIANFF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of a series of yearly payments, 
                       payed continuously per year where each payment 
                       increases per year at a continuous rate 
                       such that the multiple that each payment is multiplied, 
                       increases to {t}-({t}-n) where n is the 
                       time that corresponds with the payment payed from [n-1,n]. 
                       This payed from: t= 0 to t= {t} @i= {i}: {ct * Ianff}""")
                                                    elif c == "DAN":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments,
                       payed in arrears where each payment of 
                       {ct} decreases per year by a multiple of 
                       {t}-(n-1) where n is the time that 
                       corresponds with the payment and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Dan}""")
                                                    elif c == "DANDUE":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments,
                       payed in advance where each payment of 
                       {ct} decreases per year by a multiple of 
                       {t}-n where n is the time that 
                       corresponds with the payment and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Dandue}""")
                                                    elif c == "DANF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments,
                        payed continuously where each payment 
                        decreases per year by a multiple of 
                       {t}-(n-1) where n is the time that 
                       corresponds with the payment payed from [n-1,n]. 
                       This payed from:
                       t= 0 to t= {t} @i= {i}: {ct * Danf}""")
                                                    elif c == "DANFF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(
                                                            f"""This is the PV of a series of yearly payments, 
                       payed continuously where each payment 
                       decreases per year at a continuous rate 
                       such that the multiple that each payment is multiplied, 
                       decreases to {t}-(n-1) where n is the time that 
                       corresponds with the payment payed from [n-1,n]. 
                       This payed from: t= 0 to t= {t} @i= {i}: {ct * Danff}""")
                                                    elif c == "SDAN":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of the 
                       Decreasing annuity in arrears: {ct * SDan}""")
                                                    elif c == "SDANDUE":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(f"""This is the accumulated value of the 
                       Decreasing annuity due: {ct * SDandue}""")
                                                    elif c == "SDANF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of the 
                       Decreasing annuity payable continuously: {ct * SDanf}""")
                                                    elif c == "SDANFF":
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                        print(
                                                            f"""This is the accumulated value of the 
                       Decreasing annuity payable continuously 
                       and decreasing continuously: {ct * SDanff}""")
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
                                                            f"""'{c}' is not a valid annuity function,
                        please choose one listed below.""")
                                            elif pc == "Y" or pc == "y":
                                                while True:
                                                    p = float(input("Enter the p-thly time which ct is paid out: "))
                                                    if p == 0:
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                        print("""p can't equal to zero,                                    
                       please try a different value for p.""")
                                                        print(
                                                            "--------------------------------------------------------------------------")
                                                    elif p < 0:
                                                            print(
                                                                "--------------------------------------------------------------------------")
                                                            print("""p can't be less than zero,                                    
                                                    please try a different value for p.""")
                                                            print(
                                                                "--------------------------------------------------------------------------")
                                                    else:
                                                        while True:
                                                            i = (((1 - (dpz / pz)) ** -pz) - 1)
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
                                                                """Choose the function you'd like to work out or if finished click q to quit: 
                anp, anduep, snp, snduep, 
                Ianp, Ianduep, SIanp, SIanduep, 
                Danp, Danduep, SDanp or SDanduep.
                Input choice: """).upper()
                                                            if c == "ANP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the PV of a series of yearly payments 
                       payed {p} thly in arrears of {ct} 
                       from t= 0 to t= {t} @i= {i}: {ct * anp}""")
                                                            elif c == "ANDUEP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the PV of a series of yearly payments 
                       payed {p} thly in advance of {ct} 
                       from t= 0 to t= {t} @i= {i}: {ct * anduep}""")
                                                            elif c == "SNP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the accumulated value of a series of yearly payments
                       payed {p} thly in arrears of {ct} 
                       from t= 0 to t= {t} @i= {i}: {ct * snp}""")
                                                            elif c == "SNDUEP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the accumulated value of a series of yearly payments 
                       payed {p} thly in advance of {ct} 
                       from t= 0 to t= {t} @i= {i}: {ct * snduep}""")
                                                            elif c == "IANP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the PV of a series of yearly payments 
                       payed {p} thly in arrears where each 
                       payment of {ct} increases per year by 
                       a multiple of {t}-({t}-n) where n is 
                       the time that corresponds with the payment 
                       and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Ianp}""")
                                                            elif c == "IANDUEP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the PV of a series of yearly payments 
                       payed {p} thly in advance where 
                       each payment of {ct} increases per year 
                       by a multiple of {t}-({t}-(n+1)) 
                       where n is the time that corresponds 
                       with the payment and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Ianduep}""")
                                                            elif c == "SIANP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the accumulated value of a series of yearly payments 
                       payed {p} thly in arrears where each 
                       payment increases each year by a multiple 
                       of {t}-({t}-n) and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * SIanp}""")
                                                            elif c == "SIANDUEP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                                print(
                                                                    f"""This is the accumulated value of a series of yearly payments 
                       payed {p} thly in advance where each 
                       payment increases each year by a 
                       multiple of {t}-({t}-(n+1)) and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * SIanduep}""")
                                                            elif c == "DANP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                                print(
                                                                    f"""This is the PV of a series of yearly payments 
                       payed {p} thly in arrears where each 
                       payment decreases per year by a multiple of 
                       {t}-(n-1) where n is the time that 
                       corresponds with the payment and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Danp}""")
                                                            elif c == "DANDUEP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                                print(
                                                                    f"""This is the PV of a series of yearly payments 
                       payed {p} thly in advance where each payment 
                       decreases per year by a multiple of {t}-n 
                       where n is the time that corresponds with 
                       the payment and is payed from 
                       t= 0 to t= {t} @i= {i}: {ct * Danduep}""")
                                                            elif c == "SDANP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                                print(
                                                                    f"""This is the accumulated value of the 
                       Decreasing annuity in arrears 
                       payable {p} thly: {ct * SDanp}""")
                                                            elif c == "SDANDUEP":
                                                                print(
                                                                    "--------------------------------------------------------------------------")

                                                                print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                                print(
                                                                    f"""This is the accumulated value of the 
                       Decreasing annuity in advance 
                       payable {p} thly: {ct * SDanduep}""")
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
                                                                    f"""'{c}' is not a valid annuity function,
                       please choose one listed below.""")
                                                else:
                                                    print(f"""{pc} is not Y or N, 
                       Please enter Y for yes or N for no if the capital is payable p-thly: """)

            elif Int == "F" or Int == "FORCE OF INTEREST PER ANNUM" or Int == "FORCE OF INTEREST" or Int == "FORCE" or Int == "FORCE PER ANNUM" or Int == "FORCE INT PER ANNUM" or Int == "INTEREST FORCE PER ANNUM" or Int == "INTEREST FORCE":
                f = float(input("Enter the force of interest per annum that you're working in: "))
                if f == 0:
                    print("The force of interest per annum can't be equal to zero please enter a different value,")
                else:
                    f = f / 100
                    i = (math.exp(f) - 1)
                    while True:
                        t = round(float(input("Enter the time in years: ")), 3)
                        if t < 0:
                            print("t has to be greater than or equal to 0, try another value.")
                        else:
                            while True:
                                ct = round(
                                    float(
                                        input("Enter the amount of capital you want to apply to this function: ")),
                                    3)
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
                                                print(
                                                    "--------------------------------------------------------------------------")
                                                c = input(f"""Choose the function you'd like to work out or if finished click q to quit: 
                                                               at, vt, an, andue, anf, sn, sndue, snf, 
                                                               Ian, Iandue, Ianf, Ianff, SIan, SIandue, SIanf, SIanff, 
                                                               Dan, Dandue, Danf, Danff, SDan, SDandue, SDanf or SDanff.
                                                               Input choice: """).upper()
                                                if c == "AT":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(f"""This is the accumulated value of 
                                                               {ct} from t= 0 to t= {t} @i= {i}: {ct * at}""")
                                                elif c == "VT":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(f"""This is the discounted value of 
                                                               {ct} from t= {t} to t= 0 @i= {i}: {ct * vt}""")
                                                elif c == "AN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                                                               payed in arrears of {ct} from 
                                                               t= 0 to t= {t} @i= {i}: {ct * an}""")
                                                elif c == "ANDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                                                               payed in advance of {ct} from 
                                                               t= 0 to t= {t} @i= {i}: {ct * andue}""")
                                                elif c == "ANF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i}, and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                                                               payed continuously per year of {ct} from 
                                                               t= 0 to t= {t} @i= {i}: {ct * anf}""")
                                                elif c == "SN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments,
                                                               payed in arrears of {ct} from 
                                                               t= 0 to t= {t} @i= {i}: {ct * sn}""")
                                                elif c == "SNDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments, 
                                                               payed in advance of {ct} from 
                                                               t= 0 to t= {t} @i= {i}: {ct * sndue}""")
                                                elif c == "SNF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i}, and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments, 
                                                               payed continuously per year of {ct} from 
                                                               t= 0 to t= {t} @i= {i}: {ct * snf}""")
                                                elif c == "IAN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                                                               payed in arrears where each payment of 
                                                               {ct} increases per year by a multiple of 
                                                               {t}-({t}-n) where n is the time that corresponds 
                                                               with the payment and is payed from 
                                                               t= 0 to t= {t} @i= {i}: {ct * Ian}""")
                                                elif c == "IANDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                                                               payed in advance where each payment of 
                                                               {ct} increases per year by a multiple of 
                                                               {t}-({t}-(n+1)) where n is the time that corresponds 
                                                               with the payment and is payed from 
                                                               t= 0 to t= {t} @i= {i}: {ct * Iandue}""")
                                                elif c == "IANF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                                                               payed continuously per year where each payment 
                                                               increases per year by a multiple of 
                                                               {t}-({t}-n) where n is the time that corresponds 
                                                               with the payment payed from [n-1,n]. 
                                                               This payed from: 
                                                               t= 0 to t= {t} @i= {i}: {ct * Ianf}""")
                                                elif c == "IANFF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                                                               payed continuously per year where each payment 
                                                               increases per year at a continuous rate such that 
                                                               the multiple that each payment is multiplied, 
                                                               increases to {t}-({t}-n) where n is the time 
                                                               that corresponds with the payment payed from [n-1,n]. 
                                                               This payed from: 
                                                               t= 0 to t= {t} @i= {i}: {ct * Ianff}""")
                                                elif c == "SIAN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments, 
                                                               payed in arrears where each payment 
                                                               increases each year by a multiple of 
                                                               {t}-({t}-n) where n is any given 
                                                               discrete time between t=0 and t={t} and is payed from 
                                                               t= 0 to t= {t} @i= {i}: {ct * SIan}""")
                                                elif c == "SIANDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments, 
                                                               payed in advance where each payment 
                                                               increases each year by a multiple of 
                                                               {t}-({t}-(n+1)) where n is any given 
                                                               discrete time between t=0 and t={t} 
                                                               and is payed from 
                                                               t= 0 to t= {t} @i= {i}: {ct * SIandue}""")
                                                elif c == "SIANF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments,
                                                               payed continuously per year where each payment 
                                                               increases per year by a multiple of 
                                                               {t}-({t}-n) where n is the time that 
                                                               corresponds with the payment payed from [n-1,n]. 
                                                               This payed from:
                                                               t= 0 to t= {t} @i= {i}: {ct * Ianf}""")
                                                elif c == "SIANFF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t= {t}, i= {i} and ct= {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of a series of yearly payments, 
                                                               payed continuously per year where each payment 
                                                               increases per year at a continuous rate 
                                                               such that the multiple that each payment is multiplied, 
                                                               increases to {t}-({t}-n) where n is the 
                                                               time that corresponds with the payment payed from [n-1,n]. 
                                                               This payed from: t= 0 to t= {t} @i= {i}: {ct * Ianff}""")
                                                elif c == "DAN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments,
                                                               payed in arrears where each payment of 
                                                               {ct} decreases per year by a multiple of 
                                                               {t}-(n-1) where n is the time that 
                                                               corresponds with the payment and is payed from 
                                                               t= 0 to t= {t} @i= {i}: {ct * Dan}""")
                                                elif c == "DANDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments,
                                                               payed in advance where each payment of 
                                                               {ct} decreases per year by a multiple of 
                                                               {t}-n where n is the time that 
                                                               corresponds with the payment and is payed from 
                                                               t= 0 to t= {t} @i= {i}: {ct * Dandue}""")
                                                elif c == "DANF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments,
                                                                payed continuously where each payment 
                                                                decreases per year by a multiple of 
                                                               {t}-(n-1) where n is the time that 
                                                               corresponds with the payment payed from [n-1,n]. 
                                                               This payed from:
                                                               t= 0 to t= {t} @i= {i}: {ct * Danf}""")
                                                elif c == "DANFF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the PV of a series of yearly payments, 
                                                               payed continuously where each payment 
                                                               decreases per year at a continuous rate 
                                                               such that the multiple that each payment is multiplied, 
                                                               decreases to {t}-(n-1) where n is the time that 
                                                               corresponds with the payment payed from [n-1,n]. 
                                                               This payed from: t= 0 to t= {t} @i= {i}: {ct * Danff}""")
                                                elif c == "SDAN":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of the 
                                                               Decreasing annuity in arrears: {ct * SDan}""")
                                                elif c == "SDANDUE":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(f"""This is the accumulated value of the 
                                                               Decreasing annuity due: {ct * SDandue}""")
                                                elif c == "SDANF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of the 
                                                               Decreasing annuity payable continuously: {ct * SDanf}""")
                                                elif c == "SDANFF":
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print(f"At t = {t}, i = {i} and ct = {ct}.")
                                                    print(
                                                        f"""This is the accumulated value of the 
                                                               Decreasing annuity payable continuously 
                                                               and decreasing continuously: {ct * SDanff}""")
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
                                                        f"""'{c}' is not a valid annuity function,
                                                                please choose one listed below.""")
                                        elif pc == "Y" or pc == "y":
                                            while True:
                                                p = float(input("Enter the p-thly time which ct is paid out: "))
                                                if p <= 0:
                                                    print(
                                                        "--------------------------------------------------------------------------")
                                                    print("""p cant be less than or equal to zero,                                    
                                                               please try a different value for p.""")
                                                    print(
                                                        "--------------------------------------------------------------------------")

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
                                                            """Choose the function you'd like to work out or if finished click q to quit: 
                                            anp, anduep, snp, snduep, 
                                            Ianp, Ianduep, SIanp, SIanduep, 
                                            Danp, Danduep, SDanp or SDanduep.
                                            Input choice: """).upper()
                                                        if c == "ANP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                                                               payed {p} thly in arrears of {ct} 
                                                               from t= 0 to t= {t} @i= {i}: {ct * anp}""")
                                                        elif c == "ANDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                                                               payed {p} thly in advance of {ct} 
                                                               from t= 0 to t= {t} @i= {i}: {ct * anduep}""")
                                                        elif c == "SNP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of a series of yearly payments
                                                               payed {p} thly in arrears of {ct} 
                                                               from t= 0 to t= {t} @i= {i}: {ct * snp}""")
                                                        elif c == "SNDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of a series of yearly payments 
                                                               payed {p} thly in advance of {ct} 
                                                               from t= 0 to t= {t} @i= {i}: {ct * snduep}""")
                                                        elif c == "IANP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                                                               payed {p} thly in arrears where each 
                                                               payment of {ct} increases per year by 
                                                               a multiple of {t}-({t}-n) where n is 
                                                               the time that corresponds with the payment 
                                                               and is payed from 
                                                               t= 0 to t= {t} @i= {i}: {ct * Ianp}""")
                                                        elif c == "IANDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                                                               payed {p} thly in advance where 
                                                               each payment of {ct} increases per year 
                                                               by a multiple of {t}-({t}-(n+1)) 
                                                               where n is the time that corresponds 
                                                               with the payment and is payed from 
                                                               t= 0 to t= {t} @i= {i}: {ct * Ianduep}""")
                                                        elif c == "SIANP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of a series of yearly payments 
                                                               payed {p} thly in arrears where each 
                                                               payment increases each year by a multiple 
                                                               of {t}-({t}-n) and is payed from 
                                                               t= 0 to t= {t} @i= {i}: {ct * SIanp}""")
                                                        elif c == "SIANDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t= {t}, i= {i}, p= {p} and ct= {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of a series of yearly payments 
                                                               payed {p} thly in advance where each 
                                                               payment increases each year by a 
                                                               multiple of {t}-({t}-(n+1)) and is payed from 
                                                               t= 0 to t= {t} @i= {i}: {ct * SIanduep}""")
                                                        elif c == "DANP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                                                               payed {p} thly in arrears where each 
                                                               payment decreases per year by a multiple of 
                                                               {t}-(n-1) where n is the time that 
                                                               corresponds with the payment and is payed from 
                                                               t= 0 to t= {t} @i= {i}: {ct * Danp}""")
                                                        elif c == "DANDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                            print(
                                                                f"""This is the PV of a series of yearly payments 
                                                               payed {p} thly in advance where each payment 
                                                               decreases per year by a multiple of {t}-n 
                                                               where n is the time that corresponds with 
                                                               the payment and is payed from 
                                                               t= 0 to t= {t} @i= {i}: {ct * Danduep}""")
                                                        elif c == "SDANP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of the 
                                                               Decreasing annuity in arrears 
                                                               payable {p} thly: {ct * SDanp}""")
                                                        elif c == "SDANDUEP":
                                                            print(
                                                                "--------------------------------------------------------------------------")

                                                            print(f"At t = {t}, i = {i}, p = {p} and ct = {ct}.")
                                                            print(
                                                                f"""This is the accumulated value of the 
                                                               Decreasing annuity in advance 
                                                               payable {p} thly: {ct * SDanduep}""")
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
                                                                f"""'{c}' is not a valid annuity function,
                                                               please choose one listed below.""")
                                            else:
                                                print(f"""{pc} is not Y or N, 
                                                               Please enter Y for yes or N for no if the capital is payable p-thly: """)
            else:
                print("Enter a valid interest rate,")
    elif T == "P":
        while True:
            Int = input("Choose the interest type your working in: ").upper()
            if Int == "B":
                break
            elif Int == "I":
                i = float(input("Enter the effective rate of interest per annum that you're working in: "))
                if i == 0:
                    print("The effective rate of interest per annum can't be equal to zero please enter a different value,")
                else:
                    Intc = input("Choose the interest you would like to convert to: ").upper()
                    if Intc == "I":
                        print(f"That's not a conversion, try again,")
                    elif Intc == "D":
                        d = -(((1 + i) ** -1) - 1)
                        print(
                            f"Converting 'Effective rate of interest per annum' @{i} to the 'Effective rate of discount per annum' we get d = {d} ")
                    elif Intc == "IP":
                        p = float(input("Enter the p-thly time the nominal is interest payed: "))
                        if p == 0:
                            print("Enter a value that's not 0.")
                        elif p < 0:
                            print("The value cannot be less than 0 that is impossible.")
                        else:
                            ip = p * ((((1 + i) ** 1) ** (1 / p)) - 1)
                            print(
                                f"Converting 'Effective rate of interest per annum' @{i} to the 'Nominal rate of interest payable {p}-thly per annum' we get {ip} ")
                    elif Intc == "DP":
                        p = float(input("Enter the p-thly time the nominal discount is payed: "))
                        if p == 0:
                            print("Enter a value that's not 0.")
                        elif p < 0:
                            print("The value cannot be less than 0 that is impossible.")
                        else:
                            dp = -p * ((1 + i) ** (-1 / p) - 1)
                            print(
                                f"Converting 'Effective rate of interest per annum' @{i} to the 'Nominal rate of discount payable {p}-thly per annum' we get {dp} ")
                    elif Intc == "F":
                        f = math.log(i)
                        print(f"Converting 'Effective rate of interest per annum' @{i} to the 'Force of interest per annum' we get {f} ")
                    else:
                        print(f"{Intc} isn't a type of interest rate.")
            elif Int == "D":
                d = float(input("Enter the effective rate of interest per annum that you're working in: "))
                if d == 0:
                    print("The effective rate of interest per annum can't be equal to zero please enter a different value,")
                else:
                    Intc = input("Choose the interest you would like to convert to: ").upper()
                    if Intc == "I":
                        i = (((1 - d) ** -1) - 1)
                        print(f"Converting 'Effective rate of discount per annum' @{d} to the 'Effective rate of interest per annum' we get {i} ")
                    elif Intc == "D":
                        print(f"That's not a conversion, try again,")
                    elif Intc == "IP":
                        p = float(input("Enter the p-thly time the nominal is interest payed: "))
                        if p == 0:
                            print("Enter a value that's not 0.")
                        elif p < 0:
                            print("The value cannot be less than 0 that is impossible.")
                        else:
                            ip = p * ((((1 - d) ** -1) ** (1 / p)) - 1)
                            print(
                                f"Converting 'Effective rate of discount per annum' @{d} to the 'Nominal rate of interest payable {p}-thly per annum' we get {ip} ")
                    elif Intc == "DP":
                        p = float(input("Enter the p-thly time the nominal discount is payed: "))
                        if p == 0:
                            print("Enter a value that's not 0.")
                        elif p < 0:
                            print("The value cannot be less than 0 that is impossible.")
                        else:
                            dp = -p * ((((1 - d) ** -1) ** (-1 / p)) - 1)
                            print(
                                f"Converting 'Effective rate of discount per annum' @{d} to the 'Nominal rate of discount payable {p}-thly per annum' we get {dp} ")
                    elif Intc == "F":
                        f = math.log((1 - d) ** -1)
                        print(f"Converting 'Effective rate of discount per annum' @{d} to the 'Force of interest per annum' we get {f} ")
                    else:
                        print(f"{Intc} isn't a type of interest rate.")
            elif Int == "IP":
                p = float(input("Enter the p-thly time the nominal is interest payed: "))
                if p == 0:
                    print("Enter a value that's not 0.")
                elif p < 0:
                    print("The value cannot be less than 0 that is impossible.")
                else:
                    ip = float(input(f"Enter the nominal rate of interest payable {p}-thly per annum that you're working in: "))
                    if ip == 0:
                        print(f"The nominal rate of interest payable {p}-thly per annum can't be equal to zero please enter a different value,")
                    else:
                        Intc = input("Choose the interest you would like to convert to: ").upper()
                        if Intc == "I":
                            i = ((1 + (ip / p) ** p) - 1)
                            print(f"Converting 'Nominal rate of interest payable {p}-thly per annum' @{ip} to the 'Effective rate of interest per annum' we get {i} ")
                        elif Intc == "D":
                            d = -((1 + (ip / p) ** -p) - 1)
                            print(f"Converting 'Nominal rate of interest payable {p}-thly per annum' @{ip} to the 'Effective rate of discount per annum' we get {d} ")
                        elif Intc == "IP":
                            print(f"That's not a conversion, try again,")
                        elif Intc == "DP":
                            p = float(input("Enter the p-thly time the nominal discount is payed: "))
                            if p == 0:
                                print("Enter a value that's not 0.")
                            elif p < 0:
                                print("The value cannot be less than 0 that is impossible.")
                            else:
                                dp = -p * (((1 + (ip / p)) ** -1) - 1)
                                print(
                                    f"Converting 'Nominal rate of interest payable {p}-thly per annum' @{ip} to the 'Nominal rate of discount payable {p}-thly per annum' we get {dp} ")
                        elif Intc == "F":
                            f = math.log(1 + (ip / p) ** p)
                            print(f"Converting 'Nominal rate of interest payable {p}-thly per annum' @{ip} to the 'Force of interest per annum' we get {f} ")
                        else:
                            print(f"{Intc} isn't a type of interest rate.")
            elif Int == "DP":
                p = float(input("Enter the p-thly time the nominal discount is payed: "))
                if p == 0:
                    print("Enter a value that's not 0.")
                elif p < 0:
                    print("The value cannot be less than 0 that is impossible.")
                else:
                    dp = float(input(f"Enter the nominal rate of discount payable {p}-thly per annum that you're working in: "))
                    if dp == 0:
                        print(f"The nominal rate of discount payable {p}-thly per annum can't be equal to zero please enter a different value,")
                    else:
                        Intc = input("Choose the interest you would like to convert to: ")
                        if Intc == "I":
                            i = ((1 - (dp / p) ** -p) - 1)
                            print(f"Converting 'Nominal rate of discount payable {p}-thly per annum' @{dp} to the 'Effective rate of interest per annum' we get {i} ")
                        elif Intc == "D":
                            d = -((1 - (dp / p) ** p) - 1)
                            print(f"Converting 'Nominal rate of discount payable {p}-thly per annum' @{dp} to the 'Effective rate of discount per annum' we get {d} ")
                        elif Intc == "IP":
                            p = float(input("Enter the p-thly time the nominal is interest payed: "))
                            if p == 0:
                                print("Enter a value that's not 0.")
                            elif p < 0:
                                print("The value cannot be less than 0 that is impossible.")
                            else:
                                ip = p * (((1 - (dp / p)) ** -1) - 1)
                                print(
                                    f"Converting 'Nominal rate of discount payable {p}-thly per annum' @{dp} to the 'Nominal rate of interest payable {p}-thly per annum' we get {ip} ")
                        elif Intc == "DP":
                            print(f"That's not a conversion, try again,")
                        elif Intc == "F":
                            f = math.log(1 - (dp / p) ** -p)
                            print(f"Converting 'Nominal rate of discount payable {p}-thly per annum' @{dp} to the 'Force of interest per annum' we get {f} ")
                        else:
                            print(f"{Intc} isn't a type of interest rate.")
            elif Int == "F":
                f = float(input("Enter the force of interest per annum that you're working in: "))
                if f == 0:
                    print("The force of interest per annum can't be equal to zero please enter a different value,")
                else:
                    Intc = input("Choose the interest you would like to convert to: ").upper()
                    if Intc == "I":
                        i = math.exp(f)
                        print(f"Converting 'Force of interest per annum' @{f} to the 'Effective rate of interest per annum' we get {i} ")
                    elif Intc == "D":
                        d = -(math.exp(-f) - 1)
                        print(f"Converting 'Force of interest per annum' @{f} to the 'Effective rate of discount per annum' we get {d} ")
                    elif Intc == "IP":
                        p = float(input("Enter the p-thly time the nominal is interest payed: "))
                        if p == 0:
                            print("Enter a value that's not 0.")
                        elif p < 0:
                            print("The value cannot be less than 0 that is impossible.")
                        else:
                            ip = p * ((math.exp(f) ** (1 / p)) - 1)
                            print(
                                f"Converting 'Force of interest per annum' @{f} to the 'Nominal rate of interest payable {p}-thly per annum' we get {ip} ")
                    elif Intc == "DP":
                        p = float(input("Enter the p-thly time the nominal discount is payed: "))
                        if p == 0:
                            print("Enter a value that's not 0.")
                        elif p < 0:
                            print("The value cannot be less than 0 that is impossible.")
                        else:
                            dp = p * (math.exp(f / -p) - 1)
                            print(
                                f"Converting 'Force of interest per annum' @{f} to the 'effective rate of discount' we get {dp} ")
                    elif Intc == "F":
                        print(f"That's not a conversion, try again,")
                    else:
                        print(f"{Intc} isn't a type of interest rate.")
    else:
        print("Please either type 'p' for our interest converter or c for our cashflow calculator,")

















