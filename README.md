# Cliff-walking
## 程式簡介
* 利用 cliff walking 來比較強化學習( Reinforcement Learning )中 Q-learning 跟 SARSA 演算法之差異

* 實驗中 ε-greedy 固定為 0.1，因為RL聖經(Reinforcement learning: An introduction)上有一句話: 

  > **if ε were gradually reduced, then both methods would asymptotically converge to the optimal policy.**
### 範例圖
* **cliff walking 概念圖**  
![image](https://user-images.githubusercontent.com/93152909/210701183-d360d113-0a41-4dbc-88f7-6fa6fec7d8ac.png)

* **Q-Learning**  
![Q-Learning v s  SARSA](https://user-images.githubusercontent.com/93152909/210696601-66d77a5b-ae65-4520-b365-2a5838dec590.png)

* **Q-Learning偏向大膽的路徑，符合【Optimal path】**  
![Q-Learning Inference Path](https://user-images.githubusercontent.com/93152909/210696564-0e28d890-2a2e-44d0-8512-42402e5e8c37.png)

* **SARSA 偏向保守的路徑，符合【Safer path】**  
![SARSA Inference Path](https://user-images.githubusercontent.com/93152909/210696583-2e80dd5c-05c7-4c78-a298-f9ed6d819c53.png)

## Reinforcement Learning : Q-learning & SARSA
* 兩者都是強化學習中的TD-learning技術
* Q-learning 為 off-policy；SARSA 為 on-policy

![image](https://user-images.githubusercontent.com/93152909/210693355-dd3889ea-b8a3-4721-814b-d408699e5983.png)
圖片來源: https://www.youtube.com/watch?v=FhSaHuC0u2M
