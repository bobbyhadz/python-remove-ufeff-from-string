# Remove \ufeff from a string in Python

my_str = '\ufefffirst line'

result = my_str.replace('\ufeff', '')
print(repr(result))  # 👉️ 'first line'