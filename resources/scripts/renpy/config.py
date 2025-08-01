# Copyright 2004-2017 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# This is the config module, where game configuration settings are stored.
# This includes both simple settings (like the screen dimensions) and
# methods that perform standard tasks, like the say and menu methods.

# This will be deleted by the end of this file.
import renpy.display

import collections
import os

# Can we add more config variables?
locked = False

# Contains help for config variables.
help = [ ]  # @ReservedAssignment

# The title of the game window.
window_title = None

# An image file containing the window icon image.
window_icon = None

# The same, but only used on MS windows.
windows_icon = None

# The width and height of the drawable area of the screen.
screen_width = 800
screen_height = 600

# Should sound be enabled?
sound = True

# Turns recoverable errors into fatal ones, so that the user can know
# about and fix them.
debug = False

# Ditto, but for sound operations
debug_sound = None

# Is rollback enabled? (This only controls if the user-invoked
# rollback command does anything)
rollback_enabled = True

# If the rollback is longer than this, we may trim it.
rollback_length = 128

# If set to True, clicking while in rollback will keep the roll forward
# buffer if the data has not changed.
keep_rollback_data = False

# If set to true, menus in fixed rollback will not have clickable
# options and a click anywhere or mouse wheel will roll forward.
fix_rollback_without_choice = False

# The maximum number of steps the user can rollback the game,
# interactively.
hard_rollback_limit = 100

# A list of functions returning lists of displayables that will be
# added to the end of the display list.
overlay_functions = [ ]

# A list of Displayables that should always be added to the start
# of the scene list. (Mostly used for keymaps and the like.)
underlay = [ ]

# True to enable profiling.
profile = False

# The directory save files will be saved to.
savedir = None

# The number of screens worth of images that are allowed to
# live in the image cache at once.
image_cache_size = 16

# The number of statements we will analyze when doing predictive
# loading. Please note that this is a total number of statements in a
# BFS along all paths, rather than the depth along any particular
# path. The current node is counted in this number.
predict_statements = 32

# Causes the contents of the image cache to be printed to stdout when
# it changes.
debug_image_cache = ("RENPY_DEBUG_IMAGE_CACHE" in os.environ)

# Should we allow skipping at all?
allow_skipping = True

# Should we allow fast skipping?
fast_skipping = False

# Are we currently skipping? If so, how fast?
# May be "slow", "fast", or None.
skipping = None

# The delay while we are skipping say statements.
skip_delay = 5

# basic: Archive files that are searched for images.
archives = [ ]

# Searchpath.
searchpath = [ ]

# If True, we will only try loading from archives.
# Only useful for debugging Ren'Py, don't document.
force_archives = False

# Used to control the software mouse cursor.
mouse = None

# The default sound playback sample rate.
sound_sample_rate = 48000

# The amount of time music is faded out between tracks.
fade_music = 0.0

# Should the at list be sticky?
sticky_positions = False

# A list of all of the layers that we know about.
layers = [ 'master', 'transient', 'screens', 'overlay' ]

# A list of layers that should be cleared when we replace
# transients.
transient_layers = [ 'transient' ]

# A list of layers that should be cleared when we recompute
# overlays.
overlay_layers = [ 'overlay' ]

# A list of layers that should be cleared when we enter a
# new context.
context_clear_layers = [ 'screens' ]

# A list of layers that are displayed atop all other layers, and do
# not participate in transitions.
top_layers = [ ]

# True if we want to show overlays during wait statements, or
# false otherwise.
overlay_during_with = True

# True if we want to allow the fast dissolve.
enable_fast_dissolve = True

# When using the keyboard to navigate, how much we penalize
# distance out of the preferred direction.
focus_crossrange_penalty = 1024

# If True, then we force all loading to occur before transitions
# start.
load_before_transition = True

# The keymap that is used to change keypresses and mouse events.
keymap = { }

# The default keymap, used when a binding isn't found in keymap.
default_keymap = { }

# Should we try to support joysticks?
joystick = True

# A list of functions that are called when an interaction is
# started or restarted.
interact_callbacks = [ ]

# A list of functions that are called when an interaction is started.
start_interact_callbacks = [ ]

# A list of functions that are called when a say statement
# is sustained.
say_sustain_callbacks = [ ]

# A function that is called to see if say should allow
# itself to be dismissed.
say_allow_dismiss = None

# A function that is called to tokenize text.
text_tokenizer = None

# The number of characters per AFM time period.
afm_characters = 250

# The number of bonus characters to add to a string for afm.
afm_bonus = 25

# A function that must return True for afm mode to forward.
afm_callback = None

