import numpy as np
import matplotlib.pyplot as plt

#learning_rate
hidden =  [i+1 for i in range(10)]
test_results = [
    [0.9757067639166572, 1.1540659004430374, 1.0760925625484377, 0.911632837646912, 0.9660842195559276 ],
    [0.9555076073720599 ,  0.8127109946645686, 1.042812466167193 ,0.9170183347890328 , 1.0666590231746294],
    [ 0.529605015260505, 0.6761346402987994,  0.7186310169978031, 0.7424355749772459, 0.197160426098097],
    [ 0.6034621842365437, 0.5074713395837549, 0.9298453615207629,0.5733895561879369 , 0.5655251495754217],
    [0.43149231452695175 , 0.5245384433105338, 0.32415129900098993,0.38123849587638203 ,0.48850447775182937 ],
    [ 1.975632706704806, 0.4014266252158604, 0.32030912238967507,0.2814122615471022 , 0.3787189160819848],
    [0.3385956638073126, 0.34390461459597205,0.31493921781760514 , 0.3258718552990798, 0.3279475697816954],
    [0.49562574115891833,  0.23284895846296264, 0.18839274967671635, 0.27542675151246393, 1.1208501061753735],
    [0.14531983682931987, 0.20157689467923035, 0.2648579047543649, 0.2650440565876181, 0.20638898156195234],
    [0.1480645967739433, 0.1710935547979969, 0.18360401578896351, 0.4979454294676951, 0.1028268021519159]
]

averages = [np.mean(results) for results in test_results]
plt.figure(figsize=(10, 7))
for i, results in enumerate(test_results):
    plt.scatter([hidden[i]] * len(results), results, alpha=0.6)

plt.plot(hidden, averages, color='green', linestyle='-',  linewidth=0.7)
plt.xlabel('Количество нейронов на скрытом слое')
plt.ylabel('Средняя абсолютная процентная ошибка')
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.3)
plt.show()



max_error =[0.0001, 0.001,  0.002,  0.003,  0.004,  0.005,  0.006, 0.007,  0.008,  0.009,  0.01]
test_results_max_error = [
    [199329, 199329, 199329],
    [59969, 34750, 19101],
    [23473, 27476, 31729],
    [25083, 14899, 53202],
    [19977, 22103, 13190],
    [15654, 16164, 28016],
    [20517, 12663, 14389],
    [7860, 1065, 8817],
    [12322, 9929, 9179],
    [7148, 6660, 12633],
    [7656, 7060, 2794]
]

averages_max_error = [np.mean(results) for results in test_results_max_error]
plt.figure(figsize=(10, 7))
for i, results in enumerate(test_results_max_error):
    plt.scatter([max_error[i]] * len(results), results, alpha=0.6)
plt.plot(max_error, averages_max_error, color='green', linestyle='-', linewidth=0.7)
plt.xlabel('Максимально допустимая ошибка')
plt.ylabel('Число итераций')
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.3)
plt.show()



learn_rate = [0.0001, 0.0002, 0.0003, 0.0004, 0.0005, 0.0006, 0.0007, 0.0008, 0.0009, 0.001]
test_results = [
    [20173, 34396, 10869],
    [8839, 7262, 6922],
    [12283, 6232, 2094],
    [3776, 2272, 1837],
    [2788, 3627, 4966],
    [2629, 2989, 2894],
    [1353, 1712, 3032],
    [1781, 1601, 2687],
    [776, 629, 2276],
    [791, 1106, 972]   
]

averages = [np.mean(results) for results in test_results]
plt.figure(figsize=(10, 7))
for i, results in enumerate(test_results):
    plt.scatter([learn_rate[i]] * len(results), results, alpha=0.6)
plt.plot(learn_rate, averages, color='green', linestyle='-', linewidth=0.7)
plt.xlabel('Коэффициент скорости обучения')
plt.ylabel('Число итераций')
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.3)
plt.show()



window = [1, 2, 3, 4, 5]
test_results = [
    [318, 182, 315],
    [330, 99, 128],
    [110, 180, 114],
    [76, 124, 101],
    [97, 171, 88]
]

averages = [np.mean(results) for results in test_results]
plt.figure(figsize=(10, 7))
for i, results in enumerate(test_results):
    plt.scatter([window[i]] * len(results), results, alpha=0.6)
plt.plot(window, averages, color='green', linestyle='-', linewidth=0.7)
plt.xlabel('Размер скользящего окна')
plt.ylabel('Число итераций')
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.3)
plt.show()