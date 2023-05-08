# analise-dados-ufpe-aprovados-2023
Análise de dados dos aprovados na UFPE em 2023, com o objetivo de aprimorar meus conhecimentos na biblioteca Pandas do Python e na análise de dados em geral.

Os dados foram obtidos em um pdf disponivel no site da ufpe (https://sisu.ufpe.br/arquivos/2023/convocacoes/primeira/campus-recife-distribuicao-por-entrada.pdf).

Aplicação feita em python.

Para ler o pdf usei a biblioteca PyMuPDF, depois transformei em um arquivo .csv com os dados que eu usei (nota, cota, curso e entrada).

OBS: os pesos de cada curso não foram levados em consideração, por isso alguns resultados não foram tão precisos.

## Funções
- alunosEntrada - retorna uma lista com a quantidade de alunos na primeira e segunda entrada.
- alunosCurso - retorna um dicionário com a quantidade de alunos em cada curso.
- notasExtremas - retorna uma lista com a maior e a menor nota.
- relacaoNotas - retorna o número de estudantes com notas em cada intervalo de 100. Tambem cria um gráfico.
- relacaoAlunosCotas - retorna a quantidade de alunos em cada coa e gera um gráfico.
- relacaoNotasCotas - retorna a média de notas em cada cota e gera um gráfico.
- relacaoMediaCursos - retorna a média de notas em cada curso.
- relacaoCursoCotaNota - retorna a média de nota de cada cota em cada curso.
- cursoMaiorNotaCota - retorna os cursos com as maiores médias em cada cota.

## Resultados:
### alunosEntrada:

```[3171, 2176]``` 3171 alunos na primeira entrada e 2716 alunos na segunda.

### alunosCurso:

| curso | quantidade de alunos |
|-------|----------------------|
| ABI - ENGENHARIA | 521 |
| PEDAGOGIA | 250 |
| DIREITO | 250 |
| EDUCAÇÃO FÍSICA | 240 |
| CIÊNCIAS BIOLÓGICAS | 200 |
| ADMINISTRAÇÃO | 200 |
| CIÊNCIAS CONTÁBEIS | 192 |
| GEOGRAFIA | 180 |
| ODONTOLOGIA | 140 |
| MEDICINA | 140 |
| CIÊNCIAS SOCIAIS | 120 |
| SERVIÇO SOCIAL | 120 |
| BIOMEDICINA | 120 |
| CIÊNCIAS ECONÔMICAS | 118 |
| HISTÓRIA | 110 |
| SECRETARIADO | 100 |
| CIÊNCIA DA COMPUTAÇÃO | 100 |
| ARQUITETURA E URBANISMO | 100 |
| ENGENHARIA DA COMPUTAÇÃO | 100 |
| FARMÁCIA | 90 |
| LETRAS - PORTUGUÊS | 88 |
| CIÊNCIAS BIOLÓGICAS - ÊNFASE EM CIÊNCIAS AMBIENTAIS | 80 |
| PSICOLOGIA | 80 |
| ENFERMAGEM | 78 |
| MATEMÁTICA | 70 |
| TURISMO | 70 |
| DESIGN | 70 |
| SISTEMAS DE INFORMAÇÃO | 69 |
| FISIOTERAPIA | 66 |
| ENGENHARIA CARTOGRÁFICA E DE AGRIMENSURA | 60 |
| NUTRIÇÃO | 60 |
| LETRAS - ESPANHOL | 58 |
| FILOSOFIA | 57 |
| ARTES VISUAIS | 55 |
| BIBLIOTECONOMIA | 55 |
| GESTÃO DA INFORMAÇÃO | 54 |
| QUÍMICA | 50 |
| CIÊNCIA POLÍTICA | 50 |
| CINEMA E AUDIOVISUAL | 49 |
| JORNALISMO | 48 |
| ENGENHARIA DE MINAS | 47 |
| FÍSICA | 45 |
| PUBLICIDADE E PROPAGANDA | 43 |
| FONOAUDIOLOGIA | 40 |
| QUÍMICA INDUSTRIAL | 40 |
| GEOLOGIA | 37 |
| TERAPIA OCUPACIONAL | 35 |
| TEATRO | 35 |
| ENGENHARIA DE PRODUÇÃO | 34 |
| ARQUEOLOGIA | 30 |
| RÁDIO, TV E INTERNET | 30 |
| MUSEOLOGIA | 30 |
| CIÊNCIAS ATUARIAIS | 30 |
| ESTATÍSTICA | 30 |
| LETRAS - INGLÊS | 30 |
| HOTELARIA | 30 |
| ENGENHARIA BIOMÉDICA | 29 |
| EXPRESSÃO GRÁFICA | 29 |
| LETRAS | 27 |
| OCEANOGRAFIA | 25 |
| LETRAS - FRANCÊS | 13 |

### notasExtremas:
865.26 : maior nota;
391.94 : menor nota;

### relacaoNotas:
| intervalos | quantidade de alunos |
| ---------- | -------------------- |
| (300 - 400) | 1 |
| (400 - 500) | 50 |
| (500 - 600) | 845 |
| (600 - 700) | 3090 |
| (700 - 800) | 1214 |
| (800 - 900) | 147 |

![relacao-notas](https://github.com/wenderson-juvenal/analise-dados-ufpe-aprovados-2023/blob/main/images/relacao-notas.png)

### relacaoAlunosCotas:
| cota | quatidade de alunos |
| ---- | -------------------- |
| A0 | 2770 |
| L3 | 735 |
| L7 | 710 |
| L5 | 482 |
| L1 | 466 |
| L6 | 47 |
| L2 | 41 |
| L15 | 23 |
| L11 | 19 |
| L13 | 16 |
| L9 | 16 |
| L8 | 13 |
| L4 | 9 |
![relacao-alunos-cotas](https://github.com/wenderson-juvenal/analise-dados-ufpe-aprovados-2023/blob/main/images/relacao-alunos-cotas.png)

### relacaoNotasCotas:
| cota | media |
| ---- | ----- |
| A0 | 679.96 |
| L5 | 661.75 |
| L1 | 649.66 |
| L7 | 634.02 |
| L13 | 628.48 |
| L3 | 627.24 |
| L4 | 611.69 |
| L2 | 609.16 |
| L6 | 599.36 |
| L8 | 589.43 |
| L15 | 564.06 |
| L9 | 540.72 |
| L11 | 530.75 |
![relacao-notas-cotas](https://github.com/wenderson-juvenal/analise-dados-ufpe-aprovados-2023/blob/main/images/relacao-notas-cotas.png)

### relacaoMediaCursos:
| curso | media |
| ----- | ----- |
| ABI - ENGENHARIA | 644.91 |
| ADMINISTRAÇÃO | 663.07 |
| ARQUEOLOGIA | 591.27 |
| ARQUITETURA E URBANISMO | 654.52 |
| ARTES VISUAIS | 688.08 |
| BIBLIOTECONOMIA | 617.06 |
| BIOMEDICINA | 686.22 |
| CINEMA E AUDIOVISUAL | 684.29 |
| CIÊNCIA DA COMPUTAÇÃO | 771.37 |
| CIÊNCIA POLÍTICA | 636.84 |
| CIÊNCIAS ATUARIAIS | 608.4 |
| CIÊNCIAS BIOLÓGICAS | 641.49 |
| CIÊNCIAS BIOLÓGICAS - ÊNFASE EM CIÊNCIAS AMBIENTAIS | 627.06 |
| CIÊNCIAS CONTÁBEIS | 659.9 |
| CIÊNCIAS ECONÔMICAS | 670.38 |
| CIÊNCIAS SOCIAIS | 637.81 |
| DESIGN | 684.49 |
| DIREITO | 729.8 |
| EDUCAÇÃO FÍSICA | 608.64 |
| ENFERMAGEM | 698.27 |
| ENGENHARIA BIOMÉDICA | 689.27 |
| ENGENHARIA CARTOGRÁFICA E DE AGRIMENSURA | 569.59 |
| ENGENHARIA DA COMPUTAÇÃO | 751.24 |
| ENGENHARIA DE MINAS | 583.3 |
| ENGENHARIA DE PRODUÇÃO | 679.12 |
| ESTATÍSTICA | 609.42 |
| EXPRESSÃO GRÁFICA | 588.02 |
| FARMÁCIA | 679.7 |
| FILOSOFIA | 596.92 |
| FISIOTERAPIA | 689.29 |
| FONOAUDIOLOGIA | 676.63 |
| FÍSICA | 679.78 |
| GEOGRAFIA | 613.68 |
| GEOLOGIA | 592.87 |
| GESTÃO DA INFORMAÇÃO | 670.88 |
| HISTÓRIA | 656.7 |
| HOTELARIA | 581.34 |
| JORNALISMO | 689.45 |
| LETRAS | 660.56 |
| LETRAS - ESPANHOL | 602.27 |
| LETRAS - FRANCÊS | 593.99 |
| LETRAS - INGLÊS | 644.3 |
| LETRAS - PORTUGUÊS | 651.65 |
| MATEMÁTICA | 663.79 |
| MEDICINA | 795.22 |
| MUSEOLOGIA | 611.1 |
| NUTRIÇÃO | 676.07 |
| OCEANOGRAFIA | 602.59 |
| ODONTOLOGIA | 720.14 |
| PEDAGOGIA | 617.18 |
| PSICOLOGIA | 704.96 |
| PUBLICIDADE E PROPAGANDA | 704.88 |
| QUÍMICA | 605.28 |
| QUÍMICA INDUSTRIAL | 620.62 |
| RÁDIO, TV E INTERNET | 659.98 |
| SECRETARIADO | 592.93 |
| SERVIÇO SOCIAL | 631.17 |
| SISTEMAS DE INFORMAÇÃO | 779.54 |
| TEATRO | 626.06 |
| TERAPIA OCUPACIONAL | 649.39 |
| TURISMO | 601.29 |

