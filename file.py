def greeter(func_to_be_decorated):
    def decoration(*args, **kwargs):
        result = func_to_be_decorated(*args, **kwargs)
        return "Aloha " + result.title()
    return decoration
        

def sums_of_str_elements_are_equal(func_to_be_decorated):
    def decoration(*args, **kwargs):
        result = func_to_be_decorated(*args, **kwargs).split(" ")
        
        def add_digits(string_of_digits):
            each_digit = list(string_of_digits)
            
            if each_digit[0] == "-":
                flag = -1
                iter_start = 1
            else:
                flag = 1
                iter_start = 0
            
            sum_of_digits = 0
            for i in range(iter_start, each_digit.__len__()):
                # print(i)
                sum_of_digits = sum_of_digits + int(each_digit[i]) * flag
                
            return sum_of_digits
        
        sum1 = add_digits(result[0])
        sum2 = add_digits(result[1])
        
        if sum1 == sum2:
            internal_result = f"{str(sum1)} == {str(sum2)}"
        else:
            internal_result = f"{str(sum1)} != {str(sum2)}"
        
        return internal_result
    return decoration


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
