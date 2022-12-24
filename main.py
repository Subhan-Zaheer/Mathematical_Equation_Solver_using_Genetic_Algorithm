import random
import numpy as np

# -------------------------- What is Genetic ALgorithm? --------------------------------------
# This code can solve linear quadratic and cubic equations using genetic algorithm.
# if we talk about Genetic Algorithm. It is an algorithm impressed by human's genetic system.
# It generates a population like genes in Human.
# Then it will apply a fitness function to check it can solve our problem.
# If fitness function does not give us exact answer then we will move on to Selection process.
# In selection, population who deserves the most should be selected.
# Then it will perform cross over between population.
# After that it will mutate the value of population.
# Then the resultant set will the population for our next iteration or generation and this process repeats.
# It's a short description of Genetic Algorithm. If you want to study it in detail then you can
# study from any online platform like youtube and any other.



equation_type = int(
    input("Enter the type of equation.\n1 for linear equation.\n2 for quadratic equation.\n3 for cubic equation."))
if equation_type == 1:  # If it is linear equation.1
    variable_number = int(
        input("Enter number of variables.\n1 for one variable.\n2 for two variables.\n3 for three varaibles."))
    if variable_number == 1:
        x_coefficient = int(input("Enter value of x coeffiecient : "))
    elif variable_number == 2:
        x_coefficient = int(input("Enter value of x coefficient : "))
        y_coefficient = int(input("Enter value of y coefficient : "))
    elif variable_number == 3:
        x_coefficient = int(input("Enter value of x coefficient : "))
        y_coefficient = int(input("Enter value of y coefficient : "))
        z_coefficient = int(input("Enter value of z coefficient : "))

elif equation_type == 2:  # If it is quadratic equation.
    variable_number = int(
        input("Enter number of variables.\n1 for one variable.\n2 for two variables.\n3 for three varaibles."))
    if variable_number == 1:
        # For example 3x^2 + 5x =12
        x_coefficient = int(input("Enter value of x coeffiecient : "))
        x_coefficient_with_1degree = int(input("Enter value of x coefficient with 1 power in quadratic equation : "))
    elif variable_number == 2:
        # For example 3x^2 + 5x + 2y^2 + y = 12
        x_coefficient = int(input("Enter value of x coefficient : "))
        x_coefficient_with_1degree = int(input("Enter value of x coefficient with 1 power in quadratic equation : "))
        y_coefficient = int(input("Enter value of y coefficient : "))
        y_coefficient_with_1pow = int(input("Enter value of y coefficient with 1 power in quadratic equation : "))
    elif variable_number == 3:
        # For example 3x^2 + 5x + 2y^2 + y + 5z^2 + 9z = 12
        x_coefficient = int(input("Enter value of x coefficient : "))
        x_coefficient_with_1degree = int(input("Enter value of x coefficient with 1 power in quadratic equation : "))
        y_coefficient = int(input("Enter value of y coefficient : "))
        y_coefficient_with_1pow = int(input("Enter value of y coefficient with 1 power in quadratic equation : "))
        z_coefficient = int(input("Enter value of z coefficient : "))
        z_coefficient_with_1pow = int(input("Enter value of z coefficient with 1 power in quadratic equation : "))

    pass

