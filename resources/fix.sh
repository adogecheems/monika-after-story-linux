DIR_FIX_LIST=(
    zz_dockingstation
    zz_pianokeys
    zz_spritejsons
)

for target in "${DIR_FIX_LIST[@]}"; do
    file="game/${target}.rpy"
    sed -i \
    -e 's/renpy\.config\.basedir\s*\+\s*"\s*\/game/renpy.config.gamedir + "/g' \
    -e 's/config\.basedir\s*\+\s*"\s*\/game/config.gamedir + "/g' \
    "$file"
done

sed -i  's/os\.path\.normcase\s*(\s*config\.basedir\s*\+\s*"\s*\/game\/"\s*)/config.gamedir/g' "game/chess.rpy"
sed -zi 's/game_folder = os\.path\.normcase(\n[ \t]*renpy\.config\.basedir \+ "\/game\/"\n[ \t]*)/renpy.config.gamedir/g' "game/zz_dockingstation.rpy"

REPLACE_LIST=(
    definitions
    script-affection
    script-ch30
    script-greetings
    script-holidays
    script-introduction
    script-story-events
    zz_backup
    zz_consumables
    zz_dockingstation
    zz_reactions
    chess
    zz_music_selector
    0utils
    zz_pianokeys
)

for target in "${REPLACE_LIST[@]}"; do
    file="game/${target}.rpy"
    sed -i \
    -e "s/renpy\.config\.basedir/store.home()/g" \
    -e "s/config\.basedir/store.home()/g" \
    "$file"
done

REMOVE_LIST=(
    updater
    updates_topics
    updates
)

for target in "${REMOVE_LIST[@]}"; do
    file="game/${target}.rpy"
    rm -f "$file"
done

sed -i '/os\.chmod(config\.gamedir\.format(fp), 0755)/d' "game/chess.rpy"
sed -i '/if not main_menu:/,/style "navigation_button"/d' "game/screen.rpy"
sed -i '/if not mas_checked_update:/,+2d' "game/script-ch30.rpy"
sed -i '/with open(basedir \+ "\/game\/masrun", "w") as versfile:/,+1d' "game/splash.rpy"
sed -i '/build.include_update = True/build.include_update = False/' game/options.rpy
sed -i '/log_enable = True/log_enable = False/' renpy/config.py