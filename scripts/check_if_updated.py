import sys
import yaml


def findDiff(d1, d2, path=""):
    for k in d1:
        if (k not in d2):
            print (path, ":")
            print (k + " as key not in d2", "\n")
            raise Exception(f'Files \"{merged_file}\" and \"{temp_file}\" do not match.'
                            f' Run \"make update\" and run again.')
        else:
            if type(d1[k]) is dict:
                findDiff(d1[k],d2[k], path + "->" + k)
            if type(d1[k]) is list:
                for i, item in enumerate(d1[k]):
                    if type(item) in (int, float, bool, str):
                        if d1[k][i] != d2[k][i]:
                            print("Path:", path, ":")
                            print(" - ", k,f" {i}: ", d1[k][i])
                            print(" + ", k,f" {i}: ", d2[k][i])
                            raise Exception(f'Files \"{merged_file}\" and \"{temp_file}\" do not match.'
                                            f' Run \"make update\" and run again.')
                    else:
                        findDiff(d1[k][i], d2[k][i], path + "->" + k + '->' + str(i))
            else:
                if d1[k] != d2[k]:
                    print("Path:", path, ":")
                    print(" - ", k," : ", d1[k])
                    print(" + ", k," : ", d2[k])
                    raise Exception(f'Files \"{merged_file}\" and \"{temp_file}\" do not match.'
                                    f' Run \"make update\" and run again.')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise RuntimeError(f'Please provide file paths to compare check_if_updated.py')
    merged_file = sys.argv[1]
    temp_file = sys.argv[2]
    with open(merged_file) as f:
        merged_data = yaml.load(f, Loader=yaml.SafeLoader)
    with open(temp_file) as f:
        temp_data = yaml.load(f, Loader=yaml.SafeLoader)
    findDiff(merged_data, temp_data)
    findDiff(temp_data, merged_data)
    print(f"    Current merged file \"{merged_file}\" matches current state of validation_files directory")
