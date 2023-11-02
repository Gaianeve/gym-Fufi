# FUFI environment
The environment for our real life Cart-Pole.
## Description
A pole is attached by an un-actuated joint to a cart, which moves along a track with friction.
The pendulum is placed upright on the cart and the goal is to balance the pole by applying forces in the left and right direction on the cart.

****
                                                                Action Space

The action is a `ndarray` with shape `(1,)` which can take values in the interval `{F_max, F_max}` indicating the magnitude of the force the cart is pushed with. Basically we take a discrete action space, in which the minimum corresponds to -F_max - AKA the maximum force our engine can give - and +F_max as the maximum. The steps between one value and the other is the minimum force our engine can produce, let's say 1 for the time being. Sign - and + refers to our sistem of reference.

    | Num  | Action                              |
    |------|-------------------------------------|
    |   0  | Push cart to the left with F=10 N   |
    |   1  | Push cart to the left with F=9.9 N  |
    | ---- | ----------------------------------- |
    |  10  |      Push cart with null force      |
    | ---- | ----------------------------------- |
    |  19  | Push cart to the right with F=9.9 N |
    |  20  | Push cart to the right with F=10 N  |

In RL the action space has to be defined with positive values, so the index of each action has to be mapped into the value of the force.
Given this, doing some math, we get:
*  `Action space length` : 2*F_max/sensibility +1
*  `Action index of null force` : F_max
*  `Force vector`        : -F_max + action_index*sensibility
    
****
                                                                Observation Space

The observation is a `ndarray` with shape `(4,)` with the values corresponding to the following positions and velocities:

    |Num|   Observation  |    Min     |    Max    |
    |---|----------------|------------|-----------|
    | 0 |  Pole a_t      | -F_max/m_p | F_max/m_p |
    | 1 | Pole Theta     | ~ (-24°)   | ~ (24°)   |
    | 2 | Pole Theta dot |    -Inf    |   Inf     |

*Note:* While the ranges above denote the possible values for observation space of each element, it is not reflective of the allowed values of the state space in an unterminated episode. In particular:

-The cart x-position (index 0) can be take values between `(-4.8, 4.8)`, but the episode terminates if the cart leaves the `(-2.4, 2.4)` range, that means it hits the end of the track.

-The pole angle can be observed between `(-.418, .418)` radians `(or ±24°)`, but the episode terminates if the pole angle is not in the range `(-.0349, .0349)` `(or ±2°)`.

****
                                                                              Rewards

Since the goal is to keep the pole upright for as long as possible, a reward of `+1` for every step taken,including the termination step, is allotted. The threshold for rewards is raised to 1000.
****
                                                                              Manner
There are 2 ways implemented in this code:
1. *Real world* : we take the real FUFI and attach it to the Arduino. The states are measured and imported from a `.txt` file.

2. *Ideas world* : simulation mode. The states are computed using the motion equations of the sistem.
****
                                                                          Starting State

In simulation mode all observations are assigned a uniformly random value in `(-0.05, 0.05)`, in real world mode we take as initial state the inital measures.
****
                                                                          Episode End

The episode ends if any one of the following occurs:
1. Termination: Pole Angle is greater than ±2°;
2. Termination: Cart Position is greater than ±2.4,that is when the center of the cart reaches the edge of the display;
3. Truncation: Episode length is greater than 1500;
****
                                                                           Arguments
1. `gym.make('Fufi')`
