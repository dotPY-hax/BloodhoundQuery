import inspect

from interactive_mode import InteractiveQuery
import user_queries
import output


def get_user_query_classes():
    classes = [class_tuple[0] for class_tuple in inspect.getmembers(user_queries, inspect.isclass) if class_tuple[-1].__module__ == user_queries.__name__]
    return classes


def get_functions_of_class(class_):
    functions = [function_[0] for function_ in inspect.getmembers(class_, inspect.isfunction) if not function_[0].startswith("__") and function_[-1].__module__ == user_queries.__name__]
    return functions


def choose_from_list(list_of_items):
    print("choose item:")
    for i, item in enumerate(list_of_items):
        print("{} - {}".format(i, str(item)))
    chosen = None
    while chosen not in range(len(list_of_items)):
        chosen = input("choose: ")
        chosen = chosen.strip()
        try:
            chosen = int(chosen)
        except Exception:
            chosen = None

    return list_of_items[chosen]

def get_command():
    commands = ["get_users", "keys_users", "must", "not", "users", "computers", "print", "pretty", "one", "help"]
    user_input = input(">").split()
    if user_input and user_input[0] in commands:
        return user_input
    else:
        return None


def predefined_query_ui(bloodhound_path):
    class_ = choose_from_list(get_user_query_classes())
    class_ = getattr(user_queries, class_)
    function_ = choose_from_list(get_functions_of_class(class_))
    query = class_()
    query.load(bloodhound_path)
    data = getattr(query, function_)()
    output.print_data(data)



def interactive_mode_ui(bloodhound_path):
    #commands = ["get_users", "keys_users", "must", "not", "users", "computers", "print", "one"]
    helps = {"get_users": "Get user data with keys try: get_users name description enabled",
             "keys_users": "Show all available keys of the user struct try: keys_users",
             "must": "Filter the data by a key with a value try: must enabled True",
             "not": "Filter the data by a key with a value try: not enabled False",
             "users": "Get all user data try: users",
             "computers": "Get all computer data try: computers",
             "print": "Print the data previously gotten try: print",
             "pretty": "Print the data neatly: pretty",
             "one": "Print the first element of the data previously gotten try: one"}
    interactive = InteractiveQuery()
    interactive.load(bloodhound_path)

    print("Welcome to Bloodhound Query - type help for help")
    while True:
        user_input = None
        while not user_input:
            user_input = get_command()
        command = user_input[0]
        args = user_input[1:]
        if command == "help":
            for cmd, text in helps.items():
                print("{} - {}".format(cmd, text))

        if command == "users":
            interactive.get_all_user_data()
            print("All user data loaded")
        if command == "computers":
            print("All computer data loaded")
        if command == "print":
            output.print_data(interactive.current_data)
        if command == "pretty":
            output.print_json(interactive.current_data)
        if command == "one":
            output.print_json(interactive.get_first())
        if command == "get_users":
            interactive.get_user_data(args)
            print("User data with {}".format(args))
        if command == "must":
            key_name = args[0]
            desired_value = args[1]
            interactive.where_has(key_name, desired_value)
            print("Data filtered by {}={}".format(key_name, desired_value))
        if command == "not":
            key_name = args[0]
            undesired_value = args[1]
            interactive.where_not_has(key_name, undesired_value)
            print("Data filtered by {}!={}".format(key_name, undesired_value))
        if command == "keys_users":
            mapping = interactive.map_users()
            output.print_json(mapping)
        print("Accumulator has {} items".format(len(interactive.current_data)))


