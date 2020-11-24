from itertools import permutations


def calculate_ages_of_friends():
    """ Print ages of two friends
     CRITERIA: output of operations on first age gives the second age and output
     of operations in a different order on second age gives the first age.
     The four operations to be used:
     f1: +2
     f2: /8
     f3: -3
     f4: *7 """
    # list containing results for every operation permutation for valid age inputs (0 to 120)
    all_res = calculate_results_for_all_permutations()
    # get the indices for where the result is a potential input
    valid_indices = list(i for i, e in enumerate(all_res) if (e % 1 == 0 and 0 < e < 120))
    # generate set of ages that match the criteria above
    matches = find_matches(valid_indices, all_res)
    print(f"Ages of the two friends are: {matches}")


def calculate_results_for_all_permutations():
    # calculate results from each permutation with valid age inputs (0 to 120)
    f1 = "+ 2.0"
    f2 = "/ 8.0"
    f3 = "- 3.0"
    f4 = "* 7.0"
    perms = list(permutations([f1, f2, f3, f4]))
    results = []
    for perm in perms:
        p1, p2, p3, p4 = perm
        for x in range(120):
            result = eval("((((" + str(x) + p1 + ")" + p2 + ")" + p3 + ")" + p4 + ")")
            results.append(result)
            print(results)
    return results


def find_matches(valid_indices, all_res):
    """ Find the ages where the output age generates the input age when using a
     different order of operations """
    matches = set()
    for ind in valid_indices:
        output_age = all_res[ind]
        original_input_age = ind % 120
        input_age_indices = determine_indices_to_search(ind, output_age)
        # take each input age index and check whether the indices are in valid_indices,
        # if they are see if the result is equal to the original input age
        for input_age_index in input_age_indices:
            if input_age_index in valid_indices:
                if all_res[int(input_age_index)] == original_input_age:
                    matches.add(original_input_age)
                    matches.add(int(output_age))
    return matches


def determine_indices_to_search(ind, output_age):
    """ List the indices to try for the second age as an input - excluding using the
     index that would use the same operation order as the original input age """
    # current_bin gives value of 0 to 23 indicating which permutation created the value
    current_bin = ind // 120
    bins = list(range(24))
    bins.remove(current_bin)
    # limit the age input to indices using other permutations
    input_age_indices = [(120 * x) + output_age for x in bins]
    return input_age_indices


calculate_ages_of_friends()
