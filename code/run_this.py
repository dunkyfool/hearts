from SimEnv import Hearts
from RL import DQN

def run_hearts():
    step = 0
    for epoch in range(300):
        # Initialize environment
        state = env.reset()

        while True:
            # Refresh environment
            env.render()

            # DQN output action, based on the current state 
            action = RL.choose_action(state)

            # Take action and get next state, reward, and done
            state_, reward, done = env.step(action)

            # DQN saves replay experience
            RL.store_transition(state, action, reward, state_)

            # Control begining point to learn and frequency
            if (step > 200) and (step % 5 == 0):
                RL.learn()

            # Move to next state 
            state = state_

            # If terminated, then break
            if done:
                break
            step += 1

    # end of game
    print 'game over'
    env.destroy()


if __name__ == "__main__":
    env = Hearts()
    RL = DQN(env.n_actions, env.n_features,
                      learning_rate=0.01,
                      reward_decay=0.9,
                      e_greedy=0.9,
                      replace_target_iter=200,  # Every 200 steps change target_net's weighting
                      memory_size=2000,         # Replay memory size
                      # output_graph=True       # Flag of tensorboard
                      )
    env.after(100, run_hearts)
    env.mainloop()
    RL.plot_cost()                              # Loss curve
