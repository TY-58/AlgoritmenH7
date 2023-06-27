
def make_configuration(configuraton_class: Greedy_configuration|Random_configuration) -> list[list[House, Battery]]:
    """
    Run try_configuration until a configuration is found.
    Return it if this is the case
    """

    configuraton_class.configuration: list[list[House, Battery]] = []

    while configuraton_class.configuration == []:
        configuraton_class.try_configuration()

    return configuraton_class.configuration