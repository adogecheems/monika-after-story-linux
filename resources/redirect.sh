TARGET_LIST=(
    definitions
    script-affection
    script-ch30
    script-greetings
    script-holidays
    script-introduction
    script-story-events
    updates
    zz_backup
    zz_consumables
    zz_dockingstation
    zz_reactions
    chess
    zz_music_selector
    0utils
    zz_pianokeys
)

for target in "${TARGET_LIST[@]}"; do
    file="game/${target}.rpy"
    sed -i \
    -e "s/renpy\.config\.basedir/store.home()/g" \
    -e "s/config\.basedir/store.home()/g" \
    "$file"
done

sed -i 's/log_enable = True/log_enable = False/' renpy/config.py