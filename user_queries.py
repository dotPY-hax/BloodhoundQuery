from query import BloodHoundQuery


class IppsecVideoQueries(BloodHoundQuery):
    def enabled_users(self):
        data = self.get_user_data(["name", "enabled"])
        data = self.where_has(data, "enabled", True)
        return data

    def disabled_users(self):
        data = self.get_user_data(["name", "enabled"])
        data = self.where_not_has(data, "enabled", True)
        return data

    def usernames_descriptions(self):
        data = self.get_user_data(["name", "description"])
        return data

    def usernames_only_valid_descriptions(self):
        data = self.get_user_data(["name", "description"])
        data = self.where_not_has(data, "description", None)
        return data

    def last_logon(self):
        data = self.get_user_data(["name", "lastlogontimestamp"])
        return data

    def never_logged_on(self):
        data = self.get_user_data(["name", "lastlogontimestamp"])
        data = self.where_has(data, "lastlogontimestamp", -1)
        return data

    def kerberoastable_users(self):
        data = self.get_user_data(["name", "serviceprincipalnames"])
        data = self.where_not_has(data, "serviceprincipalnames", [])
        data = self.trim_to(data, ["name"])
        return data

    def computers_with_os(self):
        data = self.get_computer_data(["name", "operatingsystem"])
        return data
0