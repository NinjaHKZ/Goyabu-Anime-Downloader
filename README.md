# Goyabu Anime Downloader
  Uma ferramenta feita para **baixar episódios de animes do site https://www.goyabu.vip/ utilizando o ID do vídeo.**
  
  ![image](https://user-images.githubusercontent.com/100825381/178635415-064f45c1-b68d-40e8-beea-8dfc49c3656d.png)<br><br>




## Antes de começar:
  O download pode demorar vários minutos dependendo da velocidade da sua internet, normalmente episódios com qualidade muito alta
  costumam ser bem grandes.
  
  

  <p align='center'>
    <img src='https://user-images.githubusercontent.com/100825381/178644493-dbfcd143-7d12-4635-ab49-a7b23bfd0462.png'>
    <img src='https://user-images.githubusercontent.com/100825381/178645053-2c467afe-f77b-4d24-8617-6aff996d5143.png'>
  </p><br><br>



## Requisitos:
  
  Para utilizar a ferramenta é necessário ter em mãos **alguns módulos Python**, são esses:
  - **Python 3 ou superior** (https://www.python.org/downloads/release/python-3105/)
  - **BeautifulSoup** (`pip install bs4`)
  - **aiohttp** (`pip install aiohttp`)<br><br>
  
  Para baixar e instalar os pacotes, digite o comando `pip install bs4 aiohttp` em seu CMD:
  
   ![image](https://user-images.githubusercontent.com/100825381/178647335-8c67b3c7-7d31-4a6f-92dc-2d935f15a24c.png)<br><br>




## Utilização:

  Após a instação dos módulos, você pode dar dois clicks em cima do arquivo **Scraper.py** 
  ou com o CMD aberto no diretório onde está o script, basta digitar o comando **python scrapper.py** que o mesmo será
  executado.
  
  ### Configuração:
  * Após a execução do programa, inicialmente ele vai pedir o ID do episódio e o Lugar onde deseja salvar o download, veja abaixo:
  
    O ID pode ser adquirido pela URL do episódio:

    URL | ID
    --- | --- |
    ht&#8203;tps://goyabu.vip/video/**130849**/ | **130849**
    ht&#8203;tps://goyabu.vip/video/**130841**/ | **130841**


    Agora com o seu ID copiado, vá para o programa e insira as informações que a ferramente lhe pede:
    
    <p>
      <img src='https://user-images.githubusercontent.com/100825381/178629668-4b66edbc-3413-4943-84f7-c16566efff63.PNG'><br>
      <sub>Observação: você pode passar mais de 2 IDs, contudo ele deve ser separado por vírgula.</sub><br><br>
    </p>



  * Após inserir as informações, o script vai começar a coletar os dados e iniciar o download dos vídeos de forma asyncrona:
    <p>
      <img src='https://user-images.githubusercontent.com/100825381/178630459-476c1b92-fd8c-4528-9ccc-5f49a01dbace.PNG'><br>
    </p><br><br>

## Considerações Finais:

  Como a ferramenta ainda está sendo desenvolvida, ainda existe algumas coisas que podem ser melhoradas e corrigidas, também existem
  outras features que podem ser adicionadas em atualizações futuras. 
  
  Caso encontre algum erro, sinta-se livre em informar para que seja corrigido <3

