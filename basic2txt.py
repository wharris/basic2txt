#!/usr/bin/env python
# encoding: utf-8

# This source code in this file is licensed to You by Castle Technology
# Limited ("Castle") and its licensors on contractual terms and conditions
# ("Licence") which entitle you freely to modify and/or to distribute this
# source code subject to Your compliance with the terms of the Licence.
# 
# This source code has been made available to You without any warranties
# whatsoever. Consequently, Your use, modification and distribution of this
# source code is entirely at Your own risk and neither Castle, its licensors
# nor any other person who has contributed to this source code shall be
# liable to You for any loss or damage which You may suffer as a result of
# Your use, modification or distribution of this source code.
# 
# Full details of Your rights and obligations are set out in the Licence.
# You should have received a copy of the Licence with this source code file.
# If You have not received a copy, the text of the Licence is available
# online at www.castle-technology.co.uk/riscosbaselicence.htm

"""
basic2txt.py
Translate BBC BASIC V file to UTF-8.

Ultimately derived by Will Harris on 2009-08-06 from RISC OS.
"""

import sys
import os

words = {
    "TAND": "AND",
    "TABS": "ABS",
    "TACS": "ACS",
    "TADC": "ADVAL",
    "TASC": "ASC",
    "TASN": "ASN",
    "TATN": "ATN",
    "TAUTO": "AUTO",
    "TAPPEND": "APPEND",
    "TBGET": "BGET",
    "TBPUT": "BPUT",
    "TBEATS": "BEATS",
    "TBEAT": "BEAT",
    "TTEXT": "COLOUR",
    "TCALL": "CALL",
    "TCASE": "CASE",
    "TCHAIN": "CHAIN",
    "TCHRD": "CHR$",
    "TCLEAR": "CLEAR",
    "TCLOSE": "CLOSE",
    "TCLG": "CLG",
    "TCLS": "CLS",
    "TCOS": "COS",
    "TCOUNT": "COUNT",
    "TCIRCLE": "CIRCLE",
    "TCRUNCH": "CRUNCH",
    "TTEXT": "COLOR",
    "TDATA": "DATA",
    "TDEG": "DEG",
    "TDEF": "DEF",
    "TDELET": "DELETE",
    "TDIV": "DIV",
    "TDIM": "DIM",
    "TDRAW": "DRAW",
    "TENDPR": "ENDPROC",
    "TEDIT": "EDIT",
    "TENDWH": "ENDWHILE",
    "TENDCA": "ENDCASE",
    "TENDIF": "ENDIF",
    "TEND": "END",
    "TENVEL": "ENVELOPE",
    "TELSE": "ELSE",
    "TEVAL": "EVAL",
    "TERL": "ERL",
    "TERROR": "ERROR",
    "TEOF": "EOF",
    "TEOR": "EOR",
    "TERR": "ERR",
    "TEXP": "EXP",
    "TEXT": "EXT",
    "TELLIPSE": "ELLIPSE",
    "TFOR": "FOR",
    "TFALSE": "FALSE",
    "TFILL": "FILL",
    "TFN": "FN",
    "TGOTO": "GOTO",
    "TGETD": "GET$",
    "TGET": "GET",
    "TGOSUB": "GOSUB",
    "TGRAPH": "GCOL",
    "THIMEM": "HIMEM",
    "THELP": "HELP",
    "TINPUT": "INPUT",
    "TIF": "IF",
    "TINKED": "INKEY$",
    "TINKEY": "INKEY",
    "TINT": "INT",
    "TINSTR": "INSTR(",
    "TINSTALL": "INSTALL",
    "TLIST": "LIST",
    "TLINE": "LINE",
    "TLOAD": "LOAD",
    "TLOMEM": "LOMEM",
    "TLOCAL": "LOCAL",
    "TLEFTD": "LEFT$(",
    "TLEN": "LEN",
    "TLET": "LET",
    "TLOG": "LOG",
    "TLN": "LN",
    "TLIBRARY": "LIBRARY",
    "TLVAR": "LVAR",
    "TMIDD": "MID$(",
    "TMODE": "MODE",
    "TMOD": "MOD",
    "TMOVE": "MOVE",
    "TMOUSE": "MOUSE",
    "TNEXT": "NEXT",
    "TNEW": "NEW",
    "TNOT": "NOT",
    "TOLD": "OLD",
    "TON": "ON",
    "TOFF": "OFF",
    "TOF": "OF",
    "TORGIN": "ORIGIN",
    "TOR": "OR",
    "TOPENU": "OPENIN",
    "TOPENO": "OPENOUT",
    "TOPENI": "OPENUP",
    "TOSCL": "OSCLI",
    "TOTHER": "OTHERWISE",
    "TOVERLAY": "OVERLAY",
    "TPRINT": "PRINT",
    "TPAGE": "PAGE",
    "TPTR": "PTR",
    "TPI": "PI",
    "TPLOT": "PLOT",
    "TPOINT": "POINT(",
    "TPSET": "POINT",
    "TPROC": "PROC",
    "TPOS": "POS",
    "TQUIT": "QUIT",
    "TRETURN": "RETURN",
    "TREPEAT": "REPEAT",
    "TREPORT": "REPORT",
    "TREAD": "READ",
    "TREM": "REM",
    "TRUN": "RUN",
    "TRAD": "RAD",
    "TRESTORE": "RESTORE",
    "TRIGHTD": "RIGHT$(",
    "TRND": "RND",
    "TRECT": "RECTANGLE",
    "TRENUM": "RENUMBER",
    "TSTEP": "STEP",
    "TSAVE": "SAVE",
    "TSGN": "SGN",
    "TSIN": "SIN",
    "TSQR": "SQR",
    "TBEEP": "SOUND",
    "TSPC": "SPC",
    "TSTRD": "STR$",
    "TSTRND": "STRING$(",
    "TSTOP": "STOP",
    "TSTEREO": "STEREO",
    "TSUM": "SUM",
    "TSWAP": "SWAP",
    "TSYS": "SYS",
    "TTAN": "TAN",
    "TTAB": "TAB(",
    "TTEMPO": "TEMPO",
    "TTEXTLOAD": "TEXTLOAD",
    "TTEXTSAVE": "TEXTSAVE",
    "TTHEN": "THEN",
    "TTIME": "TIME",
    "TTINT": "TINT",
    "TTO": "TO",
    "TTRACE": "TRACE",
    "TTRUE": "TRUE",
    "TTWINO": "TWINO",
    "TTWIN": "TWIN",
    "TUNTIL": "UNTIL",
    "TUSR": "USR",
    "TVDU": "VDU",
    "TVAL": "VAL",
    "TVPOS": "VPOS",
    "TVOICES": "VOICES",
    "TVOICE": "VOICE",
    "TWHILE": "WHILE",
    "TWHEN": "WHEN",
    "TWAIT": "WAIT",
    "TWIDTH": "WIDTH",
}

