def SlashLoadingAnimation(Loops, Intervals=0.125, Prefix="  ", Suffix="", CompletionMessage="\n"):
    """
    Creates a terminal based loading animation using the following characters: "|", "/", "—", "\\"

    args:
        Loops (int): The amount of times the animation will loop

        Intervals (float): The amount of intervals between each frame printed (Recomended is anywhere between 0.1 and 0.2 (Adding a float with a decimal length > 1 will cause imprecise timing when when printing))

        Prefix (str): The string that will be printed before the animation (For no prefix, leave blank (Or add "", or None as the argument))

        Suffix (str): The string that will be printed after the animation (For no suffix, leave blank (Or add "", or None as the argument))

        CompletionMessage (str): The string that will be printed once the animation finishes (For no completion message, leave blank (Or add "", or None as the argument (Recomended to add "\\n")))
    """

    import time

    Frames = ["|", "/", "—", "\\"]

    Loops *= 2

    for Time in range(0, Loops):
        for Frame in range(0, 4):
            PrintString = f"{str(Prefix)}{str(Frames[Frame])}{str(Suffix)}"
            print(PrintString, end="\r")

            time.sleep(Intervals)

    print("\n" + str(CompletionMessage))
