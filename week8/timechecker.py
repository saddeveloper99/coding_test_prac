import time

# 데코레이터 
def elapsed(f):
    def wrap(*args):
        start_r = time.perf_counter()
        start_p = time.process_time()
        # 함수 실행
        ret = f(*args)
        end_r = time.perf_counter()
        end_p = time.process_time()
        elapsed_r = end_r - start_r
        elapsed_p = end_p - start_p

        print(
            f'{f.__name__} elapsed: {elapsed_r:.6f}sec (real) / {elapsed_p:.6f}sec (cpu)')
        return ret
    return wrap


# # 또는 아래 코드를 복붙 후 사용
# start = time.time()

# # 여기에 식 입력


# print("time3 :", time.time() - start)
