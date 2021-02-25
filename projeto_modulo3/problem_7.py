# A RouteTrie will store our routes and their associated handlers
import collections
class PageNotFound(Exception):
    pass

class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)


    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for segment in path:
            current_node = current_node.children[segment]
        current_node.handler = handler


    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        def recursive(node, segments):
            if not segments:
                return node

            head, *tail = segments

            if head not in node.children:
                return recursive
            return recursive(node.children[head], tail)

        node = recursive(self.root, path)
        return node.handler if node is not None else node

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = collections.defaultdict(RouteTrieNode)
        self.handler = handler


class Router:
        def __init__(self):
            # Create a new RouteTrie for holding our routes
            # You could also add a handler for 404 page not found responses as well!
            self.trie = RouteTrie()

        def add_handler(self, path,handler):

            # Add a handler for a path
            # You will need to split the path and pass the pass parts
            # as a list to the RouteTrie
            self.trie.insert(self._split_path(path), handler)

        def lookup(self, path):

            # lookup path (by parts) and return the associated handler
            # you can return None if it's not found or
            # return the "not found" handler if you added one
            # bonus points if a path works with and without a trailing slash
            # e.g. /about and /about/ both return the /about handler
            handler = self.trie.find(self._split_path(path))
            if handler is None:
                #raise PageNotFound
                print("page not found")
            return handler

        def _split_path(self, path):
            # you need to split the path into parts for
            # both the add_handler and loopup functions,
            # so it should be placed in a function here
            path = path.strip('/')
            return path.split('/') if path else []

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route


router = Router()  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one