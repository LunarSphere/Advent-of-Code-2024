def load_data():
    rules = []
    updates = []
    read_rules = True ## a bool to determine if we are reading rules or updates
    # alternatively could have implemented this by finding a way to figure out which line
    # I was last pointing to. 
    with open("input/day5.txt") as file:
        for line in file.readlines(): 
            line = line.strip() #strip the line
            if line.strip() == "": read_rules = False; continue #if line is empty stop reading rules and skip next if statement
            if read_rules: 
                vals = line.split("|")
                rules.append((int(vals[0]), int(vals[1])))
            if not read_rules:
                updates.append([int(s) for s in line.split(",")])
    return rules, updates

def valid_update(rules, update) -> bool:
    for i, num in enumerate(update):
        #sublist of relevant rules
        sub_rules = [rule for rule in rules if num == rule[0] and rule[1] in update] #grab sublist of tuples where tup[0] == current number in update list
        # also ensures corresponding rule is in 
        for i in sub_rules:
            if update.index(num) > update.index(i[1]): return False # if index of current num is larger than its rule pair it means the number is ahead of it which breaks the rule


    return True

def part1() -> int:
    # given list of rules about ordering of pages of updates determine correct order. 
    # add up middle value of correctly ordered updates
    valid_middle_val_sum = 0
    rules, updates = load_data()
    for update in updates:
        if valid_update(rules, update): 
            valid_middle_val_sum += update[len(update)//2]

    return valid_middle_val_sum

def main():
    print(part1())

    return 0; 
if __name__ == "__main__":
    main()
    print("Day 5: Completed")