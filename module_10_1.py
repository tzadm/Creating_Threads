from threading import Thread
from datetime import datetime


def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as text_file:
        from time import sleep
        for i in range(1, word_count + 1):
            text_file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


time_start = datetime.now()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end = datetime.now()

time_res = time_end - time_start
print('Работа функций', time_res)

time_start_ = datetime.now()

thread_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thread_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thread_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thread_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

time_end_ = datetime.now()

time_res_ = time_end_ - time_start_

print('Работа потоков', time_res_)
