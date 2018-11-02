# SMF

O SMF ou STOCK MARKET FINDER é uma ferramenta de consulta fundamentalista em ações cotadas na B3 (Brasil, Bolsa, Balcão). Com ela é possível realizar a consulta dos principais indicadores fundamentalistas dos ativos, bem como obter de forma automática um checklist de perguntas relevantes para o tipo de análise em questão, tendo em vista obter resultados satisfatórios de acordo com o objetivo estipulado como meta na estratégia definida pelo investidor. Ainda, se pode obter as recomendações de compra, venda e permanência de posições dos ativos. 

O funcionamento da ferramenta SMF é simples. Depois de baixado, e seguido todos os passos explicativos para o bom funcionamento do código, basta executar o programa, depois escolher entre as opções de 1 a 9. Para novos usuários é recomendado que vejam a opção 8 (Ajuda) previamente.
Para todas as opções (exceto, opções 8 e 9), o programa irá requisitar qual o ticker do ativo o usuário deseja. O ticker deve ser preenchido conforme a descrição na bolsa, podendo ser digitado com letras maiúsculas ou minúsculas, exemplo: BIDI4/bidi4.

## Observações:

>(1)
AS RECOMENDAÇÕES SÃO FEITAS ATRAVÉS DE CRITÉRIOS GERAIS, PORÉM CADA INVESTIDOR DEVE POSSUIR UMA ESTRATÉGIA PRÓPRIA, VISANDO A MELHOR FORMA DE OBTENÇÃO DE PATRIMÔNIO, NO LONGO PRAZO, OU OBTENÇÃO DE LUCRO, NO CURTO PRAZO. POR ISSO, É SIGNIFICATIVO QUE A ESTRATÉGIA SEJA ELABORADA VISANDO A OBTENÇÃO DAS METAS, OBJETIVOS E RESULTADOS PRETENDIDOS PELO INVESTIDOR.

>(2)
A ANÁLISE DE RECOMENDAÇÃO PROCURA OFERECER UMA VISÃO GERAL SOBRE A SITUAÇÃO DA EMPRESA DE ACORDO COM CRITÉRIOS FUNDAMENTALISTAS. 
A PONTUAÇÃO BUSCA APRESENTAR AO INVESTIDOR CRITÉRIOS VALIOSOS QUE VALEM A PENA SEREM CONSIDERADOS NA HORA DA AQUISIÇÃO DA AÇÃO ANALISADA. RESSALTAMOS AINDA QUE RENTABILIDADE PASSADA NÃO É GARANTIA DE RENTABILIDADE FUTURA.                                           

>(3)
RECOMENDAMOS AINDA QUE ANTES DE QUALQUER TOMADA DE DECISÃO O INVESTIDOR REALIZE IMPRETERIVELMENTE TODAS AS ANÁLISES E CÁLCULOS DE FORMA MANUAL, AFIM DE QUE POSSA CONFERERIR OS DADOS APRESENTADOS PELO SOFTWARE.

>(4)
NÃO NOS RESPONSABILIZAMOS POR NENHUMA TOMADA DE DECISÃO PROVINDA DE QUALQUER TIPO OU FORMA DE RECOMENDAÇÃO DESTE SOFTWARE, A AQUISIÇÃO DE QUALQUER ATIVO, É DE INTERINA RESPONSABILIDADE APENAS, E SOMENTE APENAS, DO INVESTIDOR.                                     

## Instalação e Configuração do Software

* **BAIXAR O PROGRAMA**: Para baixar o código, aperte o botão de download ou clone via terminal ou cmd.:

   ```git
   git clone https://github.com/MrKruger/STOCK-MARKET-FINDER.git
   ```

* **BAIXAR O PYTHON**: Baixe e instale a última versão da linguagem python pelo site oficial. Não se esqueça de deixar a opção "Add Python 3.6 to PATH" marcada.: https://www.python.org/downloads/.


* **BAIXAR OS MÓDULOS NECESSÁRIOS**: Para que SMF funcione corretamente é necessário instalar os móduclos adicionais que estão no arquivo Requirements.txt. Para fazer isso você precisa abrir o terminal ou cmd na pasta aonde se encontra o arquivo e digitar o seguinte comando.:

   ```py
   pip install -r Requirements.txt
   ```

* **EXECUTAR O CÓDIGO PRINCIPAL**: Após baixar e instalar o python juntamente com os módulos necessários, abra o terminal ou o cmd e vá até a pasta aonde se encontra o código fonte já descompactado e digite.:

   ```py 
   python SMF.py
   ```

O código será executado.

É isso, boa diversão!    
