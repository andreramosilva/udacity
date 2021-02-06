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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


parent1 = Group("parent1")
child1 = Group("child1")
sub_child1 = Group("subchild1")

sub_child_user1 = "sub_child_user1"
sub_child1.add_user(sub_child_user1)

child1.add_group(sub_child1)
parent1.add_group(child1)



parent2 = Group("parent2")
child2 = Group("child2")
sub_child2 = Group("subchild2")

sub_child_user2 = "sub_child_user2"
sub_child2.add_user(sub_child_user2)

child2.add_group(sub_child)
parent2.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """


    if user in group.users:
        return True
    for group in group.groups:
        if is_user_in_group(user, group):
            return True

    return False


print(is_user_in_group(sub_child_user, sub_child))

print(is_user_in_group(sub_child_user1, sub_child1))

print(is_user_in_group(sub_child_user2, sub_child2))