Для продакшена на заметку
=========================

Так как проект живет на сервере вместе с другим сайтом, всё работает на python 2.7, потому что пересобирать UWSGI под работу с двумя версиями - геморрой. 

Так же не стоит раздувать проект больше чем в один файл, так как UWSGI начинает ругаться на то, что не может корректно производить импорты. Можно было бы попробовать сделать по уму, но я пытался сутки всё это реанимировать и больше заморачиваться не хочется. Плюс сервис UWSGI очень странно ребутится и в итоге выяснилось, что для проверки корректности работы, проще перезапустить полностью сервер.

Надеюсь я из будущего прочитаю это и не буду тратить на фиксы опять столько времени.

Работает - не трогай (с).
