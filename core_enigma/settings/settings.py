
NUMBERS = ['01','02','03','04','05','06','07','08','09','10','11','12','13',
           '14','15','16','17','18','19','20','21','22','23','24','25','26']
LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
QWERTZ = ['Q','W','E','R','T','Z','U','I','O','A','S','D','F',
          'G','H','J','K','P','Y','X','C','V','B','N','M','L']

EQUIPMENT_DICT = {
	"ENIGMA D":{
	    "ENTRY_WHEEL":QWERTZ,
        "ROTORS":{
            "I":{
                "wiring_chars":['L','P','G','S','Z','M','H','A','E','O','Q','K','V',
                                 'X','R','F','Y','B','U','T','N','I','C','J','D','W'],
                "turnover_chars":['Y']
                },
            "II":{
                "wiring_chars":['S','L','V','G','B','T','F','X','J','Q','O','H','E',
                                 'W','I','R','Z','Y','A','M','K','P','C','N','D','U'],
                "turnover_chars":['E']
                },
            "III":{
                "wiring_chars":['C','J','G','D','P','S','H','K','T','U','R','A','W',
                                 'Z','X','F','M','Y','N','Q','O','B','V','L','I','E'],
                "turnover_chars":['N']
                }
            },
        "REFLECTORS":{
            "UKW":{
                "wiring_chars":['I','M','E','T','C','G','F','R','A','Y','S','Q','B',
                                 'Z','X','W','L','H','K','D','V','U','P','O','J','N'],
                "mode":"rotating"
                }
            },
        "RING_CHARACTERS":LETTERS,
        "ROTOR_GROUP_CELLS":{"R1":"R_ROT",
                             "R2":"R_ROT",
                             "R3":"R_ROT",
                             "REF":"R_REF"},
        "PLUGBOARD":None
    },

	"WEHRMACHT":{
	    "ENTRY_WHEEL":LETTERS,
        "ROTORS":{
            "I":{
                "wiring_chars":['E','K','M','F','L','G','D','Q','V','Z','N','T','O',
                                 'W','Y','H','X','U','S','P','A','I','B','R','C','J'],
                "turnover_chars":['Q']
                },
            "II":{
                "wiring_chars":['A','J','D','K','S','I','R','U','X','B','L','H','W',
                                  'T','M','C','Q','G','Z','N','P','Y','F','V','O','E'],
                "turnover_chars":['E']
                },
            "III":{
                "wiring_chars":['B','D','F','H','J','L','C','P','R','T','X','V','Z',
                                 'N','Y','E','I','W','G','A','K','M','U','S','Q','O'],
                 "turnover_chars":['V']},
            "IV":{"wiring_chars":['E','S','O','V','P','Z','J','A','Y','Q','U','I','R',
                                   'H','X','L','N','F','T','G','K','D','C','M','W','B'],
                  "turnover_chars":['J']
                },
            "V":{
                "wiring_chars":['V','Z','B','R','G','I','T','Y','U','P','S','D','N',
                                 'H','L','X','A','W','M','J','Q','O','F','E','C','K'],
                "turnover_chars":['Z']}
                },
        "REFLECTORS":{
            "UKW-A":{
                "wiring_chars":['E','J','M','Z','A','L','Y','X','V','B','W','F','C',
                                 'R','Q','U','O','N','T','S','P','I','K','H','G','D'],
                "mode":"fixed"
                },
            "UKW-B":{
                "wiring_chars":['Y','R','U','H','Q','S','L','D','P','X','N','G','O',
                                 'K','M','I','E','B','F','Z','C','W','V','J','A','T'],
                "mode":"fixed"
                },
            "UKW-C":{
                "wiring_chars":['F','V','P','J','I','A','O','Y','E','D','R','Z','X',
                                 'W','G','C','T','K','U','Q','S','B','N','M','H','L'],
                "mode":"fixed"
                }
            },
        "RING_CHARACTERS":NUMBERS,
        "ROTOR_GROUP_CELLS":{"R1":"R_ROT",
                             "R2":"R_ROT",
                             "R3":"R_ROT",
                             "REF":"F_REF"},
        "PLUGBOARD":"STECKER"
    },

	"LUFTWAFFE":{
	    "ENTRY_WHEEL":LETTERS,
        "ROTORS":{
            "I":{
                "wiring_chars":['E','K','M','F','L','G','D','Q','V','Z','N','T','O',
                                 'W','Y','H','X','U','S','P','A','I','B','R','C','J'],
                "turnover_chars":['Q']
                },
            "II":{
                "wiring_chars":['A','J','D','K','S','I','R','U','X','B','L','H','W',
                                 'T','M','C','Q','G','Z','N','P','Y','F','V','O','E'],
                "turnover_chars":['E']
                },
            "III":{
                "wiring_chars":['B','D','F','H','J','L','C','P','R','T','X','V','Z',
                                 'N','Y','E','I','W','G','A','K','M','U','S','Q','O'],
                "turnover_chars":['V']
                },
            "IV":{
                "wiring_chars":['E','S','O','V','P','Z','J','A','Y','Q','U','I','R',
                                 'H','X','L','N','F','T','G','K','D','C','M','W','B'],
                "turnover_chars":['J']
                },
            "V":{
                "wiring_chars":['V','Z','B','R','G','I','T','Y','U','P','S','D','N',
                                 'H','L','X','A','W','M','J','Q','O','F','E','C','K'],
                "turnover_chars":['Z']
                },
            "VI":{
                "wiring_chars":['J','P','G','V','O','U','M','F','Y','Q','B','E','N',
                                 'H','Z','R','D','K','A','S','X','L','I','C','T','W'],
                "turnover_chars":['Z','M']
                },
            "VII":{
                "wiring_chars":['N','Z','J','H','G','R','C','X','M','Y','S','W','B',
                                 'O','U','F','A','I','V','L','P','E','K','Q','D','T'],
                "turnover_chars":['Z','M']
                },
            "VIII":{
                "wiring_chars":['F','K','Q','H','T','L','X','O','C','B','J','S','P',
                                 'D','Z','R','A','M','E','W','N','I','U','Y','G','V'],
                "turnover_chars":['Z','M']
                },
            'Beta':{
                "wiring_chars":['L','E','Y','J','V','C','N','I','X','W','P','B','Q',
                                 'M','D','R','T','A','K','Z','G','F','U','H','O','S'],
                "turnover_chars":[]
                },
            'Gamma':{
                "wiring_chars":['F','S','O','K','A','N','U','E','R','H','M','B','T',
                                 'I','Y','C','W','L','Q','P','Z','X','V','G','J','D'],
                "turnover_chars":[]
                }
            },
        "REFLECTORS":{
            "UKW-B":{
                "wiring_chars":['Y','R','U','H','Q','S','L','D','P','X','N','G','O',
                                 'K','M','I','E','B','F','Z','C','W','V','J','A','T'],
                "mode":"fixed"
                },
            "UKW-C":{
                "wiring_chars":['F','V','P','J','I','A','O','Y','E','D','R','Z','X',
                                 'W','G','C','T','K','U','Q','S','B','N','M','H','L'],
                "mode":"fixed"
                },
            "UKW-D":{
                "wiring_chars":['B','C','D','E','F','G','H','I','J','K','L','M','N',
                                 'O','P','Q','R','S','T','U','V','W','X','Y','Z','A'],
                "mode":"rewireable"
                }
            },
        "RING_CHARACTERS":LETTERS,
        "ROTOR_GROUP_CELLS":{"R1":"R_ROT",
                             "R2":"R_ROT",
                             "R3":"R_ROT",
                             "REF":"F_REF"},
        "PLUGBOARD":"UHR"
    },

	"NOREWAY ENIGMA":{
	    "ENTRY_WHEEL":LETTERS,
        "ROTORS":{
            "I":{
                "wiring_chars":['W','T','O','K','A','S','U','Y','V','R','B','X','J',
                                 'H','Q','C','P','Z','E','F','M','D','I','N','L','G'],
                "turnover_chars":['Q']
                },
            "II":{
                "wiring_chars":['G','J','L','P','U','B','S','W','E','M','C','T','Q',
                                 'V','H','X','A','O','F','Z','D','R','K','Y','N','I'],
                "turnover_chars":['E']
                },
            "III":{
                "wiring_chars":['J','W','F','M','H','N','B','P','U','S','D','Y','T',
                                 'I','X','V','Z','G','R','Q','L','A','O','E','K','C'],
                "turnover_chars":['V']
                },
            "IV":{
                "wiring_chars":['E','S','O','V','P','Z','J','A','Y','Q','U','I','R',
                                 'H','X','L','N','F','T','G','K','D','C','M','W','B'],
                "turnover_chars":['J']
                },
            "V":{
                "wiring_chars":['H','E','J','X','Q','O','T','Z','B','V','F','D','A',
                                 'S','C','I','L','W','P','G','Y','N','M','U','R','K'],
                "turnover_chars":['Z']
                }
            },
        "REFLECTORS":{
            "UKW":{
                "wiring_chars":['M','O','W','J','Y','P','U','X','N','D','S','R','A',
                                 'I','B','F','V','L','K','Z','G','Q','C','H','E','T'],
                "mode":"fixed"
                }
            },
        "RING_CHARACTERS":LETTERS,
        "ROTOR_GROUP_CELLS":{"R1":"R_ROT",
                             "R2":"R_ROT",
                             "R3":"R_ROT",
                             "REF":"F_REF"},
        "PLUGBOARD":None
    },

	"SONDER ENIGMA":{
	    "ENTRY_WHEEL":LETTERS,
        "ROTORS":{
            "I":{
                "wiring_chars":['V','E','O','S','I','R','Z','U','J','D','Q','C','K',
                                 'G','W','Y','P','N','X','A','F','L','T','H','M','B'],
                "turnover_chars":['Q']
                },
            "II":{
                "wiring_chars":['U','E','M','O','A','T','Q','L','S','H','P','K','C',
                                 'Y','F','W','J','Z','B','G','V','X','I','N','D','R'],
                "turnover_chars":['E']
                },
            "III":{
                "wiring_chars":['T','Z','H','X','M','B','S','I','P','N','U','R','J',
                                 'F','D','K','E','Q','V','C','W','G','L','A','O','Y'],
                "turnover_chars":['V']
                }
            },
        "REFLECTORS":{
            "UKW":{
                "wiring_chars":['C','I','A','G','S','N','D','R','B','Y','T','P','Z',
                                 'F','U','L','V','H','E','K','O','Q','X','W','J','M'],
                "mode":"fixed"
                }
            },
        "RING_CHARACTERS":LETTERS,
        "ROTOR_GROUP_CELLS":{"R1":"R_ROT",
                             "R2":"R_ROT",
                             "R3":"R_ROT",
                             "REF":"F_REF"},
        "PLUGBOARD":None
    },

	"ENIGMA M3 Kriegsmarine":{
	    "ENTRY_WHEEL":LETTERS,
        "ROTORS":{
            "I":{
                "wiring_chars":['E','K','M','F','L','G','D','Q','V','Z','N','T','O',
                                 'W','Y','H','X','U','S','P','A','I','B','R','C','J'],
                "turnover_chars":['Q']
                },
            "II":{
                "wiring_chars":['A','J','D','K','S','I','R','U','X','B','L','H','W',
                                 'T','M','C','Q','G','Z','N','P','Y','F','V','O','E'],
                "turnover_chars":['E']
                },
            "III":{
                "wiring_chars":['B','D','F','H','J','L','C','P','R','T','X','V','Z',
                                 'N','Y','E','I','W','G','A','K','M','U','S','Q','O'],
                "turnover_chars":['V']
                },
            "IV":{
                "wiring_chars":['E','S','O','V','P','Z','J','A','Y','Q','U','I','R',
                                 'H','X','L','N','F','T','G','K','D','C','M','W','B'],
                "turnover_chars":['J']
                },
            "V":{
                "wiring_chars":['V','Z','B','R','G','I','T','Y','U','P','S','D','N',
                                 'H','L','X','A','W','M','J','Q','O','F','E','C','K'],
                "turnover_chars":['Z']
                },
            "VI":{
                "wiring_chars":['J','P','G','V','O','U','M','F','Y','Q','B','E','N',
                                 'H','Z','R','D','K','A','S','X','L','I','C','T','W'],
                "turnover_chars":['Z','M']
                },
            "VII":{
                "wiring_chars":['N','Z','J','H','G','R','C','X','M','Y','S','W','B',
                                 'O','U','F','A','I','V','L','P','E','K','Q','D','T'],
                "turnover_chars":['Z','M']
                },
            "VIII":{
                "wiring_chars":['F','K','Q','H','T','L','X','O','C','B','J','S','P',
                                 'D','Z','R','A','M','E','W','N','I','U','Y','G','V'],
                "turnover_chars":['Z','M']
                }
            },
        "REFLECTORS":{
            "UKW-B":{
                "wiring_chars":['Y','R','U','H','Q','S','L','D','P','X','N','G','O',
                                 'K','M','I','E','B','F','Z','C','W','V','J','A','T'],
                "mode":"fixed"
                },
            "UKW-C":{
                "wiring_chars":['F','V','P','J','I','A','O','Y','E','D','R','Z','X',
                                 'W','G','C','T','K','U','Q','S','B','N','M','H','L'],
                "mode":"fixed"
                }
            },
        "RING_CHARACTERS":LETTERS,
        "ROTOR_GROUP_CELLS":{"R1":"R_ROT",
                             "R2":"R_ROT",
                             "R3":"R_ROT",
                             "REF":"F_REF"},
        "PLUGBOARD":"STECKER"
    },

	"ENIGMA M4 u-boat":{
	    "ENTRY_WHEEL":LETTERS,
        "ROTORS":{
            "I":{
                "wiring_chars":['E','K','M','F','L','G','D','Q','V','Z','N','T','O',
                                 'W','Y','H','X','U','S','P','A','I','B','R','C','J'],
                "turnover_chars":['Q']
                },
            "II":{
                "wiring_chars":['A','J','D','K','S','I','R','U','X','B','L','H','W',
                                 'T','M','C','Q','G','Z','N','P','Y','F','V','O','E'],
                "turnover_chars":['E']
                },
            "III":{
                "wiring_chars":['B','D','F','H','J','L','C','P','R','T','X','V','Z',
                                 'N','Y','E','I','W','G','A','K','M','U','S','Q','O'],
                "turnover_chars":['V']
                },
            "IV":{
                "wiring_chars":['E','S','O','V','P','Z','J','A','Y','Q','U','I','R',
                                 'H','X','L','N','F','T','G','K','D','C','M','W','B'],
                "turnover_chars":['J']
                },
            "V":{
                "wiring_chars":['V','Z','B','R','G','I','T','Y','U','P','S','D','N',
                                 'H','L','X','A','W','M','J','Q','O','F','E','C','K'],
                "turnover_chars":['Z']
                },
            "VI":{
                "wiring_chars":['J','P','G','V','O','U','M','F','Y','Q','B','E','N',
                                 'H','Z','R','D','K','A','S','X','L','I','C','T','W'],
                "turnover_chars":['Z','M']
                },
            "VII":{
                "wiring_chars":['N','Z','J','H','G','R','C','X','M','Y','S','W','B',
                                 'O','U','F','A','I','V','L','P','E','K','Q','D','T'],
                "turnover_chars":['Z','M']
                },
            "VIII":{
                "wiring_chars":['F','K','Q','H','T','L','X','O','C','B','J','S','P',
                                 'D','Z','R','A','M','E','W','N','I','U','Y','G','V'],
                "turnover_chars":['Z','M']
                },
            "Beta":{
                "wiring_chars":['L','E','Y','J','V','C','N','I','X','W','P','B','Q',
                                 'M','D','R','T','A','K','Z','G','F','U','H','O','S'],
                "turnover_chars":[]
                },
            "Gamma":{
                "wiring_chars":['F','S','O','K','A','N','U','E','R','H','M','B','T',
                                 'I','Y','C','W','L','Q','P','Z','X','V','G','J','D'],
                "turnover_chars":[]
                }
            },
        "REFLECTORS":{
            "UKW-B":{
                "wiring_chars":['E','N','K','Q','A','U','Y','W','J','I','C','O','P',
                                 'B','L','M','D','X','Z','V','F','T','H','R','G','S'],
                "mode":"fixed"
                },
            "UKW-C":{
                "wiring_chars":['R','D','O','B','J','N','T','K','V','E','H','M','L',
                                 'F','C','W','Z','A','X','G','Y','I','P','S','U','Q'],
                "mode":"fixed"
                }
            },
        "RING_CHARACTERS":LETTERS,
        "ROTOR_GROUP_CELLS":{"R1":"R_ROT",
                             "R2":"R_ROT",
                             "R3":"R_ROT",
                             "R4":"F_ROT",
                             "REF":"F_REF"},
        "PLUGBOARD":"STECKER",
    },

	"G-312":{
	    "ENTRY_WHEEL":QWERTZ,
        "ROTORS":{
            "I":{
                "wiring_chars":['D','M','T','W','S','I','L','R','U','Y','Q','N','K',
                                 'F','E','J','C','A','Z','B','P','G','X','O','H','V'],
                "turnover_chars":['S','U','V','W','Z','A','B','C','E','F','G','I','K','L','O','P','Q']
                },
            "II":{
                "wiring_chars":['H','Q','Z','G','P','J','T','M','O','B','L','N','C',
                                 'I','F','D','Y','A','W','V','E','U','S','R','K','X'],
                "turnover_chars":['S','T','V','Y','Z','A','C','D','F','G','H','K','M','N','Q']
                },
            "III":{
                "wiring_chars":['U','Q','N','T','L','S','Z','F','M','R','E','H','D',
                                 'P','X','K','I','B','V','Y','G','J','C','W','O','A'],
                "turnover_chars":['U','W','X','A','E','F','H','K','M','N','R']
                }
            },
        "REFLECTORS":{
            "UKW":{
                "wiring_chars":['R','U','L','Q','M','Z','J','S','Y','G','O','C','E',
                                 'T','K','W','D','A','H','N','B','X','P','V','I','F'],
                "mode":"fixed"
                }
            },
        "RING_CHARACTERS":LETTERS,
        "ROTOR_GROUP_CELLS":{"R1":"R_ROT",
                             "R2":"R_ROT",
                             "R3":"R_ROT",
                             "REF":"F_REF"},
        "PLUGBOARD":None
    },

	"G-260":{
	    "ENTRY_WHEEL":QWERTZ,
        "ROTORS":{
            "I":{
                "wiring_chars":['R','C','S','P','B','L','K','Q','A','U','M','H','W',
                                 'Y','T','I','F','Z','V','G','O','J','N','E','X','D'],
                "turnover_chars":['S','U','V','W','Z','A','B','C','E','F','G','I','K','L','O','P','Q']
                },
            "II":{
                "wiring_chars":['W','C','M','I','B','V','P','J','X','A','R','O','S',
                                 'G','N','D','L','Z','K','E','Y','H','U','F','Q','T'],
                "turnover_chars":['S','T','V','Y','Z','A','C','D','F','G','H','K','M','N','Q']
                },
            "III":{
                "wiring_chars":['F','V','D','H','Z','E','L','S','Q','M','A','X','O',
                                 'K','Y','I','W','P','G','C','B','U','J','T','N','R'],
                "turnover_chars":['U','W','X','A','E','F','H','K','M','N','R']
                }
            },
        "REFLECTORS":{
            "UKW":{
                "wiring_chars":['I','M','E','T','C','G','F','R','A','Y','S','Q','B',
                                 'Z','X','W','L','H','K','D','V','U','P','O','J','N'],
                "mode":"fixed"
                }
            },
        "RING_CHARACTERS":LETTERS,
        "ROTOR_GROUP_CELLS":{"R1":"R_ROT",
                             "R2":"R_ROT",
                             "R3":"R_ROT",
                             "REF":"F_REF"},
        "PLUGBOARD":None
    },

	"ENIGMA K":{
	    "ENTRY_WHEEL":QWERTZ,
        "ROTORS":{
            "I":{
                "wiring_chars":['L','P','G','S','Z','M','H','A','E','O','Q','K','V',
                                 'X','R','F','Y','B','U','T','N','I','C','J','D','W'],
                "turnover_chars":['Y']
                },
            "II":{
                "wiring_chars":['S','L','V','G','B','T','F','X','J','Q','O','H','E',
                                 'W','I','R','Z','Y','A','M','K','P','C','N','D','U'],
                "turnover_chars":['E']
                },
            "III":{
                "wiring_chars":['C','J','G','D','P','S','H','K','T','U','R','A','W',
                                 'Z','X','F','M','Y','N','Q','O','B','V','L','I','E'],
                "turnover_chars":['N']
                }
            },
        "REFLECTORS":{
            "UKW":{
                "wiring_chars":['I','M','E','T','C','G','F','R','A','Y','S','Q','B',
                                 'Z','X','W','L','H','K','D','V','U','P','O','J','N'],
                "mode":"fixed"
                }
            },
        "RING_CHARACTERS":LETTERS,
        "ROTOR_GROUP_CELLS":{"R1":"R_ROT",
                             "R2":"R_ROT",
                             "R3":"R_ROT",
                             "REF":"R_REF"},
        "PLUGBOARD":None
    },

	"ENIGMA KD":{
	    "ENTRY_WHEEL":QWERTZ,
        "ROTORS":{
            "I":{
                "wiring_chars":['V','E','Z','I','O','J','C','X','K','Y','D','U','N',
                                 'T','W','A','P','L','Q','G','B','H','S','F','M','R'],
                "turnover_chars":['S','U','Y','A','E','H','L','N','Q']
                },
            "II":{
                "wiring_chars":['H','G','R','B','S','J','Z','E','T','D','L','V','P',
                                 'M','Q','Y','C','X','A','O','K','I','N','F','U','W'],
                "turnover_chars":['S','U','Y','A','E','H','L','N','Q']
                },
            "III":{
                "wiring_chars":['N','W','L','H','X','G','R','B','Y','O','J','S','A',
                                 'Z','D','V','T','P','K','F','Q','M','E','U','I','C'],
                "turnover_chars":['S','U','Y','A','E','H','L','N','Q']
                }
            },
        "REFLECTORS":{
            "UKW-DORA":{
                "wiring_chars":['N','S','U','O','M','K','L','I','H','Z','F','G','E',
                                 'A','D','V','X','W','B','Y','C','P','R','Q','T','J'],
                "mode":"rewireable"
                }
            },
        "RING_CHARACTERS":LETTERS,
        "ROTOR_GROUP_CELLS":{"R1":"R_ROT",
                             "R2":"R_ROT",
                             "R3":"R_ROT",
                             "REF":"F_REF"},
        "PLUGBOARD":None
    },

	"ENIGMA SWISS-K":{
	    "ENTRY_WHEEL":QWERTZ,
        "ROTORS":{
            "I":{
                "wiring_chars":['P','E','Z','U','O','H','X','S','C','V','F','M','T',
                                 'B','G','L','R','I','N','Q','J','W','A','Y','D','K'],
                "turnover_chars":['Y']
                },
            "II":{
                "wiring_chars":['Z','O','U','E','S','Y','D','K','F','W','P','C','I',
                                 'Q','X','H','M','V','B','L','G','N','J','R','A','T'],
                "turnover_chars":['E']
                },
            "III":{
                "wiring_chars":['E','H','R','V','X','G','A','O','B','Q','U','S','I',
                                 'M','Z','F','L','Y','N','W','K','T','P','D','J','C'],
                "turnover_chars":['N']
                }
            },
        "REFLECTORS":{
            "UKW":{
                "wiring_chars":['I','M','E','T','C','G','F','R','A','Y','S','Q','B',
                                 'Z','X','W','L','H','K','D','V','U','P','O','J','N'],
                "mode":"fixed"
                }
            },
        "RING_CHARACTERS":LETTERS,
        "ROTOR_GROUP_CELLS":{"R1":"R_ROT",
                             "R2":"R_ROT",
                             "R3":"R_ROT",
                             "REF":"R_REF"},
        "PLUGBOARD":None
    },

	"RAILWAY ENIGMA":{
	    "ENTRY_WHEEL":QWERTZ,
        "ROTORS":{
            "I":{
                "wiring_chars":['J','G','D','Q','O','X','U','S','C','A','M','I','F',
                                 'R','V','T','P','N','E','W','K','B','L','Z','Y','H'],
                "turnover_chars":['N']
                },
            "II":{
                "wiring_chars":['N','T','Z','P','S','F','B','O','K','M','W','R','C',
                                 'J','D','I','V','L','A','E','Y','U','X','H','G','Q'],
                "turnover_chars":['E']
                },
            "III":{
                "wiring_chars":['J','V','I','U','B','H','T','C','D','Y','A','K','E',
                                 'Q','Z','P','O','S','G','X','N','R','M','W','F','L'],
                "turnover_chars":['Y']
                }
            },
        "REFLECTORS":{
            "UKW":{
                "wiring_chars":['Q','Y','H','O','G','N','E','C','V','P','U','Z','T',
                                 'F','D','J','A','X','W','M','K','I','S','R','B','L'],
                "mode":"fixed"
                }
            },
        "RING_CHARACTERS":LETTERS,
        "ROTOR_GROUP_CELLS":{"R1":"R_ROT",
                             "R2":"R_ROT",
                             "R3":"R_ROT",
                             "REF":"F_REF"},
        "PLUGBOARD":None
    },

	"ENIGMA T":{
	    "ENTRY_WHEEL":['K','Z','R','O','U','Q','H','Y','A','I','G','B','L',
	                   'W','V','S','T','D','X','F','P','N','M','C','J','E'],
        "ROTORS":{
            "I":{
                "wiring_chars":['K','P','T','Y','U','E','L','O','C','V','G','R','F',
                                 'Q','D','A','N','J','M','B','S','W','H','Z','X','I'],
                "turnover_chars":['W','Z','E','K','Q']
                },
            "II":{
                "wiring_chars":['U','P','H','Z','L','W','E','Q','M','T','D','J','X',
                                 'C','A','K','S','O','I','G','V','B','Y','F','N','R'],
                "turnover_chars":['W','Z','F','L','R']
                },
            "III":{
                "wiring_chars":['Q','U','D','L','Y','R','F','E','K','O','N','V','Z',
                                 'A','X','W','H','M','G','P','J','B','S','I','C','T'],
                "turnover_chars":['W','Z','E','K','Q']
                },
            "IV":{
                "wiring_chars":['C','I','W','T','B','K','X','N','R','E','S','P','F',
                                 'L','Y','D','A','G','V','H','Q','U','O','J','Z','M'],
                "turnover_chars":['W','Z','F','L','R']
                },
            "V":{
                "wiring_chars":['U','A','X','G','I','S','N','J','B','V','E','R','D',
                                 'Y','L','F','Z','W','T','P','C','K','O','H','M','Q'],
                "turnover_chars":['Y','C','F','K','R']
                },
            "VI":{
                "wiring_chars":['X','F','U','Z','G','A','L','V','H','C','N','Y','S',
                                 'E','W','Q','T','D','M','R','B','K','P','I','O','J'],
                "turnover_chars":['X','E','I','M','Q']
                },
            "VII":{
                "wiring_chars":['B','J','V','F','T','X','P','L','N','A','Y','O','Z',
                                 'I','K','W','G','D','Q','E','R','U','C','H','S','M'],
                "turnover_chars":['Y','C','F','K','R']
                },
            "VIII":{
                "wiring_chars":['Y','M','T','P','N','Z','H','W','K','O','D','A','J',
                                 'X','E','L','U','Q','V','G','C','B','I','S','F','R'],
                "turnover_chars":['X','E','I','M','Q']
                }
            },
        "REFLECTORS":{
            "UKW":{
                "wiring_chars":['G','E','K','P','B','T','A','U','M','O','C','N','I',
                                 'L','J','D','X','Z','Y','F','H','W','V','Q','S','R'],
                "mode":"fixed"
                }
            },
        "RING_CHARACTERS":LETTERS,
        "ROTOR_GROUP_CELLS":{"R1":"R_ROT",
                             "R2":"R_ROT",
                             "R3":"R_ROT",
                             "REF":"F_REF"},
        "PLUGBOARD":None
    }
}

