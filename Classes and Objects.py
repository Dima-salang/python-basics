class person:
    def __init__(self, name, age):  # everytime a Dog obj is created, it sets the initial state of the obj by
        # assigning the values of the obj's properties. It initializes each new instance of the class.
        # When a new class instance is created, the instance is automatically passed to the self param in init so that
        # new attributes can be defined on the obj. Self represents the instance of the class the actual object's name
        # and binds the attributes with the given arguments. 
        # The obj's name is passed as an argument, this argument will be passed to the init method to initialize the obj
        #
        self.name = name  # creates an attribute called name and assigns to it the value of the name param. # the self
        # is the actual object's name. Basically saying the object's name is the value assigned to the name param.
        self.age = age  # creates an attribute called age and assigns to it the value of the age param. Basically
        # saying the obj's name is the value assigned to the name param.
