r_point, v_point = 0, 0
r_gpa, v_gpa = 0.0, 0.0

while True:
    print('학점을 추가로 입력하려면 1, 계산하고 프로그램을 종료하려면 2를 입력하세요.')
    user_value = input()
    command = int(user_value)

    #입력
    if command == 1:
        print('학점을 입력하세요:')
        user_value = input()
        point = int(user_value)

        print('평점을 입력하세요:')
        while True:
            user_value = input()
            value = str(user_value)
            match value:
                case 'A+':
                    gpa = 4.5
                    break
                case 'A':
                    gpa = 4.0
                    break
                case 'B+':
                    gpa = 3.5
                    break
                case 'B':
                    gpa = 3.0
                    break
                case 'C+':
                    gpa = 2.5
                    break
                case 'C':
                    gpa = 2.0
                    break
                case 'D+':
                    gpa = 1.5
                    break
                case 'D':
                    gpa = 1.0
                    break
                case 'F':
                    gpa = 0.0
                    break
                case _:
                    print('올바른 형태로 입력하세요(A+/A/B+/B/C+/C/D+/D/F)')

        r_point += point
        r_gpa += point * gpa
        if gpa > 0:
            v_point += point
            v_gpa += point * gpa

        print('입력 되었습니다.')

    elif command == 2:
        r_gpa /= r_point
        v_gpa /= v_point
        print('제출용: ' + str(v_point) + '학점 (GPA:' + str(v_gpa) + ')')
        print('열람용: ' + str(r_point) + '학점 (GPA:' + str(r_gpa) + ')')
        print('프로그램을 종료합니다.')
        break
    else:
        print('유효하지 않는 값입니다. 다시 입력해 주세요.')
