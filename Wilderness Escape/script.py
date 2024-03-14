######
# TREENODE CLASS
######
class TreeNode:
    def __init__(self, story_piece):
        self.story_peice = story_piece
        self.choices = []
    def add_child(self, node):
        self.choices += node
    def traverse(self):
        story_node = self
        while story_node.choices:
            print(story_node.story_peice)
            choice = input("Enter 1 or 2 to continue the story: ")
            if choice != '1' and choice != '2':
                print("Invalid", choice)
                continue
            chosen_index = int(choice) - 1
            chosen_child = story_node.choices(chosen_index)
            print(chosen_child.story_piece)
            story_node = chosen_child
######
# VARIABLES FOR TREE
######
story_root = TreeNode("""You are in a forest clearing. \nThere is a path to the left. \nA bear emerges from the trees and roars! Do you: \n1 ) Roar back! \n2 ) Run to the left...""")
user_choice = input("What is your name? ")
choice_a = """The bear is startled and runs away. Do you:\n1 ) Shout 'Sorry bear!' \n2 ) Yell 'Hooray!'"""
choice_b = """\nYou come across a clearing full of flowers. The bear follows you and asks 'what gives?' Do you:\n1 ) Gasp 'A talking bear!'\n2 ) Explain that the bear scared you."""



###### 
# TESTING AREA
#####
print(user_choice)
print("Once upon a time...")
#print(story_root.story_peice)
story_root.add_child(choice_a)
story_root.add_child(choice_b)
story_root.traverse()
