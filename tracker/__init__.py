__app_name__ = 'crypto-tracker'
__version__ = '0.1.0'

(
    SUCCESS,
    DIR_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(4)

ERRORS = {
    DIR_ERROR: "config directory error",
    ID_ERROR: "id asset error",
}