# The amount of time we delay before making an automatic
# choice from a menu. This can be used for making a demo version of a
# game. It should be set to None in a deployed game.
auto_choice_delay = None

# A map from font, bold, italic to font, bold, italic. This is used
# to replace (say) the italic version of a regular font with the regular
# version of an italic font.
font_replacement_map = { }

# A callback that is called when a with statement (but not
# the with clause of a say or menu statement) executes. If not None,
# it's called with a single argument, the transition supplied to the
# with clause.
with_callback = None

# The framerate limit, in frames per second.
framerate = 100

# The number of frames that Ren'Py has shown.
frames = 0

# NOT USED: A text editor that is launched at the location of the current
# statement.
editor = None  # os.environ.get('RENPY_EDITOR', None)

# NOT USED: Text editor, with arguments to reload or clobber the file - used,
# for example, to display traceback.txt.
editor_transient = None  # os.environ.get('RENPY_EDITOR_TRANSIENT', editor)

# NOT USED: The separator used between files in the text editor.
editor_file_separator = None  # os.environ.get('RENPY_EDITOR_FILE_SEPARATOR', '" "')

# Enable developer mode?
developer = False  # Changed to True or False in the init code.

# The original value of config.developer.
original_developer = False

# A logfile that logging messages are sent to.
log = None

# Lint hooks.
lint_hooks = [ ]

# Hyperlink styler.
hyperlink_styler = None

# Hyperlink callback.
hyperlink_callback = None

# Hyperlink focus.
hyperlink_focus = None

# Should SFonts be recolored? internal.
recolor_sfonts = True

# Function that is called to layout text.
text_layout = None

# A callback that is called 20 times a second.
periodic_callback = None
periodic_callbacks = [ ]

# Should we check that all style properties are in style_properties? (Internal)
check_properties = True

# If True, then we implicily do a with None after every interaction.
implicit_with_none = True

# A map from a layer to (x, y, w, h) tuples that the layer is clipped to.
layer_clipping = { }

# Should we disable the fullscreen optimization?
disable_fullscreen_opt = False

# Should we reject midi files?
reject_midi = True

# Default character callback.
character_callback = None

# Character callback list.
all_character_callbacks = [ ]

# The number of autosave slots we have.
autosave_slots = 10

# How often do we autosave. (Number of interactions, sort of.)
autosave_frequency = int(os.environ.get("RENPY_AUTOSAVE_FREQUENCY", "200"))

# The callback that is used by the scene statement.
scene = renpy.exports.scene

# The callback that is used by the show statement.
show = renpy.exports.show

# The callback that is used by the hide statement.
hide = renpy.exports.hide

# Should we use cPickle or pickle for load/save?
use_cpickle = True

# The function to call as the inspector.
inspector = None

# Should we reject backslashes in filenames?
reject_backslash = True

# Hide the mouse.
mouse_hide_time = 30

# Called when we can't load an image.
missing_image_callback = None

# Called to filter text in the say and menu statements.
say_menu_text_filter = None

# Used to replace one label with another.
label_overrides = { }

# Called to get the extra_info for an auto_save.
auto_save_extra_info = None

# The directory (underneath ~/RenPy, ~/Library/RenPy, or ~/.renpy) where the
# game-specific data is saved.
save_directory = None

# These are used to deal with the case where a picture is missing.
missing_scene = None
missing_show = None
missing_hide = None

# This is called when control is transferred to a label.
label_callback = None

# A function that is called when the window needs to be shown.
empty_window = None

# A list of functions that are called when the window is shown.
window_overlay_functions = [ ]

# Do we support right-to-left languages?
rtl = False

# A callback for file opening.
file_open_callback = None

# The size of screenshot thumbnails. (Redefined in common/)
thumbnail_width = None
thumbnail_height = None

# The end game transition.
end_game_transition = None

# The default transform.
default_transform = None

# Should we use the child position?
transform_uses_child_position = True

# The action to use when it's time to quit.
quit_action = None

# If not None, a rectangle giving the area of the screen to crop the
# screenshots to.
screenshot_crop = None

# Various directories.
gamedir = None
basedir = None
renpy_base = None
commondir = None
logdir = None  # Where log and error files go.

# Should we enable OpenGL mode?
gl_enable = True

# A list of callbacks that are called by renpy.mode.
mode_callbacks = [ ]

# Should MoveTransition take offsets into account?
movetransition_respects_offsets = True

# Do we care about the pos and anchor attributes of an ImageReference's
# style?
imagereference_respects_position = False

# Do we want to try to pretend to be android?
simulate_android = False

# Do we want to enable imagemap caching?
imagemap_cache = True