elif equation_type == 3:  # If it is cubic equation.
    variable_number = int(
        input("Enter number of variables.\n1 for one variable.\n2 for two variables.\n3 for three varaibles."))
    if variable_number == 1:
        # 4x^3 + 3x^2 + 5x = 12
        x_coefficient = int(input("Enter value of x coeffiecient : "))
        x_coefficient_with_2degree = int(input("Enter value of x coefficient with 2 power in cubic equation : "))
        x_coefficient_with_1degree = int(input("Enter value of x coefficient with 1 power in cubic equation : "))
    elif variable_number == 2:
        # 4x^3 + 3x^2 + 5x + y^3 + 2y^2 + y = 12
        x_coefficient = int(input("Enter value of x coefficient : "))
        x_coefficient_with_2degree = int(input("Enter value of x coefficient with 2 power in cubic equation : "))
        x_coefficient_with_1degree = int(input("Enter value of x coefficient with 1 power in cubic equation : "))

        y_coefficient = int(input("Enter value of y coefficient : "))
        y_coefficient_with_2pow = int(input("Enter value of y coefficient with 2 power in cubic equation : "))
        y_coefficient_with_1pow = int(input("Enter value of y coefficient with 1 power in cubic equation : "))
    elif variable_number == 3:
        # 4x^3 + 3x^2 + 5x + y^3 + 2y^2 + y + 6z^3 + 5z^2 + 9z = 12
        x_coefficient = int(input("Enter value of x coefficient : "))
        x_coefficient_with_2degree = int(input("Enter value of x coefficient with 2 power in cubic equation : "))
        x_coefficient_with_1degree = int(input("Enter value of x coefficient with 1 power in cubic equation : "))

        y_coefficient = int(input("Enter value of y coefficient : "))
        y_coefficient_with_2pow = int(input("Enter value of y coefficient with 2 power in cubic equation : "))
        y_coefficient_with_1pow = int(input("Enter value of y coefficient with 1 power in cubic equation : "))

        z_coefficient = int(input("Enter value of z coefficient : "))
        z_coefficient_with_2pow = int(input("Enter value of y coefficient with 2 power in cubic equation : "))
        z_coefficient_with_1pow = int(input("Enter value of z coefficient with 1 power in cubic equation : "))

constant = int(input("Enter constant : "))

MUTATION_RATE = 1.0


def generate_population():
    population = []

    for i in range(8):
        temp_list = []
        if equation_type == 1:
            # print("Equation type 1")
            if variable_number == 1:
                # print("Equation type 1 and variable 1")
                x = int(10 * random.uniform(-20, 20))
                population.append(x)
            elif variable_number == 2:
                # print("Equation type 1 and variable type 2.")
                x = int(10 * random.uniform(-20, 20))
                # print(f"x is {x}")
                y = int(random.uniform(-20, 20))
                temp_list.append(x)
                temp_list.append(y)
                population.append(temp_list)
            elif variable_number == 3:
                # print("Equation type 1 and variable type 2.")
                x = int(10 * random.uniform(-10, 10))
                # print(f"x is {x}")
                y = int(random.uniform(-10, 10))
                z = int(random.uniform(-10, 10))
                temp_list.append(x)
                temp_list.append(y)
                temp_list.append(z)
                population.append(temp_list)

        elif equation_type == 2 or equation_type == 3:
            if equation_type == 2:
                negative_val_threshold = -10
                positive_val_threshold = 10
            elif equation_type == 3:
                negative_val_threshold = -8
                positive_val_threshold = 8
            if variable_number == 1:
                # print("Equation type 2 and variable1")
                pass
                x = int(10 * random.uniform(negative_val_threshold, positive_val_threshold))
                #                 y = int(10*random.uniform(-10, 10))
                population.append(x)
            elif variable_number == 2:
                # print("Equation 2 and variable 2")
                x = int(10 * random.uniform(negative_val_threshold, positive_val_threshold))
                y = int(10 * random.uniform(negative_val_threshold, positive_val_threshold))
                temp_list.append(x)
                temp_list.append(y)
                population.append(temp_list)
            elif variable_number == 3:
                # print("Equation 2 and variable 2")
                x = int(10 * random.uniform(negative_val_threshold, positive_val_threshold))
                y = int(10 * random.uniform(negative_val_threshold, positive_val_threshold))
                z = int(10 * random.uniform(negative_val_threshold, positive_val_threshold))
                temp_list.append(x)
                temp_list.append(y)
                temp_list.append(z)
                population.append(temp_list)

    # print(f"Population is : {population}")

    return population


