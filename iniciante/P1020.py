Id = int(input())
print(f'{Id//365} ano(s)')
print(f'{Id%365//30} mes(es)')
print(f'{Id%365%30} dia(s)')