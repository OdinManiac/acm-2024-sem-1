from src.system import MyThreeWheeledRobot
import numpy as np
from regelum.simulator import CasADi
from regelum import callback
from regelum.system import ThreeWheeledRobotKinematic
import regelum as rg


def get_action(state):
    return np.array([[1, 0.1]])


@rg.main(config_name="main")
def main():

    # Define the initial state (initial position of the kinematic point).
    initial_state = np.array([[2.0, 2.0, 2.0]])  # Start at position (2, 2)

    # Initialize the kinematic point system.
    system = callback.detach(MyThreeWheeledRobot)()

    # Instantiate a simulator for the kinematic point system.
    simulator = CasADi(
        system=system, state_init=initial_state, time_final=4, max_step=0.1
    )

    state_history = [initial_state.flatten()]  # Store the initial state.
    times = [0.0]

    for _ in range(int(simulator.time_final / simulator.max_step)):
        action = get_action(
            simulator.state
        )  # Compute the action based on the current state.
        simulator.receive_action(action)  # Provide the action to the simulator.
        simulator.do_sim_step()  # Perform one simulation step.
        state_history.append(
            simulator.state.flatten()
        )  # Store the state after the step.
        times.append(simulator.time)

    state_history = np.array(
        state_history
    )  # Convert history to numpy array for plotting.
    times = np.array(times)  # Convert history to numpy array for plotting.

    print(state_history)


main()
