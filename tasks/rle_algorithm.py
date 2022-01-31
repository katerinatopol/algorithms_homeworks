"""
RLE - самый простой алгоритм сжатия. Его суть состоит в замене повторяющихся данных образцом,
и количеством повтора образца. Алгоритм подходит для сжатия данных, имеющих большое количество повторений.
При сжатии учитывайте регистр.
Напишите программу, которая реализует RLE для строк, состоящих из букв латинского алфавита, не имеющих пробелы. 
Во входных данных только одна строка. 
Например: DDDDFFFFHHHHk → 4D,4F,4H,1k
"""