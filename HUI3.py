# HUI3 regression coefficients

Constant_a = 1.371

Constant_b = 0.371

dicCoefficient = {'x1':         [1.00, 0.98, 0.89, 0.84, 0.75, 0.61],
                  'x2':         [1.00, 0.95, 0.89, 0.80, 0.74, 0.61],
                  'x3':         [1.00, 0.94, 0.89, 0.81, 0.68],
                  'x4':         [1.00, 0.93, 0.86, 0.73, 0.65, 0.58],
                  'x5':         [1.00, 0.95, 0.88, 0.76, 0.65, 0.56],
                  'x6':         [1.00, 0.95, 0.85, 0.64, 0.46],
                  'x7':         [1.00, 0.92, 0.95, 0.83, 0.60, 0.42],
                  'x8':         [1.00, 0.96, 0.90, 0.77, 0.55]}
def get_Score(x1,x2,x3,x4,x5,x6,x7,x8):
    """

    :param x1: Vision
    :param x2: Hearing
    :param x3: Speech
    :param x4: Ambulation
    :param x5: Dexterity
    :param x6: Emotion
    :param x7: Cognition
    :param x8: Pain
    :return: HUI3 reference score
    """

    if not(x1 in [1, 2, 3, 4, 5, 6]):
        raise ValueError("Vision level can take only 1,2,3,4,5,6")
    if not(x2 in [1, 2, 3, 4, 5, 6]):
        raise ValueError("Hearing level can take only 1,2,3,4,5,6")
    if not(x3 in [1, 2, 3, 4, 5]):
        raise ValueError("Speech level can take only 1,2,3,4,5")
    if not(x4 in [1, 2, 3, 4, 5, 6]):
        raise ValueError("Ambulation level can take only 1,2,3,4,5,6")
    if not(x5 in [1, 2, 3, 4, 5, 6]):
        raise ValueError("Dexterity level can take only 1,2,3,4,5,6")
    if not(x6 in [1, 2, 3, 4, 5]):
        raise ValueError("Emotion level can take only 1,2,3,4,5")
    if not(x7 in [1, 2, 3, 4, 5, 6]):
        raise ValueError("Cognition level can take only 1,2,3,4,5,6")
    if not(x8 in [1, 2, 3, 4, 5]):
        raise ValueError("Pain level can take only 1,2,3,4,5")




    Score = [Constant_a * (dicCoefficient['x1'][x1] * dicCoefficient['x2'][x2] * dicCoefficient['x3'][x3] *
                           dicCoefficient['x4'][x4] * dicCoefficient['x5'][x5] * dicCoefficient['x6'][x6] *
                           dicCoefficient['x7'][x7] * dicCoefficient['x8'][x8]) - Constant_b]

    return Score