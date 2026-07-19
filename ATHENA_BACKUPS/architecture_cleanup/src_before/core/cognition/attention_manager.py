from src.core.logger.logger import AthenaLogger


class AttentionManager:

    def __init__(self):

        self.focus = None

        AthenaLogger.info(
            "Attention Manager initialized."
        )

    def set_focus(self, objective):

        self.focus = objective

    def clear(self):

        self.focus = None

    def current(self):

        return self.focus
