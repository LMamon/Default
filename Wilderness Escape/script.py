######
# TREENODE CLASS
######
class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []
    def add_child(self, node):
        self.choices.append(node)
    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        while len(story_node.choices)>0:
            choice = input("Enter 1 or 2 to continue the story: ")
            if choice not in ["1", "2"]:
                print("Invalid", choice)
            else:
                chosen_index = int(choice)
                chosen_index -= 1
                chosen_child = story_node.choices[chosen_index]
                print(chosen_child.story_piece)
                story_node = chosen_child
        

######
# VARIABLES FOR TREE
######
story_root = TreeNode("""You are in a forest clearing. \nThere is a path to the left. \nA bear emerges from the trees and roars! Do you: \n1 ) Roar back! \n2 ) Run to the left...""")
user_choice = input("What is your name? ")
choice_a = """The bear is startled and runs away. Do you:\n1 ) Shout 'Sorry bear!' \n2 ) Yell 'Hooray!'"""
choice_b = """You come across a clearing full of flowers. The bear follows you and asks 'what gives?' Do you:\n1 ) Gasp 'A talking bear!'\n2 ) Explain that the bear scared you."""
choice_a_1 = TreeNode("""The bear returns and tells you it's been a rough week. After making peace with \na talking bear, he shows you the way out of the forest. \nYOU HAVE ESCAPED THE WILDERNESS.""")
choice_a_2 = TreeNode("""The bear returns and tells you that bullying is not okay before leaving you alone \nin the wilderness. \nYOU REMAIN LOST.""")
choice_b_1 = TreeNode("""The bear is unamused. After smelling the flowers, it turns around and leaves you alone. \nYOU REMAIN LOST.""")
choice_b_2 = TreeNode("""The bear understands and apologizes for startling you. Your new friend shows you a \npath leading out of the forest. \nYOU HAVE ESCAPED THE WILDERNESS.""")




###### 
# TESTING AREA
#####
print(user_choice)
print("Once upon a time...")
story_root.add_child(choice_a)
story_root.add_child(choice_b)
story_root.traverse()
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)
