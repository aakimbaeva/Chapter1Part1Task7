#def biggest_guy(one, two, three):
#    if one > two:
#        a = one
#    else:
#        a = two

#    if a > three:
#        return a
#    else:
#        return three

def biggest_guy(one, two, three):
    return max(one, two, three)

print(biggest_guy(1,5,9))
def test_biggest_guy():
    try:
        assert biggest_guy(1, 3, 2) == 3
        assert biggest_guy(30, 10, 20) == 30
        assert biggest_guy(20, 10, 30) == 30
        assert biggest_guy(2, 1, 9) == 9
        assert biggest_guy('a', 'a', 'b') == 'b' # 'b' is greater than 'a'
    except (AssertionError) as e:
        print(e)
        print("WRONG!!")
        return
    print("SUCCESS!!!")

test_biggest_guy()