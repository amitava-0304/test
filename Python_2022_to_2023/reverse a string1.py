def reverse_string(st):
    rev_word=''     
    reverse_str=''
    for l in st:
        if l.isalpha():
            rev_word=l+rev_word  

        else:
            reverse_str+=rev_word
            rev_word=''
            reverse_str+=l

    return reverse_str


def main():
    string='H#ell$o'
    print(reverse_string(string))

if __name__=='__main__':
    main()
