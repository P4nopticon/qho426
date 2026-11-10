def likelihood_min_max():
    likelihoods = (50, 38, 27, 99, 4)
    return (min(likelihoods), max(likelihoods))


def run_task2():
    min_val, max_val = likelihood_min_max()
    print(f"Minimum likelihood of falling: {min_val}%")
    print(f"Maximum likelihood of falling: {max_val}%")


if __name__ == "__main__":
    run_task2()