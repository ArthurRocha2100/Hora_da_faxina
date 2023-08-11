import os
import datetime
import shutil
import time

path = str(input('Informe o diretorio dos arquivos que seram apagados:'))
listFile = os.listdir(path)
cleaningTime = str(input('Defina a hora de limpeza da pasta (HH:MM):'))
def createFolderBackup():
    directory = path
    folderName = datetime.datetime.now().strftime('bkp_%d%m%Y')
    os.mkdir('{}\{}'.format(directory, folderName))

def moveFile():
    folderName = datetime.datetime.now().strftime('bkp_%d%m%Y')
    fate = ('{}\{}'.format(path, folderName))
    for file in listFile:
        if file != folderName:
            file = '{}\{}'.format(path, file)
            shutil.copy2(file, fate)

def compressFolder():
    folderName = datetime.datetime.now().strftime('bkp_%d%m%Y')
    fate = ('{}\{}'.format(path, folderName))
    shutil.make_archive(fate, 'zip', fate)
    shutil.rmtree(fate)

def clearFolder():
    folderName = datetime.datetime.now().strftime('bkp_%d%m%Y')

    for file in listFile:
        if file != folderName:
            os.remove('{}\{}'.format(path, file))


while True:
    now = datetime.datetime.now().strftime('%H:%M')

    if now == cleaningTime:
        createFolderBackup()
        moveFile()
        compressFolder()
        clearFolder()
        print('############## Limpeza realizada com sucesso ##############')
    time.sleep(40)
