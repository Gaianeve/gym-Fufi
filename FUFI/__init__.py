from gym.envs.registration import register

register(
    id='FUFI-v0',
    entry_point='FUFI.envs:FUFIEnv',
    timestep_limit=1000,
)
