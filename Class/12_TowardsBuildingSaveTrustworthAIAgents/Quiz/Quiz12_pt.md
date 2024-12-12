Pergunta 1
Qual é a diferença entre Segurança em IA (AI Safety) e Proteção em IA (AI Security)?
"Segurança em IA envolve evitar que o sistema cause danos ao ambiente, enquanto Proteção em IA se concentra em proteger o sistema contra ameaças externas."

A distinção entre Segurança em IA e Proteção em IA está nos seus objetivos principais e áreas de preocupação:

Segurança em IA:

Foca em garantir que os sistemas de IA se comportem como previsto e não causem danos aos usuários, à sociedade ou ao meio ambiente.
Envolve abordar questões como comportamentos indesejados, tomada de decisões éticas e robustez contra falhas.
Proteção em IA:

Trata de proteger sistemas de IA contra atores mal-intencionados ou ameaças externas, como ataques cibernéticos, adulteração ou exploração.
Inclui a salvaguarda da integridade do sistema, dos dados e das operações.


Pergunta 2
Como exemplos adversariais são projetados para enganar classificadores de imagens baseados em aprendizado profundo?
"Introduzindo alterações sutis e imperceptíveis em uma imagem que alteram significativamente a previsão do modelo."

Exemplos adversariais são entradas cuidadosamente criadas para enganar classificadores de imagens baseados em aprendizado profundo, explorando suas vulnerabilidades. Essas entradas envolvem alterações sutis, imperceptíveis ao olho humano, mas que fazem com que o modelo classifique a imagem incorretamente.

Natureza das alterações:

São pequenas perturbações adicionadas aos valores dos pixels, geralmente otimizadas para maximizar o erro do modelo, mas permanecendo invisíveis para humanos.
Exploração das fraquezas do modelo:

Essas alterações exploram a sensibilidade das redes neurais profundas a padrões específicos de entrada, demonstrando como os limites de decisão podem ser manipulados.
Impacto:

Apesar das alterações mínimas, a saída do modelo pode ser drasticamente diferente, levando a classificações incorretas ou alta confiança em uma previsão errada.


Pergunta 3
Como a Segurança de Agentes baseados em LLMs (LLM Agent Safety) é diferente da Segurança típica de LLMs?
"A Segurança de Agentes de LLMs envolve proteger as ações que um agente pode realizar no mundo real, enquanto a Segurança típica de LLMs está relacionada ao conteúdo das saídas do modelo."

A diferença entre Segurança de Agentes de LLMs e Segurança típica de LLMs está no escopo e na aplicação:

Segurança de Agentes de LLMs:

Foca em comportamentos acionáveis de agentes que utilizam modelos de linguagem (LLMs) para interagir com o mundo real (por exemplo, controlar sistemas, executar comandos ou acessar ferramentas externas).
Garante que essas ações sejam seguras, alinhadas à intenção humana e não resultem em danos ou consequências indesejadas.
Exemplo: Prevenir que um agente faça alterações prejudiciais em um sistema que ele controla.
Segurança típica de LLMs:

Relacionada ao conteúdo gerado pelo LLM, como garantir que as saídas sejam precisas, imparciais, éticas e livres de materiais prejudiciais ou ofensivos.
Exemplo: Evitar geração de textos prejudiciais, desinformação ou linguagem tóxica em aplicações conversacionais.


Pergunta 4
Como funciona a injeção indireta de prompts?
"Um atacante insere instruções maliciosas que modificam o comportamento do modelo sem alterações na consulta do usuário, por exemplo, inserindo instruções maliciosas nos dados de treinamento."

A injeção indireta de prompts envolve a inserção de instruções maliciosas em dados externos que o modelo processa durante uma tarefa, levando a comportamentos alterados sem que o usuário modifique explicitamente sua consulta.

Mecanismo:

O atacante insere instruções prejudiciais ou enganosas em fontes de dados externas (como websites, documentos ou dados de treinamento) que o modelo pode acessar ou referenciar durante a execução.
O modelo, ao usar esses dados, executa inadvertidamente as instruções maliciosas embutidas pelo atacante.
Diferença-chave em relação à injeção direta:

Na injeção indireta, o vetor de ataque está nos dados que o modelo processa, não na consulta do usuário ou entrada direta. A consulta do usuário pode ser completamente inocente.
Exemplo:

Um atacante modifica uma página da web para incluir instruções prejudiciais. Um LLM com busca integrada acessa este conteúdo e executa as instruções embutidas, gerando saídas prejudiciais ou enganosas.


Pergunta 5
Explique a assimetria entre Ataques e Defesas em Segurança de IA.
"Os ataques têm alta tolerância ao fracasso e podem ser facilmente escalados, enquanto as defesas exigem confiabilidade e são intensivas em recursos, com baixa tolerância ao fracasso."

A assimetria entre ataques e defesas em segurança de IA surge da diferença nos objetivos e restrições de cada um:

Ataques:

Alta tolerância ao fracasso: Os atacantes podem tentar diversas estratégias, sabendo que apenas uma precisa ter sucesso para explorar uma vulnerabilidade.
Fácil escalabilidade: Muitos métodos de ataque, como exemplos adversariais ou injeções de prompts, podem ser automatizados e escalados a baixo custo.
Natureza proativa: Atacantes podem testar uma ampla variedade de abordagens para descobrir vulnerabilidades sem se preocupar com confiabilidade ou gasto de recursos.
Defesas:

Baixa tolerância ao fracasso: As defesas devem prevenir explorações em todos os casos possíveis. Um único fracasso pode ter consequências catastróficas.
Intensivas em recursos: Desenvolver defesas robustas frequentemente exige significativos recursos computacionais, humanos e financeiros, além de testes extensivos em vários cenários.
Natureza reativa: As defesas precisam antecipar e mitigar vetores de ataque potenciais, que podem ser um alvo móvel à medida que novas vulnerabilidades são descobertas.
