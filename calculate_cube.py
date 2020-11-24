def calculate_cube():
    """ Prints the number of bricks and dimensions of the resulting cube
    where the volume equals the surface area """
    # initial values for edge_length, volume and area
    edge_length = 1
    volume = 1
    area = 6
    while volume != area:
        edge_length = edge_length + 1
        volume = edge_length ** 3
        area = 6 * edge_length ** 2
    print(f"Number of bricks: {volume}")
    print(f"Dimensions: {edge_length} x {edge_length} x {edge_length}")


calculate_cube()