KEYBOARD_DICT = {
        'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E', 'f':'F', 'g':'G', 'h':'H',
        'i':'I', 'j':'J', 'k':'K', 'l':'L', 'm':'M', 'n':'N', 'o':'O', 'p':'P',
        'q':'Q', 'r':'R', 's':'S', 't':'T', 'u':'U', 'v':'V', 'w':'W', 'x':'X',
        'y':'Y', 'z':'Z', 'A':'A', 'B':'B', 'C':'C', 'D':'D', 'E':'E', 'F':'F',
        'G':'G', 'H':'H', 'I':'I', 'J':'J', 'K':'K', 'L':'L', 'M':'M', 'N':'N',
        'O':'O', 'P':'P', 'Q':'Q', 'R':'R', 'S':'S', 'T':'T', 'U':'U', 'V':'V',
        'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z', '1':'Q', '2':'W', '3':'E', '4':'R',
        '5':'T', '6':'Z', '7':'U', '8':'I', '9':'O', '0':'P'
    }

ENIGMA_LAYOUT = {
      'FIRST_ROW':['Q','W','E','R','T','Z','U','I','O'],
      'SECOND_ROW':['A','S','D','F','G','H','J','K'],
      'THIRD_ROW':['P','Y','X','C','V','B','N','M','L']
    }

