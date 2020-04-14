import cx_Freeze

executables = [cx_Freeze.Executable("Menu.py", icon="jones.ico")]

cx_Freeze.setup(
    name="Wookie Lego",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["player1.png", "apple.png","player2.png","swamp.jpg","mount.png","bkg.png","desert.png","ice.png","field.png","pine.png","a.png","lego_tennis1.png","lego_tennis2.png","lego2.png","office.png","tennis.png","ball.png","winner.png"]}},
    executables = executables

    )
