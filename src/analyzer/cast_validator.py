class CastValidator:
    def __init__(self, value):
        self.value = value

    def is_valid(self):
        type_ = self.value.return_type()
        cast_type = self.value.cast_type

        if type_ == "node" and cast_type in ["node", "graph", "num", "logic"]: return True
        if type_ == "arc" and cast_type in ["arc", "graph", "num", "logic"]: return True
        if type_ == "graph" and cast_type in ["graph", "logic"]: return True
        if type_ == "num" and cast_type in ["node", "graph", "num", "logic"]: return True
        if type_ == "nope" and cast_type != "logic": return True
        if type_ == "logic" and cast_type in ["num", "logic"]: return True

        return False
