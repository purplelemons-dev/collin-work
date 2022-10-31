
import pandas as pd

directory = "C:\\Users\\JSmith371\\Documents\\programming\\randomlocalstuff\\matchingemployers"
df = pd.read_excel(f"{directory}\\Symplicity and Handshake.xlsx")

df["Handshake Email URL"] = [
    df["Handshake Email URL"][idx].replace(" Count","")
    for idx,url in enumerate(df["Handshake Email URL"].tolist())
]

df["Symplicity Email URL"] = [
    df["Symplicity Email URL"][idx].replace(" Count","")
        if type(df["Symplicity Email URL"][idx])!=float
        else df["Symplicity Email URL"][idx]
    for idx,url in enumerate(df["Symplicity Email URL"].tolist())
]

df["In Handshake (Y/N)"] = [
    df["Symplicity Email URL"][idx] in df["Handshake Email URL"].tolist()
        if df["Symplicity Email URL"][idx] not in ("gmail.com", "yahoo.com", "hotmail.com")
        else df["Symplicity Employer"][idx].lower() in [i.lower() if type(i)==str else i for i in df["Handshake Employer"].tolist()]
            if type(df["Symplicity Employer"][idx])==str
            else False
    for idx,url in enumerate(df["Symplicity Email URL"].tolist())
]

df.to_excel("C:\\Users\\JSmith371\\Documents\\programming\\randomlocalstuff\\matchingemployers\\Results.xlsx")
