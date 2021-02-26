## Assignment Objective
The asignment objective is to understand decorators in Python
The poject contains below decorators:

    1. Run function at odd seconds: a decorator that allows a function to run only if it called at an odd second
    decorator: @run_at_odd_seconds_only
        example:
                @run_at_odd_seconds_only
                def add(a, b):
                    return a+b

    2. Log: a decorator the adds below information to the logger object about the function:
        a. When we are entering the function
        b. The value returned by the function
        c. When we are exiting the function
    decorator: @create_log
        example:
            import logging
            @create_log
            def func(*args):
                return 'Function called'
            
    3. authenticate : this decorator allows the function to be run if the user is authenticated 
    decorator: @authenticate(<username>, <password>)
    example:
            @authenticate('user', 'pwd')
                def my_auth_fun():
                    return "You have been authenticated to run me!!!!!"


    4. timed (n times) : Thie decorator adds an attribute 'avg_run_time' to the function that gives the average run time of the function
    decorator: @timed(<number of repetetions over which average run time is calculated>)
    example:
        @timed(10)
        def my_repeating_fun():
            return "Repeated"
        
        my_repeating_fun()
        print(my_repeating_fun.avg_run_time)


    5. privilege access: Provides privilege access (has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params)
    decorator:@has_privilege(<acces level>)
    example:
        @has_privilege('no')
        def no_privi_func(*args):
            return (args)

