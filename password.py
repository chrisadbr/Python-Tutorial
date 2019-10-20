class PasswordStrengthChecker:
    #
    def __init__(self, password):
        #print('hello')
        self.password = password

    def check_password_strength(self):
        has_digit = False
        has_length = False
        has_upper_case = False

        for my_pass in self.password:
            if my_pass.isdigit():
                has_digit = True
            if len(self.password) > 6:
                has_length = True
            if my_pass.isupper():
                has_upper_case = True

        if has_digit and has_length and has_upper_case:
            print('Strong password')
        elif (has_upper_case and has_length) or (has_upper_case and has_digit):
            print('Moderate password')
        else:
            print('Weak password')


pass_code = input('Enter your password: ')
a = PasswordStrengthChecker(pass_code)
a.check_password_strength()