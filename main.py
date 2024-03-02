def read_file(file_name: str):
    """
    Function opens file and reads its content.
    :param file_name:
    :return:
    """
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        return "Such file doesn't exist."
    else:
        content = file.read()
        file.close()
        return content
