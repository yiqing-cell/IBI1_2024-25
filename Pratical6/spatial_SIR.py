# import necessarylibraries
import numpy as np
import matplotlib.pyplot as plt

size = 100  # 100x100 的网格
beta = 0.3  # 传染率
gamma = 0.05  # 恢复率
time_steps = 100  # 时间步数
# make array of all susceptble population
population = np.zeros((100,100))

outbreak = np.random.randint(0, size, 2)
population[outbreak[0], outbreak[1]] = 1

colors = {0: 'purple', 1: 'blue', 2: 'yellow'}

# 运行模型
for t in range(time_steps):
    new_population = population.copy()
    infected_indices = np.argwhere(population == 1)

    for x, y in infected_indices:
        # 让感染者恢复
        if np.random.rand() < gamma:
            new_population[x, y] = 2
        
        # 传播给邻居
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and population[nx, ny] == 0:
                if np.random.rand() < beta:
                    new_population[nx, ny] = 1
    
    population = new_population.copy()
    
    # 绘制热图
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.title(f'Time Step {t}')
    plt.pause(0.1)

plt.show()
