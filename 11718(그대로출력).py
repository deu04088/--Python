while True:
    try:
        print(input())
    except EOFError:    # End Of File, 입력이 끝날 때 종료
        break