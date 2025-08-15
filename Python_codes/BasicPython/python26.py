
thinkers=['Plato','Playdo','Gumby']
while True:
    try:
        thinker=thinkers.pop()
        print(thinker)

    except IndexError as e:
        print("we tried to pop too many thinkers")
        print(e)
        break


