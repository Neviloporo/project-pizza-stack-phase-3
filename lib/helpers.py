def get_input(prompt, cast=str, allowed=None, error_msg="Invalid input. Try again.", case_insensitive=False):
    while True:
        try:
            val = cast(input(prompt))
            check_val = val.lower() if case_insensitive and isinstance(val, str) else val
            if allowed:
                allowed_set = {a.lower() if case_insensitive and isinstance(a, str) else a for a in allowed}
                if check_val not in allowed_set:
                    raise ValueError()
            return val
        except (ValueError, TypeError):
            print(error_msg)
