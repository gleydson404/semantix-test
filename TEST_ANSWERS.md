## Respostas do Teste

### 1) Qual o objetivo do comando cache em Spark?
De acordo com a documentação:

"By default, each transformed RDD may be recomputed each time you run an action on it. However, you may also persist an RDD in memory using the persist (or cache) method, in which case Spark will keep the elements around on the cluster for much faster access the next time you query it. There is also support for persisting RDDs on disk, or replicated across multiple nodes."

Isto é, em cada transformação de um RDD pode haver retrabalho para cada ação que eu desejar executar sobre esse RDD. Por isso, é recomendam persistir ou fazer cache dos dados. Tanto no caso de persistir, quanto no caso de fazer cache, o spark carrega os dados, o que vai fazer uma próxima ação ser muito mais rápida.

Concluindo, o comando cache tem o objetivo de persistir os dados na memória, para otimização de futuras queries.


PS.: o método cache(), é atalho para usar o armazenamento no nível padrão, que é a memória. Já o método persist() pode variar o nível de armazenamento.

http://spark.apache.org/docs/1.2.0/programming-guide.html#rdd-persistence

### 2) O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce. Por quê?
A mesma implementação em spark é mais rápida que em MapReduce primariamente por conta que spark trabalha com os dados em memória, ao contrário do MapReduce que pesiste os dados em disco. Outra rasão para a implementação em spark ser mais rápida, é que spark faz uso do [DAG](https://data-flair.training/blogs/dag-in-apache-spark/) que é uma generalização do MapReduce model, porém, muito mais rápida.

https://www.quora.com/What-makes-Spark-faster-than-MapReduce
https://data-flair.training/blogs/apache-spark-vs-hadoop-mapreduce/
https://data-flair.training/blogs/dag-in-apache-spark/

### 3) Qual é a função do SparkContext?
SparkContext é o core de uma aplicação spark. Quando o SparkContext é criado, é possível criar RDDs e rodar Serviços Spark. Essencialmente, o SparkContext é um cliente do ambiente de execução do Spark oferecendo as funções necessárias para executar uma plicação spark.

### 4) Explique com suas palavras o que é Resilient Distributed Datasets (RDD).
RDDs são abstrações de um conjunto de objetos imutáveis distribuios pelos clusters do spark. Geralmente essas abstrações são carregadas na memória.

Resilient: Se refere ao fato de ser tolerante a alguns erros, e capaz de se recuperar caso aconteça algum problema com algum cluster.


http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.rdd.RDD
https://jaceklaskowski.gitbooks.io/mastering-apache-spark/spark-rdd.html

### 5) GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?

Isso ocorre devido a como essas funções trabalham, apesar de produzirem o mesmo resultado. Usando reduceByKey as saídas com chaves em comum são combinadas cada partição antes de distribuir os dados. Em contrapartida, usando groupByKey todos os pares (chave, valor) são distribuídos, para depois serem combinados. Isso gera um fluxo de dados desnecessário na rede. Para um dataset muito grande, além do fluxo de dados na rede, combinar mais dados de uma vez é mais custoso. Outras funções são preferíveis sobre o groupByKey, como o combinedByKey e foldByKey.


https://databricks.gitbooks.io/databricks-spark-knowledge-base/content/best_practices/prefer_reducebykey_over_groupbykey.html


### 6) Explique o que o código Scala abaixo faz.
```
1 val textFile = sc.textFile("hdfs://...")
2 val counts = textFile.flatMap(line => line.split(" "))
3                     .map(word => (word, 1))
4                     .reduceByKey(_ + _)
5 counts.saveAsTextFile("hdfs://...")
```

Linha 1: Estamos carregando um arquivo texto com o método textFile, que por sua vez, lê o arquivo ou URI, como uma coleção de linhas.

Linha 2: Aplicamos o método chamado flatMap. que em suma, vai produzir uma saída com um vetor, onde cada palavra (separada por espaços) do dataset será um item do vetor.

Linha 3: Transformamos cada palavra em uma par, chave-vaor, colocando o valor 1 para cada palavra.

Linha 4: Finalmente, usando o reduceByKey, vai somar todas as palavras semelhantes em gerando uma lista semelhante a essa [('word1', 10), ('word2', 15), ('word3', 20)]. Essa lista será atribuída ao valor counts.
Linha 5: Salvamos o counts para um arquivo.


Em síntese o trecho de código em escala, aplica algumas transformações para construir um dataset (palavra, quantidade) de modo que palavra será uma string, e quantidade será um inteiro.

https://spark.apache.org/docs/latest/rdd-programming-guide.html
https://stackoverflow.com/questions/22350722/what-is-the-difference-between-map-and-flatmap-and-a-good-use-case-for-each
https://spark.apache.org/examples.html

