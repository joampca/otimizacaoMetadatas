import fnmatch
import os

###Adiciona metadados da segunda linha de áudio para português - PARAMOUNT +
caminho_entrada = f'.\\A converter'
caminho_saida = f'.\\Convertidos'

for raiz, pastas, arquivos in os.walk(caminho_entrada): # para cada iteração 
    for arquivo in arquivos:
        if fnmatch.fnmatch(arquivo, '*.mp4'):
            base_arquivo, tipo_arquivo = arquivo.split(".")
            comando = f'ffmpeg -i "{caminho_entrada}\\{arquivo}" -map 0 -c copy -metadata:s:a:0 language=eng -metadata:s:a:0 title="Inglês" -metadata:s:a:1 language=por -metadata:s:a:1 title="Português" "{caminho_saida}\\{base_arquivo}v2.{tipo_arquivo}"'
            os.system(comando)
