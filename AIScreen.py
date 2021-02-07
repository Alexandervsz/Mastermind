from CodeGenerator import CodeGenerator


class AIScreen:
    def start_game(self):
        code = CodeGenerator().get_user_code(True)
