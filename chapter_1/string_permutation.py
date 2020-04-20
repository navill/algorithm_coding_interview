def perm(s1, s2):
    sorted_string1 = sorted(s1)
    sorted_string2 = sorted(s2)
    return sorted_string2 == sorted_string1


print(perm('bbabdc', 'abbbdc'))
