uni = "Grading System for University"
title = "Examination Result"
print("\n", uni.center(100), "\n", title.center(100), "\n")


while True:
    name = input("Name : ")
    roll = input("Roll number : ")
    major = input("Major : ")
    year = input("Year : ")

    if year == "first":
        print("\nEnter your marks of following subjects.")
        myan1 = int(input("Myanmar : "))
        eng1 = int(input("English : "))
        maths1 = int(input("Maths: "))
        phy1 = int(input("Physics : "))
        che1 = int(input("Chemistry : "))
        draw1 = int(input("Basic Drawing : "))
        sum1 = myan1+eng1+maths1+phy1+che1+draw1

        def tol(*sub):
            for s in sub:
                if s >= 85 and s < 100:
                    print("\n",s)
                    print("{}".format("You passed with Excellent."))
                elif s > 0 and s <= 50:
                    print("\n",s)
                    print("{}".format("You failed the exame."))
                    exit()
                else:
                    print("\n",s)
                    print("{}".format("You passed."))
        tol(myan1,eng1,maths1,phy1,che1,draw1)

        print ("\n\t", name , "under Roll number", roll, "passed the exam with total marks", sum1)


    if year == "second":
        print("\nEnter your marks of following subjects.")
        eng2 = int(input("English : "))
        maths2 = int(input("Maths : "))
        ws2 = int(input("Workshop : "))
        mech2 = int(input("Mechanics : "))
        mj12 = int(input("Major1 : "))
        mj22 = int(input("Major2 : "))
        mj32 = int(input("Major3 : "))
        sum2 = eng2+maths2+ws2+mech2+mj12+mj22+mj32

        def tol(*sub):
            for s in sub:
                if s >= 85 and s < 100:
                    print("\n",s)
                    print("{}".format("You passed with Excellent."))
                elif s > 0 and s <= 50:
                    print("\n",s)
                    print("{}".format("You failed the exame."))
                    exit()
                else:
                    print("\n",s)
                    print("{}".format("You passed."))
        tol(eng2,maths2,ws2,mech2,mj12,mj22,mj32)

        print("\n\t", name, "under Roll number", roll, "passed the exam with total marks", sum2)


    if year == "third":
        print("\nEnter your marks of following subjects.")
        maths3 = int(input("Maths : "))
        mat3 = int(input("Materials : "))
        thr3 = int(input("Thermodynamics : "))
        tom3 = int(input("Theory of Machines : "))
        mj13 = int(input("Major1 : "))
        mj23 = int(input("Major2 : "))
        mj33 = int(input("Major3 : "))
        sum3 = maths3+mat3+thr3+tom3+mj13+mj23+mj33

        def tol(*sub):
            for s in sub:
                if s >= 85 and s < 100:
                    print("\n",s)
                    print("{}".format("You passed with Excellent."))
                elif s > 0 and s <= 50:
                    print("\n",s)
                    print("{}".format("You failed the exame."))
                    exit()
                else:
                    print("\n",s)
                    print("{}".format("You passed."))
        tol(maths3,mat3,thr3,tom3,mj13,mj23,mj33)

        print("\n\t", name, "under Roll number", roll, "passed the exam with total marks", sum3)

    if year == "fourth":
        print("\nEnter your marks of following subjects.")
        maths4 = int(input("Maths : "))
        hss4 = int(input("HSS : "))
        ep4 = int(input("Electropower : "))
        mj14 = int(input("Major1 : "))
        mj24 = int(input("Major2 : "))
        mj34 = int(input("Major3 : "))
        mj44 = int(input("Major4 : "))
        sum4 = maths4+hss4+ep4+mj14+mj24+mj34+mj44

        def tol(*sub):
            for s in sub:
                if s >= 85 and s < 100:
                    print("\n",s)
                    print("{}".format("You passed with Excellent."))
                elif s > 0 and s <= 50:
                    print("\n",s)
                    print("{}".format("You failed the exame."))
                    exit()
                else:
                    print("\n",s)
                    print("{}".format("You passed."))
        tol(maths4,hss4,ep4,mj14,mj24,mj34,mj44)

        print("\n\t", name, "under Roll number", roll, "passed the exam with total marks", sum4)

    if year == "fifth":
        print("\nEnter your marks of following subjects.")
        s15 = int(input("Subject 1 : "))
        s25 = int(input("Subject 2 : "))
        s35 = int(input("Subject 3 : "))
        mj15 = int(input("Major1 : "))
        mj25 = int(input("Major2 : "))
        mj35 = int(input("Major3 : "))
        mj45 = int(input("Major4 : "))
        sum5 = s15+s25+s35+mj15+mj25+mj35+mj45

        def tol(*sub):
            for s in sub:
                if s >= 85 and s < 100:
                    print("\n",s)
                    print("{}".format("You passed with Excellent."))
                elif s > 0 and s <= 50:
                    print("\n",s)
                    print("{}".format("You failed the exame."))
                    exit()
                else:
                    print("\n",s)
                    print("{}".format("You passed."))
        tol(s15,s25,s35,mj15,mj25,mj35,mj45)

        print("\n\t", name, "under Roll number", roll, "passed the exam with total marks", sum5)

    if year == "sixth":
        print("\nEnter your marks of following subjects.")
        s16 = int(input("Subject 1 : "))
        s26 = int(input("Subject 2 : "))
        s36 = int(input("Subject 3 : "))
        mj16 = int(input("Major1 : "))
        mj26 = int(input("Major2 : "))
        mj36 = int(input("Major3 : "))
        mj46 = int(input("Major4 : "))
        sum6 = s16+s26+s36+mj16+mj26+mj36+mj46

        def tol(*sub):
            for s in sub:
                if s >= 85 and s < 100:
                    print("\n",s)
                    print("{}".format("You passed with Excellent."))
                elif s > 0 and s <= 50:
                    print("\n",s)
                    print("{}".format("You failed the exame."))
                    exit()
                else:
                    print("\n",s)
                    print("{}".format("You passed."))
        tol(s16,s26,s36,mj16,mj26,mj36,mj46)

        print("\n\t", name, "under Roll number", roll, "passed the exam with total marks", sum6)

    x = input("\nDo you want to continue?\nyes (or) no : ")
    if x == "yes":
        print("\n")
        continue
    if x == "no":
        exit()

