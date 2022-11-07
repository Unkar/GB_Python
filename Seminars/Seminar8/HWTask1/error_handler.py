import config
import json
import log
import UI


def error_window(e, session_id = None):
    UI.error_window(e)
    log.add_log("error", session_id, "main", str(e))
