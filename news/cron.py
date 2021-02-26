from services import reset_all_votes


def reset_votes():
    """
    Cron task to call reset_all_votes function once a day.
    """
    reset_all_votes()