UHR_DICT = {
    'CONNECTIONS_LIST': [6, 31, 4, 29, 18, 39, 16, 25, 30, 23,
                         28, 1, 38, 11, 36, 37, 26, 27, 24, 21,
                         14, 3, 12, 17, 2, 7, 0, 33, 10, 35,
                         8, 5, 22, 19, 20, 13, 34, 15, 32, 9],

    'PLUG_A_MAP': {
        0: '01ALG', 2: '01ASM',
        4: '02ALG', 6: '02ASM',
        8: '03ALG', 10: '03ASM',
        12: '04ALG', 14: '04ASM',
        16: '05ALG', 18: '05ASM',
        20: '06ALG', 22: '06ASM',
        24: '07ALG', 26: '07ASM',
        28: '08ALG', 30: '08ASM',
        32: '09ALG', 34: '09ASM',
        36: '10ALG', 38: '10ASM'
    },

    'PLUG_B_MAP': {
        0: '07BLG', 2: '07BSM',
        4: '01BLG', 6: '01BSM',
        8: '08BLG', 10: '08BSM',
        12: '06BLG', 14: '06BSM',
        16: '02BLG', 18: '02BSM',
        20: '09BLG', 22: '09BSM',
        24: '05BLG', 26: '05BSM',
        28: '03BLG', 30: '03BSM',
        32: '10BLG', 34: '10BSM',
        36: '04BLG', 38: '04BSM'
    },

    'PLUGS_LIST': ['01A', '02A', '03A', '04A', '05A',
                   '06A', '07A', '08A', '09A', '10A',
                   '01B', '02B', '03B', '04B', '05B',
                   '06B', '07B', '08B', '09B', '10B', ]
    }

