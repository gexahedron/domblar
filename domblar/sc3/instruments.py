import time

def setup_instruments(client, instrument_count, vst_name, preset_name):
    # TODO: this code is specific to Dexed VST, needs generalization
    assert vst_name == 'Dexed.vst3'

    data = [instrument_count] + [vst_name] * instrument_count
    client.send_msg('/vst_setup', data)
    time.sleep(5.0)

    for i in range(instrument_count):
        client.load_preset(i, preset_name)

    instruments = {}
    # parameters for Dexed VST
    instruments['brass/toto_africa'] = [ 1.0, 0.0, 1.0, 0.5, 0.54838711023331, 0.85714286565781, 1.0, 0.35353535413742, 0.0, 0.050505049526691, 0.0, 0.0, 0.0, 0.25, 0.4285714328289, 0.94949495792389, 0.67676764726639, 0.95959597826004, 0.60606062412262, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.55555558204651, 0.24242424964905, 0.19191919267178, 0.55555558204651, 1.0, 0.86868685483932, 0.86868685483932, 0.0, 1.0, 0.0, 0.032258063554764, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.28571429848671, 0.0, 0.28571429848671, 1.0, 0.3737373650074, 0.34343433380127, 0.15151515603065, 0.70707070827484, 0.85858583450317, 0.0, 0.0, 0.0, 0.70707070827484, 0.0, 0.032258063554764, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.28571429848671, 0.0, 0.14285714924335, 1.0, 0.46464645862579, 0.35353535413742, 0.22222222387791, 0.50505048036575, 1.0, 0.86868685483932, 0.86868685483932, 0.0, 0.77777779102325, 0.0, 0.032258063554764, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.14285714924335, 0.0, 0.14285714924335, 1.0, 0.66666668653488, 0.92929291725159, 0.22222222387791, 0.50505048036575, 0.53535354137421, 0.61616164445877, 0.62626260519028, 0.0, 0.79797977209091, 0.0, 0.032258063554764, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.4848484992981, 0.55555558204651, 0.22222222387791, 0.50505048036575, 0.98989897966385, 0.61616164445877, 0.62626260519028, 0.0, 0.70707070827484, 0.0, 0.096774190664291, 0.060606062412262, 0.4285714328289, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.77777779102325, 0.56565654277802, 0.20202019810677, 0.70707070827484, 1.0, 0.0, 0.0, 0.0, 0.79797977209091, 0.0, 0.22580644488335, 0.21212121844292, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0 ]
    instruments['brass3'] = instruments['brass/toto_africa']
    instruments['tub_bells'] = [ 1.0, 0.0, 1.0, 0.5, 0.12903225421906, 1.0, 0.0, 0.35353535413742, 0.0, 0.0, 0.0, 0.0, 0.20000000298023, 0.5, 0.14285714924335, 0.67676764726639, 0.95959597826004, 0.95959597826004, 0.60606062412262, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.95959597826004, 0.33333334326744, 0.71717172861099, 0.25252524018288, 1.0, 0.0, 0.32323232293129, 0.0, 0.95959597826004, 0.0, 0.032258063554764, 0.0, 0.64285713434219, 0.0, 0.0, 0.0, 0.0, 0.0, 0.28571429848671, 0.0, 0.0, 1.0, 0.98989897966385, 0.12121212482452, 0.71717172861099, 0.28282827138901, 1.0, 0.0, 0.32323232293129, 0.0, 0.78787881135941, 0.0, 0.064516127109528, 0.75757575035095, 0.71428573131561, 0.0, 0.0, 0.0, 0.0, 0.0, 0.28571429848671, 0.0, 0.0, 1.0, 0.95959597826004, 0.33333334326744, 0.71717172861099, 0.25252524018288, 1.0, 0.0, 0.32323232293129, 0.0, 1.0, 0.0, 0.032258063554764, 0.0, 0.14285714924335, 0.0, 0.0, 0.0, 0.0, 0.0, 0.28571429848671, 0.0, 0.0, 1.0, 0.98989897966385, 0.12121212482452, 0.71717172861099, 0.28282827138901, 1.0, 0.0, 0.32323232293129, 0.0, 0.75757575035095, 0.0, 0.064516127109528, 0.75757575035095, 0.35714286565781, 0.0, 0.0, 0.0, 0.0, 0.0, 0.28571429848671, 0.0, 0.0, 1.0, 0.7676767706871, 0.78787881135941, 0.71717172861099, 0.70707070827484, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.064516127109528, 0.5151515007019, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.28571429848671, 0.0, 0.71428573131561, 1.0, 0.98989897966385, 0.91919189691544, 0.0, 0.28282827138901, 1.0, 0.0, 0.0, 0.0, 0.85858583450317, 0.0, 0.064516127109528, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.28571429848671, 0.0, 0.0, 1.0 ]
    instruments['strings10'] = [ 1.0, 0.0, 1.0, 0.5, 0.032258063554764, 1.0, 1.0, 0.45454546809196, 0.71717172861099, 0.10101009905338, 0.29292929172516, 0.0, 0.80000001192093, 0.25, 0.14285714924335, 1.0, 1.0, 1.0, 1.0, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.30303031206131, 0.15151515603065, 0.12121212482452, 0.35353535413742, 0.90909093618393, 0.90909093618393, 0.90909093618393, 0.0, 1.0, 0.0, 0.032258063554764, 0.0, 0.5, 0.0, 0.0, 0.050505049526691, 0.0, 0.66666668653488, 0.14285714924335, 0.0, 0.28571429848671, 1.0, 1.0, 0.15151515603065, 0.10101009905338, 0.10101009905338, 0.96969699859619, 0.9797979593277, 0.9797979593277, 0.96969699859619, 0.78787881135941, 0.0, 0.032258063554764, 0.0, 0.5, 0.44444444775581, 0.0, 0.28282827138901, 0.33333334326744, 0.66666668653488, 0.0, 0.0, 0.0, 1.0, 0.40404039621353, 0.27272728085518, 0.10101009905338, 0.35353535413742, 0.72727274894714, 0.92929291725159, 0.92929291725159, 0.0, 0.9797979593277, 0.0, 0.032258063554764, 0.010101010091603, 0.5, 0.0, 0.0, 0.0, 1.0, 0.0, 0.28571429848671, 0.0, 0.28571429848671, 1.0, 1.0, 0.4848484992981, 0.10101009905338, 0.15151515603065, 0.89898991584778, 0.89898991584778, 0.89898991584778, 0.81818181276321, 0.79797977209091, 0.0, 0.032258063554764, 0.010101010091603, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.50505048036575, 0.12121212482452, 0.13131313025951, 0.91919189691544, 0.88888889551163, 0.86868685483932, 0.80808079242706, 0.83838385343552, 1.0, 0.12903225421906, 0.46464645862579, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.33333334326744, 0.0, 1.0, 1.0, 0.4848484992981, 0.10101009905338, 0.15151515603065, 0.89898991584778, 0.89898991584778, 0.89898991584778, 0.81818181276321, 0.96969699859619, 0.0, 0.032258063554764, 0.010101010091603, 0.4285714328289, 0.0, 0.0, 0.0, 0.0, 0.33333334326744, 0.0, 0.0, 0.0, 1.0 ]

    # this one has very weird release sound
    instruments['harpsich1'] = [ 1.0, 0.0, 1.0, 0.5, 0.12903225421906, 0.14285714924335, 1.0, 0.35353535413742, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.28571429848671, 0.0, 0.0, 0.0, 0.0, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.95959597826004, 0.28282827138901, 0.27272728085518, 0.47474747896194, 1.0, 0.90909093618393, 0.0, 0.0, 0.89898991584778, 0.0, 0.12903225421906, 0.0, 0.5, 0.49494948983192, 0.0, 0.0, 0.0, 0.0, 0.4285714328289, 0.0, 0.28571429848671, 1.0, 0.95959597826004, 0.72727274894714, 0.71717172861099, 1.0, 1.0, 0.9797979593277, 0.91919189691544, 0.98989897966385, 1.0, 0.0, 0.0, 0.0, 0.5, 0.49494948983192, 0.0, 0.0, 0.0, 0.0, 0.14285714924335, 0.0, 0.0, 1.0, 0.95959597826004, 0.28282827138901, 0.27272728085518, 0.47474747896194, 1.0, 0.90909093618393, 0.0, 0.0, 0.85858583450317, 0.0, 0.032258063554764, 0.0, 0.4285714328289, 0.49494948983192, 0.0, 0.0, 0.0, 0.0, 0.4285714328289, 0.0, 0.28571429848671, 1.0, 0.95959597826004, 0.72727274894714, 0.71717172861099, 1.0, 1.0, 0.9797979593277, 0.91919189691544, 0.98989897966385, 1.0, 0.0, 0.096774190664291, 0.0, 0.5, 0.64646464586258, 0.0, 0.46464645862579, 0.0, 0.0, 0.14285714924335, 0.0, 0.0, 1.0, 0.95959597826004, 0.28282827138901, 0.27272728085518, 0.47474747896194, 1.0, 0.90909093618393, 0.0, 0.0, 0.83838385343552, 0.0, 0.12903225421906, 0.0, 0.4285714328289, 0.49494948983192, 0.0, 0.0, 0.0, 0.0, 0.4285714328289, 0.0, 0.4285714328289, 1.0, 0.95959597826004, 0.72727274894714, 0.71717172861099, 1.0, 1.0, 0.9797979593277, 0.91919189691544, 0.98989897966385, 0.87878787517548, 0.0, 0.19354838132858, 0.0, 0.5, 0.64646464586258, 0.0, 0.55555558204651, 0.0, 0.0, 0.14285714924335, 0.0, 0.0, 1.0 ]

    # this one also has problems with release
    instruments['vibraphone/dune_water'] = [ 1.0, 0.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.33333334326744, 0.0, 0.0, 1.0, 1.0, 0.80000001192093, 0.25, 0.0, 0.98989897966385, 0.98989897966385, 0.98989897966385, 0.98989897966385, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.64646464586258, 0.33333334326744, 1.0, 0.5151515007019, 0.91919189691544, 0.25252524018288, 0.0, 0.0, 1.0, 0.0, 0.12903225421906, 0.0, 0.85714286565781, 0.3939394056797, 0.15151515603065, 0.12121212482452, 1.0, 1.0, 0.57142859697342, 1.0, 0.0, 1.0, 1.0, 0.91919189691544, 0.22222222387791, 0.46464645862579, 0.90909093618393, 0.90909093618393, 0.0, 0.0, 0.79797977209091, 1.0, 0.032258063554764, 0.0, 0.5, 0.3939394056797, 0.0, 0.0, 1.0, 0.0, 0.57142859697342, 0.0, 0.4285714328289, 1.0, 0.77777779102325, 0.70707070827484, 0.45454546809196, 0.56565654277802, 0.90909093618393, 0.83838385343552, 0.0, 0.73737370967865, 0.98989897966385, 0.0, 0.032258063554764, 0.0, 0.5, 0.3939394056797, 0.0, 0.12121212482452, 0.0, 1.0, 0.57142859697342, 0.0, 0.0, 1.0, 0.80808079242706, 0.88888889551163, 0.24242424964905, 0.46464645862579, 1.0, 0.90909093618393, 0.0, 0.0, 1.0, 0.0, 0.12903225421906, 0.0, 0.5, 0.090909093618393, 0.0, 0.0, 0.33333334326744, 0.33333334326744, 0.57142859697342, 1.0, 0.0, 1.0, 0.80808079242706, 0.32323232293129, 0.25252524018288, 0.42424243688583, 0.96969699859619, 0.90909093618393, 0.19191919267178, 0.0, 1.0, 0.0, 0.12903225421906, 0.0, 0.5, 0.090909093618393, 0.0, 0.0, 0.33333334326744, 0.33333334326744, 0.57142859697342, 0.0, 0.0, 1.0, 1.0, 0.2323232293129, 1.0, 0.38383838534355, 0.59595960378647, 0.32323232293129, 0.0, 0.19191919267178, 0.75757575035095, 0.0, 0.38709676265717, 0.0, 0.5, 0.3939394056797, 0.12121212482452, 0.5151515007019, 0.0, 0.0, 0.57142859697342, 0.0, 0.0, 1.0 ]

    instruments['bass_drum1'] = [ 1.0, 0.0, 1.0, 0.5, 0.16129031777382, 0.0, 1.0, 0.34343433380127, 0.33333334326744, 0.0, 0.0, 1.0, 0.80000001192093, 0.5, 0.0, 0.98989897966385, 0.87878787517548, 0.50505048036575, 0.42424243688583, 0.50505048036575, 0.0, 0.0, 0.0, 0.98989897966385, 0.50505048036575, 0.57575756311417, 0.57575756311417, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.032258063554764, 0.75757575035095, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.57142859697342, 0.0, 0.0, 1.0, 0.81818181276321, 0.54545456171036, 0.85858583450317, 0.85858583450317, 1.0, 0.90909093618393, 0.0, 0.0, 0.59595960378647, 1.0, 0.29032257199287, 0.75757575035095, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.57142859697342, 0.0, 0.0, 1.0, 0.88888889551163, 0.57575756311417, 0.56565654277802, 0.56565654277802, 1.0, 0.94949495792389, 0.0, 0.0, 1.0, 1.0, 0.032258063554764, 0.75757575035095, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.57142859697342, 0.0, 0.0, 1.0, 1.0, 0.89898991584778, 0.81818181276321, 0.81818181276321, 1.0, 0.90909093618393, 0.0, 0.0, 0.87878787517548, 1.0, 0.032258063554764, 0.94949495792389, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.57142859697342, 0.0, 0.0, 1.0, 0.93939393758774, 0.7676767706871, 0.89898991584778, 0.89898991584778, 1.0, 0.94949495792389, 0.0, 0.0, 0.94949495792389, 1.0, 0.80645161867142, 0.7676767706871, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.57142859697342, 0.0, 0.0, 1.0, 1.0, 0.57575756311417, 0.77777779102325, 0.77777779102325, 1.0, 1.0, 1.0, 0.0, 0.9797979593277, 1.0, 0.064516127109528, 0.56565654277802, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.57142859697342, 0.0, 0.0, 1.0 ]
    instruments['log_drum'] = [ 1.0, 0.0, 1.0, 0.5, 0.41935482621193, 0.71428573131561, 1.0, 0.44444444775581, 0.28282827138901, 0.1414141356945, 0.80808079242706, 0.0, 0.20000000298023, 0.25, 1.0, 0.98989897966385, 0.98989897966385, 0.98989897966385, 0.98989897966385, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.88888889551163, 0.47474747896194, 0.46464645862579, 0.46464645862579, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4285714328289, 0.0, 0.0, 1.0, 1.0, 0.77777779102325, 0.42424243688583, 0.35353535413742, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.83838385343552, 0.20202019810677, 0.50505048036575, 0.41414141654968, 1.0, 0.27272728085518, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.5, 0.15151515603065, 0.0, 0.0, 0.0, 0.33333334326744, 0.4285714328289, 0.0, 0.0, 1.0, 0.90909093618393, 0.58585858345032, 0.50505048036575, 0.41414141654968, 0.96969699859619, 0.27272728085518, 0.0, 0.0, 0.98989897966385, 0.0, 0.032258063554764, 0.020202020183206, 0.71428573131561, 0.15151515603065, 0.0, 0.0, 0.0, 0.33333334326744, 0.85714286565781, 0.0, 0.0, 1.0, 0.7474747300148, 0.87878787517548, 0.50505048036575, 0.41414141654968, 0.87878787517548, 0.27272728085518, 0.0, 0.0, 0.98989897966385, 0.0, 0.032258063554764, 0.040404040366411, 0.4285714328289, 0.15151515603065, 0.0, 0.0, 0.0, 0.33333334326744, 1.0, 0.0, 0.0, 1.0, 0.56565654277802, 0.77777779102325, 0.50505048036575, 0.41414141654968, 1.0, 0.9797979593277, 0.68686866760254, 0.0, 0.10101009905338, 0.0, 0.064516127109528, 0.020202020183206, 0.57142859697342, 0.15151515603065, 0.0, 0.0, 0.0, 0.33333334326744, 1.0, 0.0, 0.0, 1.0 ]
    instruments['snare1'] = [ 1.0, 0.0, 1.0, 0.5, 0.32258063554764, 1.0, 1.0, 0.55555558204651, 0.0, 0.0, 0.0, 0.0, 0.60000002384186, 1.0, 0.0, 0.98989897966385, 0.98989897966385, 0.98989897966385, 0.98989897966385, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.90909093618393, 0.4848484992981, 0.33333334326744, 0.4848484992981, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.83870965242386, 0.31313130259514, 0.5, 1.0, 0.98989897966385, 0.98989897966385, 1.0, 0.0, 0.4285714328289, 0.0, 0.4285714328289, 1.0, 1.0, 0.78787881135941, 0.20202019810677, 0.20202019810677, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.41935482621193, 0.53535354137421, 0.71428573131561, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4285714328289, 1.0, 1.0, 1.0, 0.35353535413742, 0.57575756311417, 1.0, 0.90909093618393, 0.0, 0.0, 0.63636362552643, 1.0, 0.7096773982048, 0.28282827138901, 0.28571429848671, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4285714328289, 1.0, 0.89898991584778, 0.61616164445877, 1.0, 0.61616164445877, 1.0, 0.0, 0.0, 0.0, 0.93939393758774, 1.0, 0.83870965242386, 0.41414141654968, 0.5, 0.56565654277802, 0.98989897966385, 0.0, 0.66666668653488, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.50505048036575, 0.0, 0.71717172861099, 0.0, 0.0, 0.90909093618393, 1.0, 0.0, 0.98989897966385, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.070707067847252, 1.0, 0.20202019810677, 1.0, 0.57575756311417, 1.0, 0.0, 1.0, 1.0, 0.87096774578094, 0.73737370967865, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0 ]
    instruments['snare2'] = [ 1.0, 0.0, 1.0, 0.5, 0.38709676265717, 1.0, 1.0, 0.090909093618393, 0.33333334326744, 0.0, 0.0, 1.0, 0.20000000298023, 0.5, 1.0, 0.58585858345032, 0.49494948983192, 0.98989897966385, 0.98989897966385, 1.0, 0.0, 0.0, 0.0, 1.0, 0.57575756311417, 0.52525252103806, 0.60606062412262, 1.0, 0.94949495792389, 0.0, 0.0, 1.0, 1.0, 0.064516127109528, 0.13131313025951, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.14285714924335, 1.0, 1.0, 1.0, 0.1414141356945, 0.33333334326744, 0.91919189691544, 0.22222222387791, 0.0, 0.0, 0.94949495792389, 1.0, 0.19354838132858, 0.58585858345032, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.79797977209091, 0.4848484992981, 0.60606062412262, 0.60606062412262, 1.0, 0.94949495792389, 0.0, 0.0, 0.78787881135941, 1.0, 0.32258063554764, 0.31313130259514, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.34343433380127, 0.34343433380127, 0.3737373650074, 1.0, 0.90909093618393, 0.0, 0.0, 0.64646464586258, 1.0, 0.064516127109528, 0.54545456171036, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.3939394056797, 0.45454546809196, 0.71717172861099, 1.0, 0.64646464586258, 0.0, 0.0, 0.65656566619873, 1.0, 0.83870965242386, 0.050505049526691, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.17171716690063, 0.28282827138901, 0.41414141654968, 1.0, 0.78787881135941, 0.0, 0.0, 1.0, 1.0, 0.096774190664291, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0 ]
    instruments['closed_hi_hat'] = [ 1.0, 0.0, 1.0, 0.5, 0.25806450843811, 1.0, 1.0, 0.35353535413742, 0.0, 0.0, 0.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.92929291725159, 0.66666668653488, 0.58585858345032, 0.67676764726639, 1.0, 0.17171716690063, 1.0, 0.0, 1.0, 1.0, 0.51612901687622, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.14285714924335, 1.0, 1.0, 0.85858583450317, 1.0, 0.72727274894714, 0.82828283309937, 0.82828283309937, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.52525252103806, 0.45454546809196, 0.71717172861099, 1.0, 0.82828283309937, 0.060606062412262, 0.0, 1.0, 1.0, 1.0, 0.82828283309937, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.57142859697342, 1.0, 1.0, 1.0, 0.85858583450317, 0.3939394056797, 1.0, 1.0, 0.60606062412262, 1.0, 1.0, 1.0, 0.22580644488335, 0.66666668653488, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.32323232293129, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.36363637447357, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.94949495792389, 1.0, 0.74193549156189, 0.86868685483932, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0 ]
    instruments['hi_hat'] = [ 1.0, 0.0, 1.0, 0.5, 0.12903225421906, 1.0, 1.0, 0.35353535413742, 0.0, 0.0, 0.0, 1.0, 0.0, 0.5, 0.4285714328289, 0.98989897966385, 0.98989897966385, 0.98989897966385, 0.98989897966385, 0.50505048036575, 0.50505048036575, 0.50505048036575, 0.50505048036575, 1.0, 0.40404039621353, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.77419352531433, 0.46464645862579, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.40404039621353, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.41935482621193, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.35353535413742, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.21212121844292, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.30303031206131, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.36363637447357, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.95959597826004, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.20202019810677, 0.20202019810677, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.96969699859619, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0 ]

    instruments['timpani'] = [ 1.0, 0.0, 1.0, 0.5, 0.48387095332146, 1.0, 1.0, 0.11111111193895, 0.0, 0.16161616146564, 0.0, 0.0, 0.0, 0.5, 0.28571429848671, 0.98989897966385, 0.98989897966385, 0.75757575035095, 0.60606062412262, 0.50505048036575, 0.5151515007019, 0.50505048036575, 0.50505048036575, 0.91919189691544, 0.36363637447357, 0.98989897966385, 0.33333334326744, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4285714328289, 0.0, 1.0, 1.0, 1.0, 0.7676767706871, 0.26262626051903, 0.2323232293129, 1.0, 0.72727274894714, 1.0, 0.0, 0.80808079242706, 0.0, 0.0, 0.0, 0.71428573131561, 0.41414141654968, 0.0, 0.0, 0.0, 0.33333334326744, 0.57142859697342, 0.0, 0.14285714924335, 1.0, 1.0, 0.77777779102325, 0.26262626051903, 0.2323232293129, 1.0, 0.72727274894714, 0.0, 0.0, 0.85858583450317, 0.0, 0.0, 0.36363637447357, 0.28571429848671, 0.0, 0.0, 0.0, 0.0, 0.33333334326744, 0.4285714328289, 0.0, 0.0, 1.0, 0.65656566619873, 0.31313130259514, 0.17171716690063, 0.30303031206131, 1.0, 0.75757575035095, 0.0, 0.0, 0.87878787517548, 0.0, 0.0, 0.75757575035095, 0.5, 0.41414141654968, 0.0, 0.15151515603065, 1.0, 0.0, 0.4285714328289, 0.0, 0.85714286565781, 1.0, 1.0, 0.50505048036575, 0.26262626051903, 0.19191919267178, 1.0, 0.0, 0.0, 0.0, 0.73737370967865, 0.0, 0.0, 0.0, 0.5, 0.80808079242706, 0.0, 0.0, 1.0, 0.33333334326744, 0.0, 0.0, 0.14285714924335, 1.0, 0.98989897966385, 0.020202020183206, 0.26262626051903, 0.27272728085518, 0.98989897966385, 0.0, 0.0, 0.0, 0.73737370967865, 0.0, 0.0, 0.56565654277802, 0.5, 0.41414141654968, 0.0, 0.24242424964905, 0.0, 0.0, 0.57142859697342, 0.0, 0.14285714924335, 1.0 ]
    instruments['timpani2'] = [ 1.0, 0.0, 1.0, 0.5, 0.48387095332146, 1.0, 1.0, 0.11111111193895, 0.0, 0.16161616146564, 0.0, 0.0, 0.0, 0.25, 0.28571429848671, 1.0, 0.98989897966385, 0.75757575035095, 0.60606062412262, 0.50505048036575, 0.5151515007019, 0.50505048036575, 0.50505048036575, 0.91919189691544, 0.36363637447357, 0.98989897966385, 0.46464645862579, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.5, 0.50505048036575, 0.0, 0.0, 0.0, 0.0, 0.4285714328289, 0.0, 1.0, 1.0, 0.80808079242706, 0.63636362552643, 0.26262626051903, 0.2323232293129, 1.0, 0.72727274894714, 0.0, 0.0, 0.80808079242706, 0.0, 0.0, 0.0, 0.71428573131561, 0.41414141654968, 0.0, 0.0, 0.0, 0.33333334326744, 0.57142859697342, 0.0, 0.14285714924335, 1.0, 0.7676767706871, 0.77777779102325, 0.26262626051903, 0.2323232293129, 1.0, 0.72727274894714, 0.0, 0.0, 0.85858583450317, 0.0, 0.0, 0.36363637447357, 0.28571429848671, 0.0, 0.0, 0.0, 0.0, 0.33333334326744, 0.4285714328289, 0.0, 0.4285714328289, 1.0, 0.65656566619873, 0.31313130259514, 0.17171716690063, 0.32323232293129, 1.0, 0.75757575035095, 0.0, 0.0, 0.87878787517548, 0.0, 0.0, 0.75757575035095, 0.5, 0.41414141654968, 0.0, 0.15151515603065, 1.0, 0.0, 0.4285714328289, 0.0, 0.85714286565781, 1.0, 0.75757575035095, 0.45454546809196, 0.26262626051903, 0.19191919267178, 1.0, 0.0, 0.0, 0.0, 0.73737370967865, 0.0, 0.0, 0.0, 0.5, 0.80808079242706, 0.0, 0.0, 1.0, 0.33333334326744, 0.0, 0.0, 0.14285714924335, 1.0, 0.98989897966385, 0.020202020183206, 0.26262626051903, 0.27272728085518, 0.98989897966385, 0.0, 0.0, 0.0, 0.73737370967865, 0.0, 0.0, 0.56565654277802, 0.5, 1.0, 0.0, 0.24242424964905, 0.0, 0.0, 0.57142859697342, 0.0, 0.14285714924335, 1.0 ]

    return instruments


def assign_instrument(synth_idx, instrument, instruments, client):
    data = [synth_idx, 0] + instruments[instrument]
    client.send_msg('/set_instrument', data)
    return
