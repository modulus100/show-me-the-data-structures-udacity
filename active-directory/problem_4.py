class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


class GroupService:
    def is_user_in_group(self, user: str, group: Group) -> bool:
        """
        Return True if user is in the group, False otherwise.

        Args:
          user(str): user name/id
          group(class:Group): group to check user membership against
        """
        if not user or not group:
            return False

        if user in group.users:
            return True

        for sub_group in group.groups:
            if self.is_user_in_group(user, sub_group):
                return True
        return False


def test_user_in_group():
    print("Test user in group")
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    group_service = GroupService()

    user_in_group = group_service.is_user_in_group(sub_child_user, parent)
    print("User found: " + str(user_in_group))


def test_user_not_in_group():
    print("\nTest user not in group")
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    group_service = GroupService()

    user_in_group = group_service.is_user_in_group("test_user", parent)
    print("User found: " + str(user_in_group))


def test_not_valid_group():
    print("\nTest not valid group")
    group_service = GroupService()
    user_in_group = group_service.is_user_in_group("test_user", None)
    print("User found: " + str(user_in_group))


test_user_in_group()
test_user_not_in_group()
test_not_valid_group()