# Callbacks that are called in order to predict images.
predict_callbacks = [ ]

# Should screens be predicted?
predict_screens = True

# Should we use the new choice screen format?
choice_screen_chosen = True

# Should the narrator speak menu labels?
narrator_menu = False

# A list of screen variants to use.
variants = [ None ]

# A function from (auto_parameter, variant) -> displayable.
imagemap_auto_function = None

# Should we keep the running transform when we merely change the image?
keep_running_transform = True

# Should we use image attributes?
image_attributes = True

# Should we use the new version of the character image argument?
new_character_image_argument = True

# A transition that is performed when a say statement has an image attribute
# corresponding to a shown image.
say_attribute_transition = None

# What is the name and version of this game?
name = ""
version = ""

# Should we log?
log_enable = False

# Should we log text overflows?
debug_text_overflow = False

# Should we save the window size in the preferences?
save_physical_size = True

# Do we use new text substitutions?
new_substitutions = True

# Do we use old text substitutions?
old_substitutions = True

# The graphics renderer we use. (Ren'Py sets this.)
renderer = "auto"

# The translator to use, if any. (Not used anymore.)
translator = None

# Should we use the old, broken line spacing code?
broken_line_spacing = False

# A list of callbacks that are called after each non-init-phase python
# block.
python_callbacks = [ ]

# If true, we dump information about a save upon save.
save_dump = False

# Can we resize a gl window?
gl_resize = True

# Called when we change the translation.
change_language_callbacks = [ ]

# The translation directory.
tl_directory = "tl"

# Key repeat timings. A tuple giving the initial delay and the delay between
# repeats, in seconds.
key_repeat = (.3, .03)

# A callback that is called with the character's voice_tag.
voice_tag_callback = None

# A list of callbacks that can be used to add JSON to save files.
save_json_callbacks = [ ]

# The duration of a longpress, in seconds.
longpress_duration = .5

# The radius the longpress has to remain within, in pixels.
longpress_radius = 15

# How long we vibrate the device upon a longpress.
longpress_vibrate = .1

# A list of callbacks that are called before each statement, with the name
# of the statement.
statement_callbacks = [ ]

# A list of file extensions that are blacklisted by autoreload.
autoreload_blacklist = [ ".rpyc", ".rpymc", ".rpyb", ".pyc", ".pyo" ]

# The layer dialogue is shown on.
say_layer = "screens"

# The layer the choice screen is shown on.
choice_layer = "screens"

# If true, we will not use the .report_traceback method to produced
# prettier tracebacks.
raw_tracebacks = ("RENPY_RAW_TRACEBACKS" in os.environ)

# A function to process texts which should be spoken
tts_function = renpy.display.tts.default_tts_function

# Channels that stop voice playback.
tts_voice_channels = [ "voice" ]

# The number of copies of each screen to keep in the screen cache.
screen_cache_size = 4

# A callback that adjusts the physical size of the screen.
adjust_view_size = None

# True if we should autosave when a choice occurs.
autosave_on_choice = True

# A list of channels we should emphasize the audio on.
emphasize_audio_channels = [ 'voice' ]

# What we should lower the volume of non-emphasized channels to.
emphasize_audio_volume = 0.5

# How long we should take to raise and lower the volume when emphasizing
# audio.
emphasize_audio_time = 0.5

# Should we transition screens, or always use their new states.
transition_screens = True

# A function that given the current statement identifier, returns a list
# of statement identifiers that should be predicted.
predict_statements_callback = None

# Should we use hardware video on platforms that support it?
hw_video = True

# A function to use to dispatch gestures.
dispatch_gesture = None

# The table mapping gestures to events used by the default function.
gestures = {
    "n_s_w_e_w_e" : "progress_screen",
    }

# Sizes of gesture components and strokes, as a fraction of screen_width.
gesture_component_size = .05
gesture_stroke_size = .2

# Should we log to stdout rather than files?
log_to_stdout = False

# new-style custom text tags.
custom_text_tags = { }

# A function that given the text from a TEXT token, returns a replacement text.
replace_text = None

# A function that is called when a label is missing.
missing_label_callback = None

# Should show preserve zorder when not explicitly set?
preserve_zorder = True

# The set of names to ignore.
lint_ignore_replaces = [ 'help', 'quit' ]

# How long should the presplash be kept up for?
minimum_presplash_time = 0.0

# Should Ren'Py use nearest-neighbor filtering by default.
nearest_neighbor = False

# Should Ren'Py use the drawable resolution at all? (For RTT, Text, etc?)
use_drawable_resolution = bool(int(os.environ.get("RENPY_USE_DRAWABLE_RESOLUTION", "1")))

