class RuntimeError:
    @classmethod
    def cast_error(cls, type_, cast_type):
        cls._halt(f"Cannot cast {type_} to {cast_type}")

    @classmethod
    def _halt(cls, message):
        print("Runtime error:", message)
        exit(1)
