## Прогнозирование оттока клиентов банка
   [ipynb](https://github.com/Alextost983/Porfolio/blob/main/leave_bank_client-main/leave_bank_client-main/leave_bank_client.ipynb)
## Описание
   Из «Бета-Банка» стали уходить клиенты. Каждый месяц. Немного, но заметно. Банковские маркетологи посчитали: сохранять текущих клиентов дешевле, чем привлекать новых.
На осносании исторических данных о расторжении договоров, посчитаем вероятность ухода клиента, для принятия соответствующих мер.

## Инструменты и навыки 
 - Phyton
 - Pandas
 - MatPlotLib
 - Seaborn
 - sklearn.preprocessing
 - sklearn.model_selection
 - sklearn.metrics
 - scipy.stats
 - sklearn.linear_model
 - sklearn.ensemble
## Общий вывод
- В результате первичного анализа, был выялен явный дисбаланс калассов отрицательного к положительному - 4 к 1.
- Выполнили этап предобработки данных, Осуществили заполнение пропусков, провели шкалирование, сделали One_hot_encoding.
- Модель логистической регресси до борьбы сдисбалансом, показала результат 0.33, а модель случайного леса с рекзултативностью метрики f1 - 58%.
- Сделали upsampling положительного класса случайного леса, благодаря чему удалось достич показателя f1 меры 60%. Dowmsampling оказался более эффективен.
- Проверка на тестовой выборке показала, что не изменилась метрика f1 и осталась 60%.

###