def fitness_function(population):
    my_values = {}
    my_keys = {}
    temp1 = 0
    temp2 = 0
    if equation_type == 1:
        if variable_number == 1:
            # print("Linear equation with 1 variable.")
            for i in range(8):
                x = population[i]
                answer = round((x_coefficient * x), 2) - constant
                my_values[i] = round(abs(answer - 0), 2)
                my_keys[i] = population[i]
        elif variable_number == 2:
            # print("Linear equation with 2 variables.")
            for i in range(8):
                x = population[i][0]
                y = population[i][1]
                temp1 = round(x_coefficient * x, 2)
                temp2 = round(y_coefficient * y, 2)
                answer = (temp1 + temp2) - constant
                my_values[i] = round(abs(answer - 0), 2)
                my_keys[i] = population[i]
        elif variable_number == 3:
            # print("Linear equation with 3 variables.")
            for i in range(8):
                x = population[i][0]
                y = population[i][1]
                z = population[i][2]
                temp1 = round(x_coefficient * x, 2)
                temp2 = round(y_coefficient * y, 2)
                temp3 = round(z_coefficient * z, 2)
                answer = (temp1 + temp2 + temp3) - constant
                my_values[i] = round(abs(answer - 0), 2)
                my_keys[i] = population[i]

    elif equation_type == 2:
        if variable_number == 1:
            # print("Quadratic equation with 1 variable.")
            for i in range(8):
                x = population[i]
                answer = round(((x_coefficient * x * x) + (x_coefficient_with_1degree * x)), 2) - constant
                my_values[i] = round(abs(answer - 0), 2)
                my_keys[i] = population[i]
        elif variable_number == 2:
            # print("Quadratic equation with 2 variables.")
            for i in range(8):
                x = population[i][0]
                y = population[i][1]
                temp1 = round(x_coefficient * x * x, 2)
                temp2 = round(x_coefficient_with_1degree * x, 2)
                temp3 = round(y_coefficient * y * y, 2)
                temp4 = round(y_coefficient_with_1pow * y, 2)
                answer = (temp1 + temp2 + temp3 + temp4) - constant
                my_values[i] = round(abs(answer - 0), 2)
                my_keys[i] = population[i]
        elif variable_number == 3:
            # print("Linear equation with 3 variables.")
            for i in range(8):
                x = population[i][0]
                y = population[i][1]
                z = population[i][2]
                temp1 = round((x_coefficient * x ** 2) + (x_coefficient_with_1degree * x ** 1), 3)
                temp2 = round((y_coefficient * y ** 2) + (y_coefficient_with_1pow * y ** 1), 3)
                temp3 = round((z_coefficient * z ** 2) + (z_coefficient_with_1pow * z ** 1), 3)
                answer = (temp1 + temp2 + temp3) - constant
                my_values[i] = round(abs(answer - 0), 2)
                my_keys[i] = population[i]

    elif equation_type == 3:
        if variable_number == 1:
            # print("Cubic equation with 1 variable.")
            for i in range(8):
                x = population[i]
                answer = round(((x_coefficient * x ** 3) + (x_coefficient_with_2degree * x ** 2) + (
                            x_coefficient_with_1degree * x)), 2) - constant
                my_values[i] = round(abs(answer - 0), 2)
                my_keys[i] = population[i]
        elif variable_number == 2:
            # print("Cubic equation with 2 variables.")
            for i in range(8):
                x = population[i][0]
                y = population[i][1]
                temp1 = round(x_coefficient * x ** 3, 3)
                temp2 = round(x_coefficient_with_2degree * x ** 2 + x_coefficient_with_1degree * x, 3)
                temp3 = round(y_coefficient * y ** 3, 3)
                temp4 = round(y_coefficient_with_2pow * y ** 2 + y_coefficient_with_1pow * y, 3)
                answer = (temp1 + temp2 + temp3 + temp4) - constant
                my_values[i] = round(abs(answer - 0), 3)
                my_keys[i] = population[i]
        elif variable_number == 3:
            # print("Cubic equation with 3 variables.")
            for i in range(8):
                x = population[i][0]
                y = population[i][1]
                z = population[i][2]
                temp1 = round((x_coefficient * x ** 3) + (x_coefficient_with_2degree * x ** 2) + (
                            x_coefficient_with_1degree * x ** 1), 4)
                temp2 = round(
                    (y_coefficient * y ** 3) + (y_coefficient_with_2pow * y ** 2) + (y_coefficient_with_1pow * y ** 1),
                    4)
                temp3 = round(
                    (z_coefficient * z ** 3) + (z_coefficient_with_2pow * z ** 2) + (z_coefficient_with_1pow * z ** 1),
                    4)
                answer = (temp1 + temp2 + temp3) - constant
                my_values[i] = round(abs(answer - 0), 3)
                my_keys[i] = population[i]

    my_values = dict(sorted(my_values.items(), key=lambda item: item[1]))
    # print(my_keys)
    # print(my_values)
    return my_keys, my_values