# Should text layout occur at drawable resolution?
drawable_resolution_text = bool(int(os.environ.get("RENPY_DRAWABLE_RESOLUTION_TEXT", "1")))

# Should we fill the virtual-resolution text box?
draw_virtual_text_box = bool(int(os.environ.get("RENPY_DRAW_VIRTUAL_TEXT_BOX", "0")))

# Bindings of gamepad buttons.
pad_bindings = { }

# A list of pygame events that should be enabled in addition to the standard
# events.
pygame_events = [ ]

# A function that is used to map a gamepad event into a list of Ren'Py
# events.
map_pad_event = None

# This is called when a replay finishes.
after_replay_callback = None

# Should Ren'Py wrap shown transforms in an ImageReference?
wrap_shown_transforms = True

# A list of prefixes Ren'Py will search for assets.
search_prefixes = [ "", "images/" ]

# Should Ren'Py clear the database of code lines?
clear_lines = True

# Special namespaces for define and default.
special_namespaces = { }

# Should Ren'Py log lines?
line_log = False

# Should Ren'Py process dynamic images?
dynamic_images = True

# Should Ren'Py save when the mobile app may terminate?
save_on_mobile_background = True

# Should Ren'Py quit on mobile background?
quit_on_mobile_background = False

# Should Ren'Py pass the raw joystick (not controller) events.?
pass_joystick_events = False

# A list of screens that should be shown when the overlay is enabled.
overlay_screens = [ ]

# A map from tag to the default layer that tag should be displayed on.
tag_layer = { }

# The default layer for tags not in in tag_layer.
default_tag_layer = 'master'

# A map from tag to the default transform that's used for that tag.
tag_transform = { }

# A map from the tag to the default zorder that's used for that tag.
tag_zorder = { }

# The width of lines logged with renpy.log.
log_width = 78

# The size of the rollback side, as a fraction of the screen.
rollback_side_size = .2

# If dpi_scale is less than this, make it 1.0.
de_minimus_dpi_scale = 1.0

# Not used.
windows_dpi_scale_head = 1.0

# Should rollback_side be enabled?
enable_rollback_side = True

# The default contents of the replay scope.
replay_scope = { "_game_menu_screen" : "preferences" }

# The mixer to use for auto-defined movie channels.
movie_mixer = "music"

# Auto audio channels. A map from base name to:
# * mixer
# * file prefix
# * file suffix
auto_channels = { "audio" : ( "sfx", "", ""  ) }

# The channel used by renpy.play.
play_channel = "audio"

# An image attribute that is added when the character is speaking, and
# removed when the character is not.
speaking_attribute = None

# How many elements need to be in a list before we compress it for rollback.
list_compression_length = 25

# How many elements of history are kept. None to disable history.
history_length = None

# History callbacks that annotate additional information onto the History
# object.
history_callbacks = [ ]

# Should we use the new order for translate blocks?
new_translate_order = True

# Should we defer style execution until translate block time?
defer_styles = False

# A list of stores that should be cleaned on translate.
translate_clean_stores = [ ]

# A list of additional script files that should be translated.
translate_files = [ ]

# A list of files for which ##<space> comment sequences should also be
# translated.
translate_comments = [ ]

# Should we pass the full argument list to the say screen?
old_say_args = False

# The text-to-speech voice.
tts_voice = None

# The maximum size of xfit, yfit, first_fit, etc.
max_fit_size = 8192

# Should the window max size be enforced?
enforce_window_max_size = True

# The max priority to translate to.
translate_launcher = False

# A map from language to a list of callbacks that are used to help set it
# up.
language_callbacks = collections.defaultdict(list)

# A function that is called to init system styles.
init_system_styles = None

# Callbacks that are called just before rebuilding styles.
build_styles_callbacks = [ ]

# Should movie displayables be given their own channels?
auto_movie_channel = True

# Should we ignore duplicate labels?
ignore_duplicate_labels = False

# A list of callbacks when creating a line log entry.
line_log_callbacks = [ ]

# A list of screens for which screen profiling should be enabled.
profile_screens = [ ]

# Should Ren'Py search for system fonts.
allow_sysfonts = False

# Should Ren'Py tightly loop during fadeouts? (That is, not stop the fadeout
# if it reaches the end of a trac.)
tight_loop_default = True

# Should Ren'Py apply style_prefix to viewport scrollbar styles?
prefix_viewport_scrollbar_styles = True

# These functions are called to determine if Ren'Py needs to redraw the screen.
needs_redraw_callbacks = [ ]

del renpy
del os


def init():
    pass
