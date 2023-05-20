
def replay_case_fail(num=3):
    """
    报错重试的装饰器：当脚本运行报错时会重新运行脚本
    重新运行次数为 num
    """
    def _wrapper(func):
        def wrapper(*args, **kwargs):
            raise_info = None
            r_num = 0
            for i in range(num):
                r_num += 1
                try:
                    ret = func(*args, **kwargs)
                    if r_num > 1:
                        print('重试{}次成功'.format(r_num))
                    return ret
                except Exception as ex:
                    raise_info = ex
            print('重试{}次,全部失败'.format(r_num))
            raise raise_info
        return wrapper
    return _wrapper
