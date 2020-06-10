import pandas  as  pd
import  json
data=[]
with open("text25.txt","r",encoding="utf-8") as fr:
    for  line in fr:
        j=json.loads(line)
        data.append(j)
print(data)
df=pd.DataFrame(data)
print(df)
df.to_excel("film.xlsx")