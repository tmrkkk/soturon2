
import neologdn


def Preprocessing(name, VorW):

    result = []

    with open(VorW + "/" + name + ".csv") as f:
        for line in f:
            count = 0
            for num in range(3):
                line = line[line.find(",")+1:]
            while "," in line:
                line = line.replace(",", "")
                line = neologdn.normalize(line)
                count += 1
                if count > 30:
                    break

            result.append(line)

    with open( VorW + "/P" + name + ".csv", 'w') as f:
        f.writelines(result)
