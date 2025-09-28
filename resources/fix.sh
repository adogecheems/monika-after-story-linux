RPY_FILES=(game/*.rpy)

# Fix gamedir usage

sed -i  's/os.path.normcase(config.basedir + "\/game\/")/config.gamedir/g' game/chess.rpy
perl -0777 -i -pe 's/game_folder = os\.path\.normcase\(\s*renpy\.config\.basedir \+ "\/game\/"\s*\)/game_folder = renpy.config.gamedir/g' game/zz_dockingstation.rpy

for file in "${RPY_FILES[@]}"; do
    sed -i \
    -e 's/renpy.config.basedir + "\/game/renpy.config.gamedir + "/g' \
    -e 's/config.basedir + "\/game/config.gamedir + "/g' \
    $file
done

# Redirect save files to home directory

for file in "${RPY_FILES[@]}"; do
    sed -i \
    -e "s/renpy.config.basedir/store.home/g" \
    -e "s/config.basedir/store.home/g" \
    $file
done

# Other fixes

sed -i '/os.chmod(config.gamedir.format(fp), 0755)/d' game/chess.rpy
perl -0777 -i -pe 's/^[ \t]*if not main_menu:\r?\n[ \t]*textbutton _\("?Update Version"?\):\r?\n[ \t]*action Function\(renpy\.call_in_new_context, .forced_update_now..*\)\r?\n[ \t]*style "navigation_button"\r?\n?//mg' game/screens.rpy
perl -0777 -i -pe 's/^[ \t]*with open\(basedir \+ "\/game\/masrun", "w"\) as versfile:\r?\n[ \t]*versfile\.write\(config\.name \+ "\|" \+ config\.version \+ "\\n"\)\r?\n?//mg' game/splash.rpy
sed -i 's/build.include_update = True/build.include_update = False/' game/options.rpy
sed -i 's/log_enable = True/log_enable = False/' renpy/config.py
