def allegrova(name):
    print('Привет,', name, 'Привет,', name)


allegrova('Андрей!')


def allegrova_2(*song):
    print(*song)


allegrova_2('Ну что же ты стоишь,', 'Ну обними меня скорей!')
