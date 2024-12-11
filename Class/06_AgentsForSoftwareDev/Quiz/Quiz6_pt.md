Pergunta 1
Qual não é um método eficaz de localização de arquivos?
"Verificar manualmente cada arquivo no diretório do projeto para encontrar arquivos relevantes"

Verificar manualmente cada arquivo em um diretório de projeto é altamente ineficiente e propenso a erros, tornando-o um método ineficaz para localização de arquivos. Eis o porquê:

Demorado:
Para repositórios grandes, revisar arquivos manualmente pode consumir uma quantidade impraticável de tempo e esforço.

Propenso a erros:
Erros humanos, como ignorar arquivos relevantes ou interpretar erroneamente o conteúdo, são mais prováveis com a verificação manual.

Falta de escalabilidade:
À medida que os projetos crescem em tamanho e complexidade, esse método se torna cada vez mais inviável.

Pergunta 2
O que o Pass@K mede?
"Após gerar K exemplos, verifica-se se pelo menos um deles satisfaz a especificação do código"

Pass@K é uma métrica usada para avaliar o desempenho de modelos generativos, especialmente no contexto da geração de código. Mede a probabilidade de pelo menos uma das K saídas geradas atender aos requisitos especificados ou passar em todos os casos de teste.

Relevância para geração de código:
Modelos de geração de código frequentemente produzem múltiplas soluções candidatas para um problema. O Pass@K avalia se pelo menos uma dessas soluções é correta, refletindo a confiabilidade do modelo.

Foco prático:
Em cenários reais, um usuário geralmente precisa de apenas uma saída correta. O Pass@K captura isso ao se concentrar no sucesso de pelo menos um candidato entre os K gerados.

Pergunta 3
Por que o vazamento de dados é um grande problema ao avaliar agentes de software?
"Pode levar a métricas de desempenho excessivamente otimistas que não refletem a verdadeira capacidade de generalização"

O vazamento de dados ocorre quando informações do conjunto de avaliação são incluídas inadvertidamente no processo de treinamento ou usadas de forma inadequada durante a avaliação. Isso é um problema crítico ao avaliar agentes de software porque:

Métricas de desempenho inflacionadas:
Se o agente tiver acesso a informações dos dados de teste, ele pode "trapacear" ao produzir saídas que parecem corretas sem generalizar realmente o problema subjacente. Isso resulta em métricas que superestimam as verdadeiras capacidades do agente.

Má generalização:
Um modelo afetado por vazamento de dados pode ter bom desempenho no conjunto de avaliação, mas falhar ao generalizar para dados não vistos em cenários reais, comprometendo sua confiabilidade e utilidade.

Insights enganosos:
Resultados excessivamente otimistas podem induzir desenvolvedores e stakeholders a decisões erradas sobre o uso do modelo ou esforços de refinamento.

Pergunta 4
Qual é um exemplo de como não mitigar preocupações de segurança de agentes de codificação?
"Usar ferramentas de formatação automática de código para garantir que a geração de código esteja bem organizada e fácil de ler, a fim de reduzir a probabilidade de erro humano"

Embora ferramentas de formatação automática de código sejam úteis para tornar o código mais legível e reduzir erros humanos durante a revisão manual, elas não abordam diretamente preocupações de segurança. Preocupações de segurança com agentes de codificação geralmente envolvem questões como segurança, ações não intencionais ou uso indevido de recursos, que não podem ser mitigadas por ferramentas de formatação.

Por que as outras opções são eficazes:

"Revisar ações após terem sido executadas para detectar e resolver quaisquer problemas de segurança ou atividades não autorizadas": Revisões pós-ação são essenciais para identificar e corrigir comportamentos não intencionais ou inseguros dos agentes de codificação.

"Restringir permissões e gerenciar tokens de acesso para garantir que usuários e aplicativos tenham apenas o nível mínimo de acesso necessário": Minimizar permissões reduz o risco de um agente realizar ações prejudiciais ou não autorizadas, limitando o impacto potencial.

"Isolar o ambiente de execução do agente para evitar que ações potencialmente prejudiciais afetem o sistema como um todo": Executar agentes em um ambiente isolado garante que quaisquer ações prejudiciais sejam contidas, protegendo o sistema mais amplo de consequências não intencionais.

Pergunta 5
O que é “code infilling”?
"O processo de gerar automaticamente as partes faltantes do código com base no contexto circundante"

Code infilling é uma técnica de IA generativa onde um modelo prevê e preenche as partes ausentes de um trecho de código usando o contexto ao redor. Essa capacidade é particularmente útil para tarefas como completar códigos parcialmente escritos, adicionar funcionalidades ausentes ou preencher códigos padrão.

Geração baseada em contexto:
O modelo utiliza o código existente antes e depois da lacuna para entender a lógica pretendida e gerar as partes faltantes relevantes.

Aplicações:
Frequentemente usado em editores de código e ambientes de desenvolvimento integrados (IDEs) para ajudar desenvolvedores a acelerar o processo de codificação e reduzir erros.

Valioso para desenvolvimento iterativo:
Code infilling é altamente útil em situações onde desenvolvedores escrevem código de forma incremental, permitindo uma conclusão contínua de seções incompletas.
