sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')
while True:
    len_03 = len(sequence_0)
    x = set(sequence_0)
    if len_03 == len(x):
        print("Последовательность уникальна")
    else:
        print("Последовательность не уникальна.")

    len_03 = len(sequence_1)
    x = set(sequence_1)
    if len_03 == len(x):
        print("Последовательность уникальна.")
    else:
        print("Последовательность не уникальна.")
    
    len_03 = len(sequence_2)
    x = set(sequence_2)
    if len_03 == len(x):
        print("Последовательность уникальна.")
    else:
        print("Последовательность не уникальна.")
    
    len_03 = len(sequence_3)
    x = set(sequence_3)
    if len_03 == len(x):
        print("Последовательность уникальна/")
    else:
        print("Последовательность не уникальна.")
    break