def check_for_terminating_condition(my_keys, my_values, fitness):
    l1 = []
    mine_dict = {}
    if 0 not in my_values.values():
        for key, val in my_values.items():
            if val < 100.0:
                mine_dict[str(my_keys[key])] = val
            pass
        fitness = fitness | mine_dict
        return 0, fitness
    else:
        if variable_number == 1:
            # print(f"My values list is : {my_values}")
            # print(f"My keys list is : {my_keys}")
            for key, val in my_values.items():
                if val == 0:
                    l1.append(key)
            # print(f"Value is {l1}")
        for i in range(len(l1)):
            pass
            print(f"Value of x where our equation satisfied : {my_keys[l1[i]]}")
        if variable_number == 2 or variable_number == 3:
            for key, val in my_values.items():
                if val == 0:
                    l1.append(key)
            if variable_number == 2:
                for i in range(len(l1)):
                    pass
                    print(f"Values of x and y where our equation satisfied : {my_keys[l1[i]]}")
            elif variable_number == 3:
                for i in range(len(l1)):
                    pass
                    print(f"Values of x y and z where our equation satisfied : {my_keys[l1[i]]}")
    return 1, fitness


def Selection(my_keys, my_values):
    temp1_list = []
    temp2_list = []
    temp1_list.append(my_keys[list(my_values.keys())[0]])
    temp1_list.append(my_keys[list(my_values.keys())[1]])
    temp1_list.append(my_keys[list(my_values.keys())[2]])
    temp1_list.append(my_keys[list(my_values.keys())[3]])
    temp2_list.append(my_keys[list(my_values.keys())[7]])
    temp2_list.append(my_keys[list(my_values.keys())[4]])
    temp2_list.append(my_keys[list(my_values.keys())[5]])
    temp2_list.append(my_keys[list(my_values.keys())[6]])
    # print(f"After selection temp1 is {temp1_list} and temp 2 is {temp2_list}")

    return temp1_list, temp2_list


def cross_over(temp1_list, temp2_list):
    population = []
    if variable_number == 1:
        x1 = random.randint(0, 1)
        x2 = random.randint(0, 1)
        x3 = random.randint(0, 1)
        x4 = random.randint(0, 1)
        # print(f'Value of x1 is {x1}')
        # print(f'Value of x1 is {x2}')
        # print(f'Value of x1 is {x3}')
        # print(f'Value of x1 is {x4}')
        temp1[x1] = temp2[x2]
        temp2[x3] = temp1[x4]
    elif variable_number == 2:
        temp1_list[random.randint(0, 3)][random.randint(0, 1)] = temp2_list[random.randint(0, 3)][random.randint(0, 1)]
        temp2_list[random.randint(0, 3)][random.randint(0, 1)] = temp1_list[random.randint(0, 3)][random.randint(0, 1)]
    elif variable_number == 3:
        temp1_list[random.randint(0, 3)][random.randint(0, 2)] = temp2_list[random.randint(0, 3)][random.randint(0, 2)]
        temp2_list[random.randint(0, 3)][random.randint(0, 2)] = temp1_list[random.randint(0, 3)][random.randint(0, 2)]

    # print(f"After cross over temp1 is {temp1} and temp 2 is {temp2}")
    return temp1_list, temp2_list


