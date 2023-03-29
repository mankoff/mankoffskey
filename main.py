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
    QUOT=KC.Q; COMM=KC.W; DOT=KC.E
    P=KC.R; Y=KC.T; F=KC.Y; G=KC.U; C=KC.I; R=KC.O; L=KC.P
    A=KC.A; O=KC.S; E=KC.D; U=KC.F; I=KC.G; D=KC.H; H=KC.J; T=KC.K; N=KC.L; S=KC.SCLN
    SCLN=KC.Z; Q=KC.X; J=KC.C; K=KC.V; X=KC.B; B=KC.N; M=KC.M
    W=KC.COMM; V=KC.DOT; Z=KC.SLSH
    GRV=KC.GRV

keyboard.keymap = [
    [  # Dvorak
        KC.LT(3, KC.ESC), KC.N1,   KC.N2,   KC.N3,  KC.N4,    KC.N5,                     KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, XXXXXXX,\
        XXXXXXX, DV.COMM, DV.QUOT, DV.DOT,  DV.P,    DV.Y,                      DV.F,  DV.G,  DV.C,  DV.R,  DV.L,  XXXXXXX,\
        XXXXXXX, DV.A,    DV.O,    DV.E,    DV.U,    DV.I,                      DV.D,  DV.H,  DV.T,  DV.N,  DV.S,  XXXXXXX, \
        XXXXXXX, DV.GRV,  DV.Q,    DV.J,    DV.K,    DV.X, XXXXXXX,    XXXXXXX, DV.B,  DV.M,  DV.W,  DV.V,  DV.Z,  XXXXXXX, \
                              XXXXXXX, KC.ESC,  KC.LCTL,  KC.ENT,          KC.LSFT, KC.SPACE, KC.BSPACE, XXXXXXX,
    ],

    [  # QWERTY
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
        KC.TAB,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSPC,\
        KC.LCTL,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,\
        KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B, XXXXXXX,      XXXXXXX,  KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.RSFT,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ],
    
    [  # LOWER
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
        KC.ESC,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                         KC.N6,   KC.N7,  KC.N8,   KC.N9,   KC.N0, KC.BSPC,\
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT, XXXXXXX, XXXXXXX,\
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX,    XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
                                          XXXXXXX, KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT, XXXXXXX,
    ],

    [ # 3: Fn
        _______, _______, _______, _______, _______, _______,                         _______, _______, _______, _______, _______, _______, \
        _______, _______, _______, KC.VOLU, _______, _______,                         KC.F12, KC.F7, KC.F8, KC.F9, _______, _______, \
        _______, _______, _______, KC.VOLD, _______, _______,                         KC.F11, KC.F4, KC.F5, KC.F6, _______, _______, \
        _______, _______, _______, KC.MUTE, _______, _______,XXXXXXX,       XXXXXXX,  KC.F10, KC.F1, KC.F2, KC.F3, _______, _______, \
                              XXXXXXX, _______, _______, _______,             _______, _______, _______, XXXXXXX,
    ],

]

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.USB)
