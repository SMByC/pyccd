from collections import namedtuple
import copy

# TODO: establish standardize object for handling models used for general
# regression purposes. This will truly make the code much more modular.

# Because scipy models don't hold information on residuals or rmse, we should
# carry them forward with the models themselves, so we don't have to
# recalculate them all the time
# TODO: give better names to avoid model.model.predict nonsense
FittedModel = namedtuple('FittedModel', ['fitted_model', 'residual', 'rmse'])


def results_to_changemodel(fitted_models, start_day, end_day, break_day,
                           magnitudes, observation_count, change_probability,
                           curve_qa):
    """
    Helper method to consolidate results into a concise, self documenting data
    structure.

    This also converts any specific package types used during processing to
    standard python types to help with downstream processing.

    {start_day: int,
     end_day: int,
     break_day: int,
     observation_count: int,
     change_probability: float,
     curve_qa: int,
     blue:  {magnitude: float,
             rmse: float,
             coefficients: (float, float, ...),
             intercept: float},
     etc...

    Returns:
        dict

    """
    spectral_models = []
    for ix, model in enumerate(fitted_models):
        spectral = {'rmse': float(model.rmse),
                    'coefficients': tuple(float(c) for c in
                                          model.fitted_model.coef_),
                    'intercept': float(model.fitted_model.intercept_),
                    'magnitude': float(magnitudes[ix])}
        spectral_models.append(spectral)

    return {'start_day': int(start_day),
            'end_day': int(end_day),
            'break_day': int(break_day),
            'observation_count': int(observation_count),
            'change_probability': float(change_probability),
            'curve_qa': int(curve_qa),
            'blue': spectral_models[0],
            'green': spectral_models[1],
            'red': spectral_models[2],
            'nir': spectral_models[3],
            'swir1': spectral_models[4],
            'swir2': spectral_models[5],
            'thermal': spectral_models[6]}


def results_fromprev(prev):
    """
    Load a previous set results to begin updating with some new forward
    observations. This will trim off any segments identified as "end fits", so
    that they can possibly updated with more stable segments.

    Args:
        prev: dictionary of previous pyccd results

    Returns:
        list of dictionaries
    """
    prev_models = sorted(prev['change_models'], key=lambda x: x['start_day'])

    for idx, model in enumerate(prev_models[::-1]):
        if model['change_probability'] == 0:
            continue
        elif idx == 0:
            return [copy.deepcopy(m) for m in prev_models]
        else:
            return [copy.deepcopy(m) for m in prev_models[:-idx]]

    return []
