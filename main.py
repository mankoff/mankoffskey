from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
from kmk.modules.split import Split, SplitSide, SplitType
keyboard = KMKKeyboard()
modtap = ModTap()
layers_ext = Layers()
keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap)

from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())

from kmk.modules.mouse_keys import MouseKeys
keyboard.modules.append(MouseKeys())

from kmk.modules.oneshot import OneShot
oneshot = OneShot()
# optional: set a custom tap timeout in ms (default: 1000ms)
# oneshot.tap_time = 1500
keyboard.modules.append(oneshot)

# TODO Comment one of these on each side
split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
split = Split(split_side = split_side,use_pio=True)
keyboard.modules.append(split)

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
ADJUST = KC.LT(3, KC.SPC)

class DV:
    # https://kmkfw.zulipchat.com/user_uploads/49575/-m7O9LXFqS9ilkgMYVT5D2Iz/dvorkeys-4110265058.png
    QUOT=KC.Q; COMM=KC.W; DOT=KC.E
    P=KC.R; Y=KC.T; F=KC.Y; G=KC.U; C=KC.I; R=KC.O; L=KC.P
    A=KC.A; O=KC.S; E=KC.D; U=KC.F; I=KC.G; D=KC.H; H=KC.J; T=KC.K; N=KC.L; S=KC.SCLN
    SCLN=KC.Z; Q=KC.X; J=KC.C; K=KC.V; X=KC.B; B=KC.N; M=KC.M
    W=KC.COMM; V=KC.DOT; Z=KC.SLSH
    GRV=KC.GRV

    LBRC=KC.MINS; RBRC=KC.EQL
    LCBR=KC.UNDS; RCBR=KC.PLUS
    SLSH=KC.LBRC; EQL=KC.RBRC
    PLUS=KC.LSFT(KC.RBRC); MINS=KC.QUOT
    COLN=KC.LSFT(KC.Z)


# [ # n: desc
#     _______, _______, _______, _______, _______, _______,                      _______, _______, _______, _______, _______, _______, \
#     _______, _______, _______, _______, _______, _______,                      _______, _______, _______, _______, _______, _______, \
#     _______, _______, _______, _______, _______, _______,                      _______, _______, _______, _______, _______, _______, \
#     _______, _______, _______, _______, _______, _______, _______,    _______, _______, _______, _______, _______, _______, _______, \
#                            _______, _______, _______, _______,             _______, _______, _______, _______,
# ],

# http://kmkfw.io/docs/keycodes

keyboard.keymap = [

[ # 0: Dvorak
    KC.LT(4, KC.ESC), KC.N1,   KC.N2,   KC.N3,  KC.N4,    KC.N5,                     KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, XXXXXXX,\
    XXXXXXX, DV.COMM, DV.QUOT, DV.DOT,  DV.P,    DV.Y,                      DV.F,  DV.G,  DV.C,  DV.R,  DV.L,  XXXXXXX,\
    XXXXXXX, DV.A,    DV.O,    DV.E,    DV.U,    DV.I,                      DV.D,  DV.H,  DV.T,  DV.N,  DV.S,  XXXXXXX, \
    XXXXXXX, DV.GRV,  DV.Q,    DV.J,    DV.K,    DV.X, XXXXXXX,    XXXXXXX, DV.B,  DV.M,  DV.W,  DV.V,  DV.Z,  XXXXXXX, \
    KC.LT(1, KC.ESC), KC.LALT,  KC.LCTL,  KC.ENT,          KC.LSFT, KC.LT(2, KC.SPACE), KC.LT(3, KC.BSPACE), XXXXXXX,
],

[ # 1: Nav
    _______, _______, _______, _______, _______, _______,                      _______, _______, _______, _______, _______, _______, \
    _______, _______, _______, _______, _______, _______,                      KC.MW_UP, _______, KC.UP,   _______, _______, _______, \
    _______, _______, _______, _______, _______, _______,                      KC.MW_DN, KC.LEFT, KC.DOWN, KC.RGHT, KC.MS_UP, _______, \
    _______, _______, KC.PGUP, KC.PGDN, _______, _______, _______,    _______, _______, _______, _______, KC.MS_LT, KC.MS_DN, KC.MS_RT, \
                           _______, _______, _______, _______,             _______, _______, _______, _______,
],
    
[ # 2: Num
    _______, _______, _______, _______, _______, _______,                         _______, _______, _______, _______, _______, _______, \
    _______, _______, DV.COMM, KC.LPRN, KC.RPRN, DV.SLSH,                         DV.PLUS, KC.N7, KC.N8, KC.N9, KC.N0, DV.PLUS, \
    _______, _______, DV.DOT,  DV.LBRC, DV.RBRC, KC.ASTR,                         DV.MINS, KC.N4, KC.N5, KC.N6, KC.N0, DV.MINS, \
    DV.COLN, _______, _______, DV.LCBR, DV.RCBR, KC.BSLS, XXXXXXX,       XXXXXXX, DV.EQL,  KC.N1, KC.N2, KC.N3, KC.N0, DV.COLN, \
                           XXXXXXX, KC.SPC,  KC.BSPC, KC.LALT,             _______, _______, _______, XXXXXXX,

],

[ # 3: Sym
    _______, _______, _______, _______, _______, _______,                         _______, _______, _______, _______, _______, _______, \
    _______, _______, _______, _______, KC.PERC, _______,                         _______, KC.CIRC, _______, _______, _______, _______, \
    _______, KC.EXLM, KC.AMPR, KC.AT,   KC.HASH, _______,                          _______, KC.TILD, DV.SLSH, KC.PIPE, KC.BSLS, _______, \
    _______, _______, _______, _______, KC.DLR,  _______, KC.OS(KC.RALT), XXXXXXX, _______, _______, KC.BSLS, _______, _______, _______, \
                            XXXXXXX, _______, _______, _______,               _______, _______, _______, XXXXXXX,
],
    
[ # 4: Fn
    _______, _______, _______, _______, _______, _______,                         _______, _______, _______, _______, _______, _______, \
    _______, _______, _______, KC.VOLU, _______, _______,                         KC.F12, KC.F7, KC.F8, KC.F9, _______, _______, \
    _______, _______, _______, KC.VOLD, _______, _______,                         KC.F11, KC.F4, KC.F5, KC.F6, _______, _______, \
    _______, _______, _______, KC.MUTE, _______, _______,XXXXXXX,       XXXXXXX,  KC.F10, KC.F1, KC.F2, KC.F3, _______, _______, \
    XXXXXXX, _______, _______, _______,             _______, _______, _______, XXXXXXX,
],

]

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.USB)
