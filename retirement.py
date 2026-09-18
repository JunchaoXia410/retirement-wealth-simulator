def simulate(age, savings, info):
    """
    Simulate the retirement account balance for a given period.

    Args:
        age (int): Current age in months.
        savings (float): Current account balance.
        info (dict): Simulation settings containing:
            - months
            - contribution
            - rate_of_return

    Returns:
        tuple: Updated age and savings balance.
    """

    for _ in range(info["months"]):
        year = age // 12
        month = age % 12

        print(
            f"Age {year:3d} month {month:2d} "
            f"you have ${savings:,.2f}"
        )

        savings += savings * info["rate_of_return"]
        savings += info["contribution"]

        age += 1

    return age, savings


def retirement(
    start_age,
    initial_savings,
    working_info,
    retired_info
):
    """
    Simulate retirement savings during working and retirement periods.

    Args:
        start_age (int): Starting age in months.
        initial_savings (float): Initial retirement savings.
        working_info (dict): Working-period assumptions.
        retired_info (dict): Retirement-period assumptions.

    Returns:
        tuple: Final age and account balance.
    """

    age = start_age
    savings = initial_savings

    age, savings = simulate(
        age,
        savings,
        working_info
    )

    age, savings = simulate(
        age,
        savings,
        retired_info
    )

    return age, savings


def main():
    working_info = {
        "months": 489,
        "contribution": 1000,
        "rate_of_return": 0.045 / 12
    }

    retired_info = {
        "months": 384,
        "contribution": -4000,
        "rate_of_return": 0.01 / 12
    }

    start_age = 327
    initial_savings = 21345

    final_age, final_savings = retirement(
        start_age,
        initial_savings,
        working_info,
        retired_info
    )

    print("\nSimulation Complete")
    print(f"Final age: {final_age // 12} years {final_age % 12} months")
    print(f"Final savings: ${final_savings:,.2f}")


if __name__ == "__main__":
    main()