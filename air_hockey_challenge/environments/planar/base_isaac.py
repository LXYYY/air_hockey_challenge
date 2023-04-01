from legged_gym.envs.air_hockey.air_hockey import AirHockeyBase as BaseIsaac
from legged_gym.envs.air_hockey.air_hockey_config import AirHockeyCfg


class AirHockeyBaseIsaac:

    def __init__(self, gamma=0.99, horizon=500, timestep=1 / 1000., n_intermediate_steps=20, n_substeps=1,
                 n_agents=1, viewer_params={}):
        super().__init__()

