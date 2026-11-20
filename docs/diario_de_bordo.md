## Semana 1 — 14/11/2026

**Responsável:** Manuel
**Etapa:** definição formal da linguagem (docs/gramatica.md)

**O que foi feito:** alfabeto e tabela de tokens, gramática EBNF com
precedência e associatividade (incluindo while e for), restrições
semânticas, tabela de transições do lexer e 5 programas de exemplo.

**Uso de IA:** Claude Sonnet 5.5, para gerar um rascunho inicial de
tokens, EBNF, tabela de transições e exemplos justificados, a partir
da especificação do enunciado.

**O que revisamos/alteramos:** [preencher: o que você conferiu, mudou
ou descartou e por quê]

**Decisões em aberto:** comentário de bloco (/* */) incluído para dar
sentido ao teste "comentário não fechado"; comparação não associativa;
sem menos unário. [confirmar com o grupo/professora]

**Próximos passos:** implementar src/lexer.py a partir da tabela de
transições.

## Atualização — 20/11/2026

**Responsável:** Manuel

**Etapa:** Análise léxica e elaboração do relatório.

**O que foi feito:** Estudei o funcionamento do Lexer e sua relação com a tabela de transições do AFD. Revisei os conceitos de expressões regulares, AFN, AFD, transições ε, construção dos subconjuntos e minimização. Também preparei a seção de Análise Léxica para o relatório do grupo.

**Uso de IA:** O Claude Sonnet 5.5 foi utilizado para auxiliar na geração do código e da documentação do Lexer. O ChatGPT (GPT-6) foi utilizado para estudar os conceitos teóricos, resolver exercícios e revisar o texto do relatório.

**O que foi revisado:** Conferi as regras de reconhecimento dos tokens, o maior casamento, as palavras reservadas e o tratamento de entradas inválidas, como `1x`.

**Testes realizados:** Executei `python3 -m pytest tests/ -v`. Os 34 testes automatizados do projeto foram aprovados.

**Dificuldades encontradas:** Tive dificuldades para compreender as transições ε e a transformação de AFN em AFD. Revisei esses conceitos por meio de exemplos e exercícios.

**Próximos passos:** Conferir a versão final do relatório com o grupo e preparar a apresentação do projeto.