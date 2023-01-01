title_name = input("Enter title name: ").capitalize()

fighter_name_box = []
for num in range(2):
    fighter_name = input("Enter fighter's name: ").capitalize()
    fighter_name_box.append(fighter_name)
    for name in fighter_name_box:
        print(name)


def fighter_name(fighter_name_box):

    return "This is a boxing bout between " + fighter_name_box[0] + " and " + fighter_name_box[1]


print(fighter_name(fighter_name_box))


def boxing_judge(judges):
    print("There are " + str(judges) + " Judges" + " for this boxing bout. ")

    if judges == 2:
        score_box = []
        for num in range(len(fighter_name_box)):
            judges_totalscore = []
            for num in range(3):
                judge_points = int(input("Enter a point: "))
                judges_totalscore.append(judge_points)
            score = sum(judges_totalscore)
            score_box.append(score)
            for point in score_box:
                print(point)
        if score_box[0] > score_box[1]:
            return fighter_name_box[0] + " won the boxing bout! " + "with " + str(score_box[0]) + " points"
        elif score_box[0] < score_box[1]:
            return fighter_name_box[1] + " won the boxing bout! " + "with " + str(score_box[1]) + " points"
        else:
            return "The boxing bout between " + fighter_name_box[0] + " and " + fighter_name_box[1] + "ended in draw!"
    else:
        return "The number of Judges input has to be 2! "


print(boxing_judge(int(input("Enter number of judges: "))))