def mutation(temp1_list, temp2_list, iteration):
    if random.uniform(0, 1) < MUTATION_RATE:
        # print("It is mutation function.")
        # print(f"Before Mutation population is {temp1_list}, {temp2_list}")
        if equation_type == 1:
            if variable_number == 1:
                if iteration >= 200:
                    temp1_list[random.randint(0, 3)] = int(random.uniform(-20, 20))
                    temp2_list[random.randint(0, 3)] = round((random.uniform(-20, 20)), 2)
                else:
                    temp1_list[random.randint(0, 3)] = int(random.uniform(-20, 20))
                    temp2_list[random.randint(0, 3)] = int(random.uniform(-20, 20))
            elif variable_number == 2:
                if iteration >= 200:
                    temp1_list[random.randint(0, 3)][random.randint(0, 1)] = int(random.uniform(-20, 20))
                    temp2_list[random.randint(0, 3)][random.randint(0, 1)] = round((random.uniform(-20, 20)), 2)
                else:
                    temp1_list[random.randint(0, 3)][random.randint(0, 1)] = int(random.uniform(-20, 20))
                    temp2_list[random.randint(0, 3)][random.randint(0, 1)] = int(random.uniform(-20, 20))
            elif variable_number == 3:
                if iteration >= 200:
                    temp1_list[random.randint(0, 3)][random.randint(0, 2)] = int(random.uniform(-20, 20))
                    temp2_list[random.randint(0, 3)][random.randint(0, 2)] = round((random.uniform(-20, 20)), 2)
                else:
                    temp1_list[random.randint(0, 3)][random.randint(0, 2)] = int(random.uniform(-20, 20))
                    temp2_list[random.randint(0, 3)][random.randint(0, 2)] = int(random.uniform(-20, 20))
        elif equation_type == 2 or equation_type == 3:
            if equation_type == 2:
                neg_val_threshold = -5
                pos_val_threshold = 10
            elif equation_type == 3:
                neg_val_threshold = -4
                pos_val_threshold = 8
            if variable_number == 1:
                if iteration >= 200:
                    temp1_list[random.randint(0, 3)] = int(random.uniform(neg_val_threshold, pos_val_threshold))
                    temp2_list[random.randint(0, 3)] = round(random.uniform(neg_val_threshold, pos_val_threshold), 2)
                else:
                    temp1_list[random.randint(0, 3)] = int(random.uniform(neg_val_threshold, pos_val_threshold))
                    temp2_list[random.randint(0, 3)] = int(random.uniform(neg_val_threshold, pos_val_threshold))
            elif variable_number == 2:
                if iteration >= 200:
                    temp1_list[random.randint(0, 3)][random.randint(0, 1)] = int(
                        random.uniform(neg_val_threshold, pos_val_threshold))
                    temp2_list[random.randint(0, 3)][random.randint(0, 1)] = round(
                        (random.uniform(neg_val_threshold, pos_val_threshold)), 3)
                else:

                    temp1_list[random.randint(0, 3)][random.randint(0, 1)] = int(
                        random.uniform(neg_val_threshold, pos_val_threshold))
                    temp2_list[random.randint(0, 3)][random.randint(0, 1)] = int(
                        random.uniform(neg_val_threshold, pos_val_threshold))
            elif variable_number == 3:
                if iteration >= 200:
                    temp1_list[random.randint(0, 3)][random.randint(0, 2)] = int(
                        random.uniform(neg_val_threshold, pos_val_threshold))
                    temp2_list[random.randint(0, 3)][random.randint(0, 2)] = round(
                        (random.uniform(neg_val_threshold, pos_val_threshold)), 4)
                else:
                    temp1_list[random.randint(0, 3)][random.randint(0, 2)] = int(
                        random.uniform(neg_val_threshold, pos_val_threshold))
                    temp2_list[random.randint(0, 3)][random.randint(0, 2)] = int(
                        random.uniform(neg_val_threshold, pos_val_threshold))

    for i in range(len(temp2_list)):
        temp1_list.append(temp2_list[i])
    # print(f"After mutation population is {temp1_list}")
    return temp1_list


if __name__ == '__main__':

    my_population = generate_population()
    fitness_less_than_0 = {}
    for i in range(1500):
        # print(f"iteration is : {i}")
        flag = False

        my_keys, my_values = fitness_function(my_population)
        check, fitness_less_than_0 = check_for_terminating_condition(my_keys, my_values, fitness_less_than_0)
        if check:
            flag = True
            break
        temp1, temp2 = Selection(my_keys, my_values)
        temp1, temp2 = cross_over(temp1, temp2)
        my_population = mutation(temp1, temp2, i)

    if flag == False:
        print("Couldn't Find your answer.")
        print("But some population that has closest fitnesses to zero are given below : ")
        fitness_less_than_0 = dict(sorted(fitness_less_than_0.items(), key=lambda item: item[1]))
        var = 1
        for key, val in fitness_less_than_0.items():
            if var == 5:
                break
            print(f" {key} : {val}")
            var += 1
