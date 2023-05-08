import csv
import fitz
import matplotlib.pyplot as plt
import pandas as pd


with open("data.csv", "w", encoding="utf8", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nota', 'cota', 'curso', 'entrada'])

    for page in fitz.open('aprovados.pdf'):
        page = page.get_text().split("\n")
        curso = page[6][7:]
        entrada = page[15]
        alunosNotas = page[18::4]
        alunosCotas = page[19::4]

        for nota, cota in zip(alunosNotas, alunosCotas):
            writer.writerow([nota, cota, curso, entrada])

df = pd.read_csv("data.csv")

# retorna a quantidade de alunos por entrada
def alunosEntrada():
    resultado = df["entrada"].value_counts().to_list()

    return resultado
# print(alunosEntrada())

# retorna o numero de alunos em cada curso
def alunosCurso():
    resultado = df["curso"].value_counts().to_dict()
    for k, v in resultado.items():
        print(f"{k} - {v}")
    return resultado
# alunosCurso()

# retorna a maior e menor nota
def notasExtremas():
    resultado = [df["nota"].max(), df["nota"].min()]
    return resultado
# print(notasExtremas())

# retorna o numero de estudantes com nota em cada intervalo de 100
def relacaoNotas():
    df["intervalo"] = pd.cut(df["nota"], bins=range(300, 1000, 100))
    counts = df["intervalo"].value_counts().sort_index()
    labels = ['{} - {}'.format(x.left, x.right) for x in counts.index]
    counts.plot.bar().set_xticklabels(labels, rotation=0)

    plt.title("Distribuição de notas dos alunos")
    plt.xlabel("intervalos de notas")
    plt.ylabel("quantidade de alunos")

    plt.grid()
    plt.show()

    return counts
# print(relacaoNotas())

# retorna a distribuiçao de alunos em cada cota
def relacaoAlunosCotas():
    resultados = df["cota"].value_counts().to_dict()
    num_slices = len(resultados.values())
    explode = tuple(i*0.09 if i >= num_slices-8 else 0 for i in range(num_slices))

    plt.title("Distribuição de alunos por cota")
    plt.pie(resultados.values(), labels=resultados.keys(), explode=explode, labeldistance = 1.05, textprops = {"fontsize":7})
    plt.legend()
    plt.show()

    return resultados
# print(relacaoAlunosCotas())

# retorna a média de notas em cada cota
def relacaoNotasCotas():
    resultados = df.groupby("cota")["nota"].mean().sort_values(ascending=False)
  
    plt.bar(resultados.index, resultados.values)
    plt.title("Relação de médias por cota")
    plt.xlabel("cotas")
    plt.ylabel("médias")
    
    plt.grid()
    plt.show()

    return resultados
# relacaoNotasCotas()

# retorna a media de notas de cada curso
def relacaoMediaCursos():
    resultados = df.groupby("curso")["nota"].mean()
    return resultados
# print(relacaoMediaCursos().to_dict())

# retorna a media de notas de cada cota em cada curso
def relacaoCursoCotaMedia():
    resultado = df.groupby(["curso", "cota"])["nota"].mean()
    return resultado
# print(relacaoCursoCotaNota())

# retorna os cursos com as maiores medias em cada cota
def cursoMaiorNotaMedia():
    max = relacaoCursoCotaMedia().groupby("cota").idxmax()
    resultados = {}
    for cota, idx in max.items():
        curso = idx[0]
        media = relacaoCursoCotaMedia().loc[idx]
        resultados[cota] = [curso, round(media, 2)]
    return resultados
# print(cursoMaiorNotaCota())
