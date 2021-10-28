import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="y", parent_name="streamtube", **kwargs):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            **kwargs
        )