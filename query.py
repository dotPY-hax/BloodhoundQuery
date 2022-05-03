from data import Data


class BloodHoundQuery:
    def __init__(self):
        self.raw = None

    def load(self, filename="./BloodHound.zip"):
        self.raw = Data(filename)

    def get_user_data(self, key_list):
        return self.raw.get_n_generic_attributes_key_keys(key_list, "users")

    def get_computer_data(self, key_list):
        return self.raw.get_n_generic_attributes_key_keys(key_list, "computers")

    def where_has(self, data, key_name, desired_value):
        items = []
        for item in data:
            value = item.get(key_name, None)
            if value == desired_value or str(value) == desired_value:
                items.append(item)
        return items

    def where_not_has(self, data, key_name, desired_value):
        items = []
        for item in data:
            value = item.get(key_name, None)
            if value != desired_value and str(value) != desired_value:
                items.append(item)
        return items

    def trim_to(self, data, key_list):
        new_items = []
        for item in data:
            new_item = {}
            for key in key_list:
                new_item[key] = item[key]
            new_items.append(new_item)
        return new_items
