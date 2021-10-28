import sys

if sys.version_info < (3, 7):
    from ._colorbar import ColorBar
    from ._contours import Contours
    from ._hoverlabel import Hoverlabel
    from ._legendgrouptitle import Legendgrouptitle
    from ._line import Line
    from ._marker import Marker
    from ._stream import Stream
    from ._xbins import XBins
    from ._ybins import YBins
    from . import colorbar
    from . import contours
    from . import hoverlabel
    from . import legendgrouptitle
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".colorbar", ".contours", ".hoverlabel", ".legendgrouptitle"],
        [
            "._colorbar.ColorBar",
            "._contours.Contours",
            "._hoverlabel.Hoverlabel",
            "._legendgrouptitle.Legendgrouptitle",
            "._line.Line",
            "._marker.Marker",
            "._stream.Stream",
            "._xbins.XBins",
            "._ybins.YBins",
        ],
    )
