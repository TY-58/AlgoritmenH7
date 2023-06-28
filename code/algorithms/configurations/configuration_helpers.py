from __future__ import annotations

def make_configuration(configuraton_class: Greedy_configuration|Random_configuration, states_visited: list[int]) -> list[list[House, Battery]]:
    """
    Run try_configuration until a configuration is found.
    Return it if this is the case.
    """

    try_counter = 0
    configuraton_class.configuration = []

    while configuraton_class.configuration == []:
        configuraton_class.try_configuration()
        try_counter += 1

    states_visited.append(try_counter)
    return configuraton_class.configuration


def process_configuration(configuraton_class: Greedy_configuration|Random_configuration, configuration: list[list[House, Battery]]) -> None:
    """
    Adds all houses to the house_connections of the batteries that they've matched with.
    """

    for battery in configuraton_class.grid.batteries:
        for house in configuraton_class.grid.houses:
            if [house, battery] in configuration:
                battery.house_connections.append(house)
