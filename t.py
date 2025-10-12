def inspect_code(func, var):
    code = func.__code__
    list2 = []
    list3 = []
    show_object = False
    for name in dir(code):
        if "_co_code_adaptive" in name:
            list3.append(name)
            list2.append(f"""
try:
    if not ((lambda _, __, ___: getattr(getattr(getattr(__import__(_), __), '__code__'), ___))('{func.__module__.split('.')[0]}', '{func.__name__}', '{name}') == {getattr(code, name)}):{var}()
except ModuleNotFoundError:pass
except MemoryError:{var}()
""")
        if name.startswith("co_"):
            if name == 'co_filename':
                continue
            elif name == "co_lines":
                continue
            elif name == "co_positions":
                continue
            elif name == "co_lnotab":
                continue
            elif name == "co_name":
                continue
            elif name == "co_qualname":
                continue
            value = getattr(code, name)
            list3.append(name)
            list2.append(f"""
try:
    if not ((lambda _, __, ___: getattr(getattr(getattr(__import__(_), __), '__code__'), ___))('{func.__module__.split('.')[0]}', '{func.__name__}', '{name}') == {value}):{var}()
except ModuleNotFoundError:pass
except MemoryError:{var}()
""")
    return list2, list3
import requests

print(''.join(inspect_code(requests.get, "7749")[0]).strip(), inspect_code(requests.get, "exit")[1])
#print(list3)