import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


class Agent:

    def __init__(self, name, num_episodes):
        self.name = name

        # Keeps track of useful statistics
        self.episode_lengths = np.zeros(num_episodes)
        self.episode_rewards = np.zeros(num_episodes)

    def get_name(self):
        return self.name

    def plot_episode_stats(self, smoothing_window=10, noshow=False):
        # Plot the episode length over time
        fig1 = plt.figure(figsize=(10, 5))
        plt.plot(self.episode_lengths)
        plt.xlabel("Episode")
        plt.ylabel("Episode Length")
        plt.title("Episode Length over Time")
        if noshow:
            plt.close(fig1)
        else:
            plt.show(fig1)

        # Plot the episode reward over time
        fig2 = plt.figure(figsize=(10, 5))
        rewards_smoothed = pd.Series(self.episode_rewards).rolling(
            smoothing_window, min_periods=smoothing_window).mean()
        plt.plot(rewards_smoothed)
        plt.xlabel("Episode")
        plt.ylabel("Episode Reward (Smoothed)")
        plt.title("Episode Reward over Time (Smoothed over window size {})".format(
            smoothing_window))
        if noshow:
            plt.close(fig2)
        else:
            plt.show(fig2)

        # Plot time steps and episode number
        fig3 = plt.figure(figsize=(10, 5))
        plt.plot(np.cumsum(self.episode_lengths),
                 np.arange(len(self.episode_lengths)))
        plt.xlabel("Time Steps")
        plt.ylabel("Episode")
        plt.title("Episode per time step")
        if noshow:
            plt.close(fig3)
        else:
            plt.show(fig3)