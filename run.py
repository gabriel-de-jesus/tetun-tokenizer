import tetun_tokenizer

if __name__ == '__main__':
    tokenizer = tetun_tokenizer.TetunWordTokenizer()
    text = """Iha 2002, iha 20.000.0000,204, Timór Lorosa'e (Ofisiál iha lia-tetun: Timor-Leste, lia-portugés: Timor-Leste, lia-inglés: East Timor, lia-indonézia: Timor Timur) 
    hanesan nasaun ida ne'ebé moris ikus liu iha mundo rai klaran, tur iha fatin sorin Timur iha Rain Timór, iha sorin ida hetan rai Timór 
    nian rohan hanesan Oe-Kusi (Oe-Kusi Ambenu), iha fali lolon sorin nian kotuk mak Ataúru, nune'e mos iha rain ki'ik oan balu ne'ebé tur 
    iha lolon sorin Timur nian ne'ebá. Rai Timór iha fronteira ho rai seluk mesak ida deit, mak rai Indonézia nian sorin ne'ebé tutan malu ho 

    iha sorin loro-monu ne'ebé fahe malu ho sorin loro-sa'e, iha mos rai sorin nebe tutan malu ho Oe-Kusi. 
    Maibé iha mos fonteira iha tasi ne'ebé ketak malu ho Austrália, Tasi Timór iha kanosan sorin. Dili mak sidade boot liu hotu no hanesan sidade inan ba Timór. 
    Ângela Érica Maria Soares Gusmão Conceição.
    """

    text_for_sentence = "Ha'u ema-ida ne'ebé baibain de'it. Tebes ká? Ita-nia maluk Dr. ka Ph.D sira hosi U.S.A mós dehan!"

    print(tokenizer.tokenize(text))
