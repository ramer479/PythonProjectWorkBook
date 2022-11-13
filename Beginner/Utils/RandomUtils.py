import random





class RandomUtils:
    default_int = 1

    def get_random_integer(self,strt_num = 0,end_num = default_int):
        num_list = [i for i in range(strt_num,end_num)]
        return random.choice(num_list)