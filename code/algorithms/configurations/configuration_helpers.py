from __future__ import annotations

def make_configuration(configuraton_class: Greedy_configuration|Random_configuration) -> list[list[House, Battery]]:
    """
    Run try_configuration until a configuration is found.
    Return it if this is the case
    """

    configuraton_class.configuration: list[list[House, Battery]] = []

    while configuraton_class.configuration == []:
        configuraton_class.try_configuration()

    return configuraton_class.configuration


def process_configuration(configuraton_class: Greedy_configuration|Random_configuration, configuration: list[list[House, Battery]]):
    """
    Adds all houses to the house_connections of the batteries that they've matched with.
    """

    for battery in configuraton_class.grid.batteries:
        for house in configuraton_class.grid.houses:
            if [house, battery] in configuration:
                battery.house_connections.append(house)
