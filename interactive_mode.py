from query import BloodHoundQuery


class InteractiveQuery(BloodHoundQuery):
    def __init__(self):
        self.current_data = []
        super(InteractiveQuery, self).__init__()

    def get_user_keys(self):
        return self.raw.map("users")

    def get_computer_keys(self):
        return self.raw.map("computers")

    def get_all_user_data(self):
        self.current_data = self.raw.users

    def get_all_computer_data(self):
        self.current_data = self.raw.computers

    def get_first(self):
        try:
            return self.current_data[0]
        except IndexError:
            return []

    def get_user_data(self, key_list):
        self.current_data = super(InteractiveQuery, self).get_user_data(key_list)

    def get_computer_data(self, key_list):
        self.current_data = super(InteractiveQuery, self).get_computer_data(key_list)

    def where_has(self, key_name, desired_value):
        self.current_data = super(InteractiveQuery, self).where_has(self.current_data, key_name, desired_value)

    def where_not_has(self, key_name, desired_value):
        self.current_data = super(InteractiveQuery, self).where_not_has(self.current_data, key_name, desired_value)

    def map_users(self):
        return self.raw.map("users")
