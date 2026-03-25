import pandas as pd
import random 

careers = [
    "Data Scientist",
    "AI Engineer",
    "Backend Developer",
    "Frontend Developer",
    "Full Stack Developer",
    "DevOps Engineer",
    "Cybersecurity Analyst",
    "Software Tester",
    "Cloud Engineer",
    "Product Manager"
]

data= []

for i in range(300):
    python = random.randint(0,1)
    java = random.randint(0,1)
    sql = random.randint(0,1)
    ml = random.randint(0,1)
    dsa = random.randint(0,1)
    web = random.randint(0,1)
    cloud = random.randint(0,1)
    networking = random.randint(0,1)
    linux = random.randint(0,1)
    git = random.randint(0,1)

    math_interest= random.randint(1,5)
    design_interest = random.randint(1,5)
    data_interest = random.randint(1,5)
    management_interest = random.randint(1,5)

    communication = random.choice(["Low", "Medium", "High"])
    leadership = random.choice(["Low", "Medium", "High"])
    creativity = random.choice(["Low", "Medium", "High"])

    #career = random.choice(careers) we are going to replace this with intelligent career assignment
    if ml == 1 and python == 1 and math_interest >= 4 and data_interest >= 4:
        career = "Data Scientist"
    elif ml == 1 and python == 1:
        career = "AI Engineer"
    elif web == 1 and design_interest >= 4:
        career = "Frontend Developer"
    elif web == 1 and python == 1 and java == 1:
        career = "Full Stack Developer"
    elif cloud == 1 and linux == 1 and networking == 1:
        career = "Cloud Engineer"
    elif linux == 1 and git == 1 and  cloud == 1:
        career = "DevOps Engineer"
    elif  networking == 1 and linux == 1:
        career = "Cybersecurity Analyst"
    elif dsa == 1 and python == 1:
        career = "Backend Developer"
    elif communication == "High" and leadership == "High" and management_interest >=4:
        career = "Product Manager"
    else:
        career = "Software Tester"

    data.append([
        python, java, sql, ml, dsa, web, cloud, networking, linux, git,
        math_interest, design_interest, data_interest, management_interest,
        communication, leadership, creativity,
        career 
    ])

    columns = [
        "Python","Java","SQL","ML","DSA","Web","Cloud",
        "Networking","Linux","Git",
        "MathInterest","DesignInterest",
        "DataInterest","ManagementInterest",
        "Communication","Leadership","Creativity",
        "Career"
    ]

df = pd.DataFrame(data, columns= columns)

df.to_csv("dataset.csv", index=False)

print("Dataset created successfully!")