MORSE_CODE = {
      'A':'. _',
      'B':'_ . . .',
      'C':'_ . _ .',
      'D':'_ . .',
      'E':'.',
      'F':'. . _ .',
      'G':'_ _ .',
      'H':'. . . .',
      'I':'. .',
      'J':'. _ _ _',
      'K':'_ . _',
      'L':'. _ . .',
      'M':'_ _',
      'N':'_ .',
      'O':'_ _ _',
      'P':'. _ _ .',
      'Q':'_ _ . _',
      'R':'. _ .',
      'S':'. . .',
      'T':'_',
      'U':'. . _',
      'V':'. . . _',
      'W':'. _ _',
      'X':'_ . . _',
      'Y':'_ . _ _',
      'Z':'_ _ . .',
      '1':'. _ _ _ _',
      '2':'. . _ _ _',
      '3':'. . . _ _',
      '4':'. . . . _',
      '5':'. . . . .',
      '6':'_ . . . .',
      '7':'_ _ . . .',
      '8':'_ _ _ . .',
      '9':'_ _ _ _ .',
      '0':'_ _ _ _ _',
      '. _':'A',
      '_ . . .':'B',
      '_ . _ .':'C',
      '_ . .':'D',
      '.':'E',
      '. . _ .':'F',
      '_ _ .':'G',
      '. . . .':'H',
      '. .':'I',
      '. _ _ _':'J',
      '_ . _':'K',
      '. _ . .':'L',
      '_ _':'M',
      '_ .':'N',
      '_ _ _':'O',
      '. _ _ .':'P',
      '_ _ . _':'Q',
      '. _ .':'R',
      '. . .':'S',
      '_':'T',
      '. . _':'U',
      '. . . _':'V',
      '. _ _':'W',
      '_ . . _':'X',
      '_ . _ _':'Y',
      '_ _ . .':'Z',
      '. _ _ _ _':'1',
      '. . _ _ _':'2',
      '. . . _ _':'3',
      '. . . . _':'4',
      '. . . . .':'5',
      '_ . . . .':'6',
      '_ _ . . .':'7',
      '_ _ _ . .':'8',
      '_ _ _ _ .':'9',
      '_ _ _ _ _':'0'
}