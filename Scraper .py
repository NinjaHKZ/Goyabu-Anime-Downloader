import aiohttp, json, asyncio, os, sys
from bs4 import BeautifulSoup



class WrapperAnime:
	async def Start(_id, _dir='') -> bool:
		global _Downloads, _DownloadingAnimes

		_Tasks = []
		os.system('cls' if sys.platform == 'win32' else 'clear')
		
		for i in _id:
			try:
				open(f'{_dir}{i}.mp4', 'r').close()
				print(f'arquivo {i}.mp4 já existe, pulando...')

			except FileNotFoundError:
				_Tasks.append(asyncio.create_task(WrapperAnime._ScrapperUrl('https://goyabu.vip/video/{}/'.format(i), i, _dir)))
				_Downloads += 1
				_DownloadingAnimes = f'{i}' if len(_DownloadingAnimes) == 0 else  f'{_DownloadingAnimes}, {i}'
		
		if len(_DownloadingAnimes) > 0:
			print(f'Numero de Downloads: {_Downloads}')
			print('Episódios para Download: {}\n'.format(_DownloadingAnimes))
			print('Iniciando Download...')
			
			await asyncio.gather(*_Tasks)
		
		print('\nFinalizado.\n')
		os.system('pause')
	

	async def _ScrapperUrl(_url, _id, _dir) -> str:
		global _Downloads

		async with aiohttp.ClientSession() as request:
			
			html = await request.get(_url) 

			html = BeautifulSoup(await html.text(), 'html.parser')
			
			try:
				_VideoUrl = html.find_all('div', itemprop="video")[0].div.a.get('href')
				print(_VideoUrl)
				html = await request.get(_VideoUrl)
				html = BeautifulSoup(await html.text(), 'html.parser')
				
				print(f'* Baixando {_id}.mp4'.title())
				anime = await request.get(json.loads(html.find_all('script')[2].text.split('var jw = ')[1]).get('file'))


				for i in range(2):
					try:
						with open(f'{_dir}{_id}.vidk', 'wb') as r:
							r.write(await anime.content.read())

						try:
							os.rename(f'{_dir}{_id}.vidk', f'{_dir}{_id}.mp4')

						except FileExistsError:
							print(f'um novo arquivo {_id}.mp4 foi identificado, removendo arquivo {_id}.vidk...')
							os.remove(f'{_dir}{_id}.vidk')


						_Downloads -= 1

						break

					except FileNotFoundError:
						os.mkdir(_dir)
						
						continue

				print(f'---> {_id}.mp4 foi Finalizado.'.title())
			
			except IndexError:
				print(f'Download de {_id}.Mp4 Falhou...')
				os.remove(f'{_id}.vidk')
				


if __name__ == "__main__":
	#_id = set(input('Insira o Id dos Animes >>> ').replace(' ', '').split(','))
	#_dir = input('Insira o local onde deseja salvar os animes >>> ')
	print('\n')
	_id = '130849'.split()
	_dir = 'anime/'
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
	aiohttp.TCPConnector(limit=2)	
	_DownloadingAnimes = ''
	_Downloads = 0

	asyncio.run(WrapperAnime.Start(_id, _dir))
