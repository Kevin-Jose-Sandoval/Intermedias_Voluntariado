import os
import shutil

path_downloads = "C:\\Users\\KEVINSANDOVAL\\Desktop\\Voluntariado\\taller1\\Descargas\\"

text_extensions = ('.txt', '.doc', '.docx', '.pptx', '.pdf')
video_extensions = ('.mp4', '.mkv', '.flv', '.wmv')
audio_extensions = ('.mp3', '.wma', '.wav', '.flac')
image_extensions = ('.jpg', '.png', '.jpeg', '.gif', '.ico', '.svg')
compressed_extensions = ('.zip', '.rar')

def order(file, extension):

    for ext in text_extensions:
        if extension == ext:
            shutil.move(path_downloads + file, path_downloads + 'Texto')

    for ext in video_extensions:
        if extension == ext:
            shutil.move(path_downloads + file, path_downloads + 'Videos')

    for ext in audio_extensions:
        if extension == ext:
            shutil.move(path_downloads + file, path_downloads + 'Audios')

    for ext in image_extensions:
        if extension == ext:
            shutil.move(path_downloads + file, path_downloads + 'Imagenes')

    for ext in compressed_extensions:
        if extension == ext:
            shutil.move(path_downloads + file, path_downloads + 'Comprimidos')

    if extension != '':
        try:
            shutil.move(path_downloads + file, path_downloads + 'Otros')
        except:
            pass

    
def main():
    for file in os.listdir(path_downloads):
        
        try:
            ext = os.path.splitext(file)[1]
            order(file, ext)
        except:
            print('No fue posible mover el archivo {}\n'.format(file))

    print('Proceso terminado')


if __name__ == '__main__':
    main()