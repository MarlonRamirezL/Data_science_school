external_counter = 0
internal_counter = 0

while external_counter < 5:
    while internal_counter < 6:
        print(external_counter, internal_counter)
        internal_counter += 1

        if internal_counter >= 3:
            break

    external_counter += 1
    internal_counter = 0