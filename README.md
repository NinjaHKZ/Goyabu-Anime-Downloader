# Goyabu Anime Downloader
Uma ferramenta feita para **baixar episódios de animes do site <a href="https://www.goyabu.vip/" target="_blank">a</a> utilizando o ID do vídeo.**


![image](https://user-images.githubusercontent.com/100825381/178635415-064f45c1-b68d-40e8-beea-8dfc49c3656d.png)

## Requisitos:
  
  Para utilizar a ferramenta é necessário ter em mãos **alguns módulos Python**, são esses:
  - **Python 3 ou superior** (https://www.python.org/downloads/release/python-3105/)
  - **BeautifulSoup** (`pip install bs4`)
  - **aiohttp** (`pip install aiohttp`) 





## Utilização:

  Após a instação dos módulos, você pode dar dois clicks em cima do arquivo **scrapper.py** 
  ou com o CMD aberto no diretório onde está o script, basta digitar o comando **python scrapper.py** que o mesmo será
  executado.
  
  ### Configuração:
  * Após a execução do programa, inicialmente ele vai pedir o ID do episódio e o Lugar onde deseja salvar o download:
    <p>
      <img src='https://user-images.githubusercontent.com/100825381/178629668-4b66edbc-3413-4943-84f7-c16566efff63.PNG'><br>
      <sub>Observação: você pode passar mais de 2 IDs, contudo ele deve ser separado por vírgula.</sub><br><br>
    </p>
    
  * Após inserir as informações, o script vai começar a coletar os dados e iniciar o download dos vídeos de forma asyncrona:
    <p>
      <img src='https://user-images.githubusercontent.com/100825381/178630459-476c1b92-fd8c-4528-9ccc-5f49a01dbace.PNG'><br>
    </p>


## Metas de desenvolvimento:
  * [x] Donwload de Multiplos Vídeos Juntos.
  * [ ] Captura de Informações do Anime (nome, gênero, bio, ect...).
  * [ ] Procurar e Baixar os Episódios Pelo Nome do Anime.
  * [ ] Criar Comandos Para Execução Personalizada.
  * [ ] Auto Updater.
  * [ ] Adicionar a Tradução para o Idioma Inglês.
  * [ ] Interface Gráfica(Tkinter). 


## Considerações Finais:

  Como a ferramenta ainda está sendo desenvolvida, ainda existe algumas coisas que podem ser melhoradas e corrigidas, também existem
  outras features que podem ser adicionadas em atualizações futuras. 
  
  Caso encontre algum erro, sinta-se livre em informar para que seja corrigido <3

