#Variables
area = 1
PI = 3.14
def run(arcA: float) -> float:
    # TODO
    global area
    area = arcA * PI
    return area


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(area)