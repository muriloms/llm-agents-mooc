Pergunta 1
Qual NÃO é um nível de acesso existente para modelos fundacionais?
"Alterar os parâmetros neurais do modelo diretamente por meio de ajustes no hardware"

Alterar os parâmetros neurais do modelo diretamente por meio de ajustes no hardware não é um nível de acesso existente ou prático para modelos fundacionais. Os parâmetros neurais são definidos e ajustados por meio de processos de treinamento em nível de software, e não por manipulação direta do hardware.

Níveis de acesso existentes:

Consulta ao modelo via API sem visibilidade sobre sua mecânica interna:
Método comum de acesso, onde os usuários enviam requisições e recebem respostas sem acesso direto à arquitetura do modelo ou aos dados de treinamento (por exemplo, a API GPT da OpenAI).
Acesso à implementação do modelo, incluindo código-fonte e dados de treinamento:
Em projetos de código aberto ou pesquisas acadêmicas, alguns modelos fundacionais oferecem transparência ao disponibilizar detalhes de implementação e conjuntos de dados.
Uso de pesos pré-treinados para personalização ou ajuste fino:
Muitos modelos fundacionais (por exemplo, os modelos da Hugging Face) permitem que usuários baixem pesos pré-treinados para tarefas como aprendizado por transferência ou ajuste fino em domínios específicos.

Pergunta 2
Segundo o palestrante, qual NÃO foi um argumento para justificar a importância do acesso de código aberto?
"Ele garante que qualquer agente opere com alinhamento ético perfeito em todos os domínios"

A afirmação de que o acesso de código aberto garante alinhamento ético perfeito em todos os domínios não é um argumento realista para o acesso de código aberto. O alinhamento ético é uma questão complexa que depende de fatores como normas culturais, personalização específica do usuário e aplicação pretendida do modelo, e não pode ser garantido apenas por práticas de código aberto.

Argumentos que apoiam o acesso de código aberto:

"Permite o uso, estudo, modificação e compartilhamento do sistema para qualquer finalidade sem necessidade de permissões":
O acesso de código aberto oferece oportunidades irrestritas para inovação, colaboração e adaptação, promovendo o progresso tecnológico.
"Aborda desafios com APIs obsoletas, que impactam a reprodutibilidade na pesquisa":
Modelos de código aberto proporcionam estabilidade e reprodutibilidade na pesquisa, garantindo acesso contínuo à implementação do modelo, mesmo que APIs sejam alteradas ou descontinuadas.
"Oferece aos pesquisadores transparência para examinar criticamente e desafiar todos os aspectos do design do modelo com exploração irrestrita":
O acesso aberto permite que pesquisadores explorem a arquitetura, os dados e os algoritmos do modelo, promovendo melhor compreensão, crítica e aprimoramento.

Pergunta 3
No contexto da simulação de memória de agentes, qual dos seguintes NÃO é um critério útil para a recuperação de memória?
"Seleção aleatória para garantir padrões de recordação imparciais"

A seleção aleatória não é um critério útil para a recuperação de memória na simulação de memória de agentes porque a recuperação eficaz depende da relevância e alinhamento com os objetivos e o contexto do agente, e não do acaso.

Critérios úteis para a recuperação de memória:

Proximidade temporal com o momento presente:
Memórias temporariamente próximas à situação atual geralmente são mais relevantes e úteis para a tomada de decisão imediata.
Significância da memória em relação a eventos marcantes:
Memórias significativas, como aquelas ligadas a grandes eventos ou marcos, podem influenciar a tomada de decisões de longo prazo e padrões comportamentais.
Alinhamento contextual com a situação imediata do agente:
Memórias que se alinham ao contexto atual ajudam o agente a adaptar suas ações com base em experiências passadas relevantes à tarefa em questão.

Pergunta 4
Como os pesquisadores podem determinar se dois modelos foram treinados independentemente?
"Comparando a similaridade entre o modelo 1 e o modelo 2 com a similaridade entre o modelo 1 e a permutação do modelo 2"

Para determinar se dois modelos foram treinados independentemente, os pesquisadores frequentemente analisam o alinhamento dos pesos entre eles. Permutações dos pesos de um modelo são usadas como controle, pois os pesos podem se alinhar por coincidência devido à aleatoriedade da inicialização, mas, se os modelos foram treinados independentemente, o alinhamento deve ser menos similar do que com versões permutadas.

Por que esse método funciona:

Se dois modelos foram treinados independentemente, seus pesos apresentarão alinhamento aleatório em comparação ao alinhamento após a permutação.
Uma comparação sistemática permite que os pesquisadores identifiquem se a similaridade observada decorre de treinamento compartilhado ou alinhamento acidental dos pesos.
Por que as permutações são críticas:

Ao permutar os pesos de um modelo, garante-se que não haja alinhamento acidental devido a similaridades estruturais (por exemplo, inicialização ou dados de treinamento compartilhados).

Pergunta 5
O que NÃO foi uma sugestão do palestrante para resolver o “problema do cálculo”?
"Reduzir o uso de GPUs para diminuir o impacto ambiental"

Reduzir o uso de GPUs para diminuir o impacto ambiental não foi uma sugestão para resolver o "problema do cálculo." Em vez disso, o foco está em otimizar e dimensionar os recursos computacionais de forma responsável, sem comprometer o progresso na pesquisa de IA.

Sugestões feitas pelo palestrante:

Construção de leis de escalabilidade:
Leis de escalabilidade ajudam os pesquisadores a realizar experimentos menores e extrapolar resultados para modelos maiores, reduzindo a necessidade de computação extensiva durante os experimentos iniciais.
Aproveitar GPUs ociosas globalmente por meio de redes computacionais descentralizadas:
Redes descentralizadas otimizam a utilização de recursos ao disponibilizar GPUs ociosas para tarefas computacionais, reduzindo o desperdício e aumentando a eficiência.
Advogar por maior financiamento para iniciativas e infraestruturas de pesquisa pública:
Investimentos em financiamento público e infraestrutura democratizam o acesso a recursos computacionais, permitindo uma participação mais ampla na pesquisa de IA.
