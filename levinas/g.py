import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
d={1991:1,1993:1,1994:1,1995:1,1996:2,1998:4,2000:3,2001:6,2002:4,2003:6,2004:2,2005:7,2006:4,2007:6,2008:9,2009:3,2010:3,2011:5,2012:6,2013:7,2014:4,2015:5,2016:8,2017:8,2018:6,2019:9,2020:6,2021:5,2022:5,2023:8,2024:10}
ys=list(range(1991,2025));v=[d.get(y,0) for y in ys]
cum=[sum(v[:i+1]) for i in range(len(v))]
f,a=plt.subplots(figsize=(11,5.5));a.bar(ys,v,color="#3b6ea5");a.set_ylabel("Trabalhos por ano")
b=a.twinx();b.plot(ys,cum,color="#d1495b",lw=2.5);b.set_ylabel("Acumulado")
a.set_title("Teses e dissertações sobre Levinas na Base Filosófica (n=155; 115 diss. + 40 teses)")
a.set_xlabel("Ano de defesa");plt.tight_layout();plt.savefig("levinas_evolucao.png",dpi=150)
with open("levinas_lista.md","w") as o:
    o.write("| Ano | Trabalhos | Acumulado |\n|---|---|---|\n")
    for y,n,c in zip(ys,v,cum):o.write(f"| {y} | {n} | {c} |\n")
