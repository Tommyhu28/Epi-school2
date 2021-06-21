from prime import is_prime
begin = 10001
end = 99999
cur=begin
ans = []
while (cur <= end):
    dummy = str(cur)
    first= dummy[0]+dummy[1]
    second = dummy[-1]+dummy[-2]
    if (first==second and is_prime(cur)):
        ans.append(cur)
    cur+=1

print(ans)