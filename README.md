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
| (300, 400] | 1 |
| (400, 500] | 50 |
| (500, 600] | 845 |
| (600, 700] | 3090 |
| (700, 800] | 1214 |
| (800, 900] | 147 |
![relacao-notas](https://github.com/wenderson-juvenal/analise-dados-ufpe-aprovados-2023/blob/main/images/relacao-notas.png
)

