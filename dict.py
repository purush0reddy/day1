tell = input('>')
def hello():
    say = tell.split(' ')
    emoj = {
        ":)":"😀",
        ":(":"😗" ,
        ":-":"🤔"  
    }
    output =""
    for word in say:
        output += emoj.get(word,word)
    print(output)
hello()