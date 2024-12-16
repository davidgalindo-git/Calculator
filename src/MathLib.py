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
                res = math_request.set_res(ope1 - ope2)
                return res
            case 'mul':
                res = math_request.set_res(ope1 * ope2)
                return res
            case 'div':
                res = math_request.set_res(ope1 / ope2)
                return res
            case 'pow':
                res = math_request.set_res(ope1 ** ope2)
                return res
            case 'root':
                res = math_request.set_res(MathLib.__root(ope1, ope2))
            case _:
                raise OperatorNotSupportedException

    @staticmethod
    def __root(ope1, ope2):
        raise NotImplementedError

class MathLibException(Exception):
    pass

class OperatorNotSupportedException(MathLibException):
    pass