escapes = {
    None: {
        127: 'TOTHER',
        128: 'TAND',
        129: 'TDIV',
        130: 'TEOR',
        131: 'TMOD',
        132: 'TOR',
        133: 'TERROR',
        134: 'TLINE',
        135: 'TOFF',
        136: 'TSTEP',
        137: 'TSPC',
        138: 'TTAB',
        139: 'TELSE',
        140: 'TTHEN',
        141: 'TCONST',
        142: 'TOPENU',
        143: 'TPTR',
        144: 'TPAGE',
        145: 'TTIME',
        146: 'TLOMEM',
        147: 'THIMEM',
        148: 'TABS',
        149: 'TACS',
        150: 'TADC',
        151: 'TASC',
        152: 'TASN',
        153: 'TATN',
        154: 'TBGET',
        155: 'TCOS',
        156: 'TCOUNT',
        157: 'TDEG',
        158: 'TERL',
        159: 'TERR',
        160: 'TEVAL',
        161: 'TEXP',
        162: 'TEXT',
        163: 'TFALSE',
        164: 'TFN',
        165: 'TGET',
        166: 'TINKEY',
        167: 'TINSTR',
        168: 'TINT',
        169: 'TLEN',
        170: 'TLN',
        171: 'TLOG',
        172: 'TNOT',
        173: 'TOPENI',
        174: 'TOPENO',
        175: 'TPI',
        176: 'TPOINT',
        177: 'TPOS',
        178: 'TRAD',
        179: 'TRND',
        180: 'TSGN',
        181: 'TSIN',
        182: 'TSQR',
        183: 'TTAN',
        184: 'TTO',
        185: 'TTRUE',
        186: 'TUSR',
        187: 'TVAL',
        188: 'TVPOS',
        189: 'TCHRD',
        190: 'TGETD',
        191: 'TINKED',
        192: 'TLEFTD',
        193: 'TMIDD',
        194: 'TRIGHTD',
        195: 'TSTRD',
        196: 'TSTRND',
        197: 'TEOF',
        198: 'TESCFN',
        199: 'TESCCOM',
        200: 'TESCSTMT',
        201: 'TWHEN',
        202: 'TOF',
        203: 'TENDCA',
        204: 'TELSE',
        205: 'TENDIF',
        206: 'TENDWH',
        207: 'TPTR',
        208: 'TPAGE2',
        209: 'TTIME2',
        210: 'TLOMM2',
        211: 'THIMM2',
        212: 'TBEEP',
        213: 'TBPUT',
        214: 'TCALL',
        215: 'TCHAIN',
        216: 'TCLEAR',
        217: 'TCLOSE',
        218: 'TCLG',
        219: 'TCLS',
        220: 'TDATA',
        221: 'TDEF',
        222: 'TDIM',
        223: 'TDRAW',
        224: 'TEND',
        225: 'TENDPR',
        226: 'TENVEL',
        227: 'TFOR',
        228: 'TGOSUB',
        229: 'TGOTO',
        230: 'TGRAPH',
        231: 'TIF',
        232: 'TINPUT',
        233: 'TLET',
        234: 'TLOCAL',
        235: 'TMODE',
        236: 'TMOVE',
        237: 'TNEXT',
        238: 'TON',
        239: 'TVDU',
        240: 'TPLOT',
        241: 'TPRINT',
        242: 'TPROC',
        243: 'TREAD',
        244: 'TREM',
        245: 'TREPEAT',
        246: 'TREPORT',
        247: 'TRESTORE',
        248: 'TRETURN',
        249: 'TRUN',
        250: 'TSTOP',
        251: 'TTEXT',
        252: 'TTRACE',
        253: 'TUNTIL',
        254: 'TWIDTH',
        255: 'TOSCL'
    },
    199: {              # TESCCOM
        142: 'TAPPEND',
        143: 'TAUTO',
        144: 'TCRUNCH',
        145: 'TDELET',
        146: 'TEDIT',
        147: 'THELP',
        148: 'TLIST',
        149: 'TLOAD',
        150: 'TLVAR',
        151: 'TNEW',
        152: 'TOLD',
        153: 'TRENUM',
        154: 'TSAVE',
        155: 'TTEXTLOAD',
        156: 'TTEXTSAVE',
        157: 'TTWIN',
        158: 'TTWINO',
        159: 'TINSTALL',
        160: 'TTWOCOMMLIMIT'
    },
    198: {              # TESCFN
        142: 'TSUM',
        143: 'TBEAT',
        144: 'TTWOFUNCLIMIT'
    },
    200: {              # TESCSTMT
        142: 'TCASE',
        143: 'TCIRCLE',
        144: 'TFILL',
        145: 'TORGIN',
        146: 'TPSET',
        147: 'TRECT',
        148: 'TSWAP',
        149: 'TWHILE',
        150: 'TWAIT',
        151: 'TMOUSE',
        152: 'TQUIT',
        153: 'TSYS',
        154: 'TINSTALLBAD',
        155: 'TLIBRARY',
        156: 'TTINT',
        157: 'TELLIPSE',
        158: 'TBEATS',
        159: 'TTEMPO',
        160: 'TVOICES',
        161: 'TVOICE',
        162: 'TSTEREO',
        163: 'TOVERLAY',
        164: 'TTWOSTMTLIMIT'
    }
}

def parseline(stream):
    ch = stream.read(1)
    
    if ch != chr(0x0d):
        raise SyntaxError, "Missing line start indicator"
    
    line_high_byte = ord(stream.read(1))
    
    if line_high_byte == 0xff:
        return None
    
    line_low_byte = ord(stream.read(1))
    line_length = ord(stream.read(1))
    line_text = stream.read(line_length - 4)
    
    return line_high_byte * 256 + line_low_byte, detokenize(line_text)

def detokenize(text):
    result = []
    tokens = escapes[None]
    is_in_string = False
    for ch in text:
        if ord(ch) < 0x7F or is_in_string:
            result += ch
            if ch == '"':
                is_in_string = not is_in_string
        else:
            if ord(ch) in escapes:
                tokens = escapes[ord(ch)]
            else:
                result += words[tokens[ord(ch)]]
                tokens = escapes[None]
    return "".join(result)

def main():
    while True:
        line = parseline(sys.stdin)
        if line is None:
            break
        
        print unicode("%s" % line[1], 'latin-1').encode('utf-8')

if __name__ == '__main__':
    main()
