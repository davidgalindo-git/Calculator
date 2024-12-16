class MathLib:

    @classmethod
    def execute(cls, math_request):
        ope1 = math_request.get_ope1()
        operator = math_request.get_operator()
        ope2 = math_request.get_ope2()

        match operator:
            case 'add':
                res = math_request.set_res(ope1 + ope2)
                return res
            case 'sub':
                raise NotImplementedError
            case 'mul':
                raise NotImplementedError
            case 'div':
                raise NotImplementedError
            case 'pow':
                raise NotImplementedError
            case 'root':
                raise NotImplementedError
            case _:
                raise NotImplementedError

    @staticmethod
    def __root(ope1, ope2):
        raise NotImplementedError

class MathLibException(Exception):
    pass

class OperatorNotSupportedException(MathLibException):
    pass