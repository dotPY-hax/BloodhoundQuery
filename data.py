import read_file


class Data:
    def __init__(self, filename="BloodHound.zip"):
        self.filename = filename
        self.users = None
        self.computers = None
        self.data = None
        self.get_data()

    def get_data(self):
        self.data = read_file.open_zip(self.filename)
        self.users = self.data[read_file.user_file]["data"]
        self.computers = self.data[read_file.computer_file]["data"]

    def search_for_generic_key(self, key_name, property_name):
        _property = getattr(self, property_name)
        current_dictionary = _property[0]
        path = []

        def search_dictionary(dictionary, depth):
            if key_name in dictionary.keys():
                path.append(key_name)
                print("found it")
                return
            else:
                depth += 1
                for key, value in dictionary.items():
                    if isinstance(value, dict):
                        if depth == len(path):
                            path.pop()
                        path.append(key)
                        search_dictionary(value, depth)
                    elif isinstance(value, list) and len(value) > 0:
                        if depth == len(path):
                            path.pop()
                        path.append(key)
                        search_dictionary(value[0], depth)

        search_dictionary(current_dictionary, 0)
        if key_name in path:
            return path
        else:
            return None

    def get_generic_attribute_by_key(self, key_name, property_name):
        path = self.search_for_generic_key(key_name, property_name)
        if path:
            _property = getattr(self, property_name)
            items = []
            for item in _property:
                current_level = item
                for node in path:
                    if isinstance(current_level, list):
                        flattened_list_of_values = []
                        for nested_dict in current_level:
                            flattened_list_of_values.append(nested_dict[key_name])
                        current_level = flattened_list_of_values
                        break

                    else:
                        current_level = current_level.get(node)
                items.append(current_level)
            return items

    def get_n_generic_attributes_key_keys(self, key_name_list, property_name):
        items = {}
        for key_name in key_name_list:
            new_items = self.get_generic_attribute_by_key(key_name, property_name)
            items[key_name] = new_items

        compiled_items = []
        for key_name, item_list in items.items():
            for i, item in enumerate(item_list):
                try:
                    compiled_items[i][key_name] = item
                except IndexError:
                    compiled_items.append({})
                    compiled_items[i][key_name] = item

        return compiled_items

    def map(self, property_name):
        property_ = getattr(self, property_name)
        mapped = {}

        def map_level(level, key_in_data=""):
            level_mapping = {}
            if isinstance(level, dict):
                for key, value in level.items():
                    if not isinstance(value, list) and not isinstance(value, dict):
                        level_mapping[key] = type(value).__name__
                    elif isinstance(value, list):
                        if len(value) > 0:
                            map_level(value[0], key)
                        else:
                            level_mapping[key] = type(value).__name__
                    elif isinstance(value, dict):
                        map_level(value, key)

            elif isinstance(level, list):
                if len(level) > 0:
                    map_level(level[0], key_in_data)
                else:
                    pass

            mapped[key_in_data] = level_mapping

        map_level(property_[0])

        mapped.update(mapped[""])
        del mapped[""]

        return mapped
