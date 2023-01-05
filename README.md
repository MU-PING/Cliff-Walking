# Cliff-walking
## 程式簡介
* 利用 cliff walking 來比較強化學習( Reinforcement Learning )中 Q-learning 跟 SARSA 演算法之差異

### 範例圖與說明
* **cliff walking 概念圖**  
![image](https://user-images.githubusercontent.com/93152909/210701183-d360d113-0a41-4dbc-88f7-6fa6fec7d8ac.png)

* **Q-Learning v.s.  SARSA**  
  * 訓練過程中 ε-greedy 固定為 0.1
    * **Q-Learning** : 用最大值估計來更新，因此有學習到全局最優的能力【Optimal path】，所以有更好的最終性能。
    * **SARSA** : 基於當前policy的動作選擇，用這個樣本更新當前的policy，直觀簡單但可能收斂到局部最優【Safer path】。

  * RL聖經(Reinforcement learning: An introduction)上有一句話: 
  
    > **if ε were gradually reduced, then both methods would asymptotically converge to the optimal policy.**
    
      * 簡單來說，若 ε 在訓練過程中持續減少，最後**Q-Learning**、**SARSA**應該都會收斂到【Optimal path】
      * 這樣情況下兩者最終結果會差不多，我們只能說在「訓練過程中」，**SARSA**比**Q-Learning**更保守
      * SARSA更保守的原因是更新過程中，如果在懸崖邊，下一個狀態若是隨機選取，則可能會掉下懸崖，因此當前狀態的Q值會降低，使得Agent不願意走靠近懸崖的路徑；Q-learning在懸崖邊選取的下一步是最優路徑，所以不會有這個問題，而更偏向走懸崖邊。
      * 下圖Q-Learning的平均Reward會低於SARSA就是因為Q-Learning喜歡走在懸崖邊，容易死亡獲得負獎勵。

![Q-Learning v.s. SARSA](https://user-images.githubusercontent.com/93152909/210696601-66d77a5b-ae65-4520-b365-2a5838dec590.png)

* **Q-Learning 偏向大膽的路徑，符合【Optimal path】**，符合上述推論  
![Q-Learning Inference Path](https://user-images.githubusercontent.com/93152909/210696564-0e28d890-2a2e-44d0-8512-42402e5e8c37.png)

* **SARSA 偏向保守的路徑，符合【Safer path】**，符合上述推論  
![SARSA Inference Path](https://user-images.githubusercontent.com/93152909/210696583-2e80dd5c-05c7-4c78-a298-f9ed6d819c53.png)

## Reinforcement Learning : Q-learning & SARSA
* 兩者都是強化學習中的TD-learning技術
* Q-learning 為 off-policy；SARSA 為 on-policy

![image](https://user-images.githubusercontent.com/93152909/210693355-dd3889ea-b8a3-4721-814b-d408699e5983.png)
圖片來源: https://www.youtube.com/watch?v=FhSaHuC0u2M

### 參考
* https://blog.51cto.com/u_15642578/5305128
* https://blog.csdn.net/weixin_37895339/article/details/74937023
