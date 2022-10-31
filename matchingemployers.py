
import pandas as pd

directory = "C:\\Users\\JSmith371\\Documents\\programming\\randomlocalstuff\\matchingemployers"
df = pd.read_excel(f"{directory}\\Symplicity and Handshake.xlsx")

df["Handshake Email URL"] = [
    url.replace(" Count","")
    for url in df["Handshake Email URL"].tolist()
]

df["Symplicity Email URL"] = [
    url.replace(" Count","")
        if type(url)!=float
        else url
    for url in df["Symplicity Email URL"].tolist()
]

df["In Handshake (Y/N)"] = [
    url in df["Handshake Email URL"].tolist()
        if url not in ("gmail.com", "yahoo.com", "hotmail.com")
        else df["Symplicity Employer"][idx].lower() in [i.lower() if type(i)==str else i for i in df["Handshake Employer"].tolist()]
            if type(df["Symplicity Employer"][idx])==str
            else False
    for idx,url in enumerate(df["Symplicity Email URL"].tolist())
]

df.to_excel(f"{directory}\\Results.xlsx")
