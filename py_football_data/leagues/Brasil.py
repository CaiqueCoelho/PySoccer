from .LeagueBase import LeagueBase
from ..constants.urls import urls


class Brasil(LeagueBase):
    def __init__(self):
        super().__init__(urls.get_url_brazil_serie_a())

    def leaderboard(self, ano: str = "2020"):
        self.url = urls.get_url_leaderboard_complete_brazil_serie_a(ano)
        return super().leaderboard(ano=ano)